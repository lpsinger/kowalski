import h5py
import os
import glob
import numpy as np
import pymongo
import json
import argparse
import traceback
import datetime
import pytz
from numba import jit
# from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


''' load config and secrets '''
with open('/app/config.json') as cjson:
    config = json.load(cjson)

with open('/app/secrets.json') as sjson:
    secrets = json.load(sjson)

for k in secrets:
    config[k].update(secrets.get(k, {}))


def utc_now():
    return datetime.datetime.now(pytz.utc)


def connect_to_db():
    """ Connect to the mongodb database

    :return:
    """
    try:
        # there's only one instance of DB, it's too big to be replicated
        _client = pymongo.MongoClient(host=config['database']['host'],
                                      port=config['database']['port'])
        # grab main database:
        _db = _client[config['database']['db']]
    except Exception as _e:
        raise ConnectionRefusedError
    try:
        # authenticate
        _db.authenticate(config['database']['user'], config['database']['pwd'])
    except Exception as _e:
        raise ConnectionRefusedError

    return _client, _db


def insert_db_entry(_db, _collection=None, _db_entry=None):
    """
        Insert a document _doc to collection _collection in DB.
        It is monitored for timeout in case DB connection hangs for some reason
    :param _collection:
    :param _db_entry:
    :return:
    """
    assert _collection is not None, 'Must specify collection'
    assert _db_entry is not None, 'Must specify document'
    try:
        _db[_collection].insert_one(_db_entry)
    except Exception as _e:
        print('Error inserting {:s} into {:s}'.format(str(_db_entry['_id']), _collection))
        traceback.print_exc()
        print(_e)


def insert_multiple_db_entries(_db, _collection=None, _db_entries=None):
    """
        Insert a document _doc to collection _collection in DB.
        It is monitored for timeout in case DB connection hangs for some reason
    :param _db:
    :param _collection:
    :param _db_entries:
    :return:
    """
    assert _collection is not None, 'Must specify collection'
    assert _db_entries is not None, 'Must specify documents'
    try:
        _db[_collection].insert_many(_db_entries, ordered=False)
    except pymongo.errors.BulkWriteError as bwe:
        print(bwe.details)
    except Exception as _e:
        traceback.print_exc()
        print(_e)


@jit
def deg2hms(x):
    """Transform degrees to *hours:minutes:seconds* strings.

    Parameters
    ----------
    x : float
        The degree value c [0, 360) to be written as a sexagesimal string.

    Returns
    -------
    out : str
        The input angle written as a sexagesimal string, in the
        form, hours:minutes:seconds.

    """
    assert 0.0 <= x < 360.0, 'Bad RA value in degrees'
    # ac = Angle(x, unit='degree')
    # hms = str(ac.to_string(unit='hour', sep=':', pad=True))
    # print(str(hms))
    _h = np.floor(x * 12.0 / 180.)
    _m = np.floor((x * 12.0 / 180. - _h) * 60.0)
    _s = ((x * 12.0 / 180. - _h) * 60.0 - _m) * 60.0
    hms = '{:02.0f}:{:02.0f}:{:07.4f}'.format(_h, _m, _s)
    # print(hms)
    return hms


@jit
def deg2dms(x):
    """Transform degrees to *degrees:arcminutes:arcseconds* strings.

    Parameters
    ----------
    x : float
        The degree value c [-90, 90] to be converted.

    Returns
    -------
    out : str
        The input angle as a string, written as degrees:minutes:seconds.

    """
    assert -90.0 <= x <= 90.0, 'Bad Dec value in degrees'
    # ac = Angle(x, unit='degree')
    # dms = str(ac.to_string(unit='degree', sep=':', pad=True))
    # print(dms)
    _d = np.floor(abs(x)) * np.sign(x)
    _m = np.floor(np.abs(x - _d) * 60.0)
    _s = np.abs(np.abs(x - _d) * 60.0 - _m) * 60.0
    dms = '{:02.0f}:{:02.0f}:{:06.3f}'.format(_d, _m, _s)
    # print(dms)
    return dms


def process_file(_file, _collection, _batch_size=2048, verbose=False):

    # connect to MongoDB:
    if verbose:
        print('Connecting to DB')
    _, _db = connect_to_db()
    if verbose:
        print('Successfully connected')

    print(f'processing {_file}')
    documents = []
    batch_num = 1

    with h5py.File(_file, 'r') as f:
        # print(list(f.keys()))
        dset = f['class_table']
        # for table in dset:
        #     print(table)
        #     print(dset[table].shape, dset[table].dtype)
        #     print(dset[table][0:5])
        #     input()

        total_entries = dset['axis1'].shape[0]

        for ei, entry in enumerate(dset['block0_values']):
            if verbose:
                print(f'processing entry #{ei+1} of {total_entries}')

            try:
                ra, dec, rf_score = entry
                objid, flag = dset['block1_values'][ei][0], dset['block2_values'][ei][0]
                # print(ra, dec, rf_score, objid, flag)
                # input()

                doc = dict()
                doc['objid'] = int(objid)
                doc['ra'] = float(ra)
                doc['dec'] = float(dec)
                doc['rf_score'] = float(rf_score)
                doc['flag'] = int(flag)

                # GeoJSON for 2D indexing
                doc['coordinates'] = {}
                # doc['coordinates']['epoch'] = doc['jd']
                _ra = doc['ra']
                _dec = doc['dec']
                _radec = [_ra, _dec]
                # string format: H:M:S, D:M:S
                # tic = time.time()
                _radec_str = [deg2hms(_ra), deg2dms(_dec)]
                # print(time.time() - tic)
                # print(_radec_str)
                doc['coordinates']['radec_str'] = _radec_str
                # for GeoJSON, must be lon:[-180, 180], lat:[-90, 90] (i.e. in deg)
                _radec_geojson = [_ra - 180.0, _dec]
                doc['coordinates']['radec_geojson'] = {'type': 'Point',
                                                       'coordinates': _radec_geojson}
                # radians:
                doc['coordinates']['radec'] = [_ra * np.pi / 180.0, _dec * np.pi / 180.0]

                # print(doc['coordinates'])

                # insert into collection. don't do that! too much overhead if one-by-one
                # db[_collection].insert_one(doc)
                # insert_db_entry(db, _collection=_collection, _db_entry=doc)
                documents.append(doc)

                # insert batch, then flush
                if len(documents) == _batch_size:
                    print(f'inserting batch #{batch_num} from {_file}')
                    insert_multiple_db_entries(_db, _collection=_collection, _db_entries=documents)
                    # flush:
                    documents = []
                    batch_num += 1

            except Exception as e:
                traceback.print_exc()
                print(e)
                continue

        # stuff left from the last file?
        if len(documents) > 0:
            print(f'inserting batch #{batch_num} from {_fits_file}')
            insert_multiple_db_entries(_db, _collection=_collection, _db_entries=documents)


if __name__ == '__main__':
    ''' Create command line argument parser '''
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description='')

    args = parser.parse_args()

    # connect to MongoDB:
    print('Connecting to DB')
    client, db = connect_to_db()
    print('Successfully connected')

    collection = 'AMSG_20180302'

    # create 2d index:
    print('Creating 2d index')
    db[collection].create_index([('coordinates.radec_geojson', '2dsphere'),
                                 ('_id', pymongo.ASCENDING)], background=True)

    # number of records to insert
    batch_size = 2048

    _location = '/_tmp/sgcat/'

    files = glob.glob(os.path.join(_location, 'dec*.h5'))

    print(f'# files to process: {len(files)}')

    # init threaded operations
    # pool = ThreadPoolExecutor(4)
    pool = ProcessPoolExecutor(12)

    for ff in files[::-1]:
        pool.submit(process_file, _file=ff, _collection=collection, _batch_size=batch_size, verbose=True)
        # process_file(_file=ff, _collection=collection, _batch_size=batch_size, verbose=True)

    # wait for everything to finish
    pool.shutdown(wait=True)

    print('All done')
