>Here, the available databases are listed. 
>Additionally, I list the databases that are planned to be added.


### <span class="badge badge-primary">ZTF_alerts</span>
##### <span class="badge badge-success">Available</span>
All ZTF alerts starting from February 9, 2018. Pushed from IPAC's Kafka cluster in real time.

<a href="https://github.com/Caltech-IPAC/ztf/blob/master/src/pl/avroalerts/schema/" target="_blank">AVRO packet schema description <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">ZTF_20180919</span>
##### <span class="badge badge-success">Available</span>
ZTF source catalog generated by Matthew Graham.

<hr/>

### <span class="badge badge-primary">TNS</span>
##### <span class="badge badge-success">Available</span>
Alerts from Transient Name Server. Gets updated every 10 minutes.

<a href="https://wis-tns.weizmann.ac.il/search" target="_blank">TNS search page <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">Gaia_DR2</span>
##### <span class="badge badge-success">Available</span>
Gaia Data Release 2 catalog (gaia_source table)

<a href="https://cosmos.esa.int/documents/29201/1645651/GDR2_DataModel_draft.pdf" target="_blank">Original data and format description (draft) <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">Gaia\_DR2\_WD</span>
##### <span class="badge badge-success">Available</span>
Gaia DR2-based catalog of known white dwarfs and CVs 


<hr/>

### <span class="badge badge-primary">Gaia\_DR2\_light\_curves</span>
##### <span class="badge badge-success">Available</span>
Light curves from Gaia Data Release 2 catalog (light_curves table)

Available fields:

```python
[('source_id', int),
 ('transit_id', int),
 ('band', str),
 ('time', float),
 ('mag', float),
 ('flux', float),
 ('flux_error', float),
 ('flux_over_error', float),
 ('rejected_by_photometry', bool),
 ('rejected_by_variability', bool),
 ('other_flags', int),
 ('solution_id', int)]
```

<hr/>

### <span class="badge badge-primary">Gaia_DR1</span>
##### <span class="badge badge-success">Available</span>
Gaia Data Release 1 catalog (gaia_source table)

<a href="https://gaia.esac.esa.int/documentation/GDR1/datamodel/Ch1/gaia_source.html" target="_blank">Original data and format description <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">PanSTARRS</span>
##### <span class="badge badge-success">Available</span>
A combination of ObjectThin and MeanObject tables from PanSTARRS DR1, namely:

From ObjectThin:<br>
objID, projectionID, skyCellID, objInfoFlag, qualityFlag, raMean, decMean, 
raMeanErr, decMeanErr, epochMean, nStackDetections, nDetections, ng, nr, ni, nz, ny

From MeanObject:<br>
gQfPerfect, gMeanPSFMag, gMeanPSFMagErr, gMeanPSFMagStd, gMeanPSFMagNpt,
gMeanPSFMagMin, gMeanPSFMagMax, gMeanKronMag, gMeanKronMagErr, gFlags,
rQfPerfect, rMeanPSFMag, rMeanPSFMagErr, rMeanPSFMagStd, rMeanPSFMagNpt,
rMeanPSFMagMin, rMeanPSFMagMax, rMeanKronMag, rMeanKronMagErr, rFlags,
iQfPerfect, iMeanPSFMag, iMeanPSFMagErr, iMeanPSFMagStd, iMeanPSFMagNpt,
iMeanPSFMagMin, iMeanPSFMagMax, iMeanKronMag, iMeanKronMagErr, iFlags,
zQfPerfect, zMeanPSFMag, zMeanPSFMagErr, zMeanPSFMagStd, zMeanPSFMagNpt,
zMeanPSFMagMin, zMeanPSFMagMax, zMeanKronMag, zMeanKronMagErr, zFlags,
yQfPerfect, yMeanPSFMag, yMeanPSFMagErr, yMeanPSFMagStd, yMeanPSFMagNpt,
yMeanPSFMagMin, yMeanPSFMagMax, yMeanKronMag, yMeanKronMagErr, yFlags

for all objects with nDetections> 2

<a href="https://outerspace.stsci.edu/display/PANSTARRS/PS1+ObjectThin+table+fields" target="_blank">Original data and format description for ObjectThin table <i class="fa fa-external-link" aria-hidden="true"></i></a><br>
<a href="https://outerspace.stsci.edu/display/PANSTARRS/PS1+MeanObject+table+fields" target="_blank">Original data and format description for MeanObject table <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">2MASS_PSC</span>
##### <span class="badge badge-success">Available</span>
2MASS Point Source catalog

<a href="https://www.ipac.caltech.edu/2mass/releases/allsky/doc/sec2_2a.html" target="_blank">Original data and format description <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">2MASS_XSC</span>
##### <span class="badge badge-success">Available</span>
2MASS Extended Source catalog

<a href="https://www.ipac.caltech.edu/2mass/releases/allsky/doc/sec2_3a.html" target="_blank">Original data and format description <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">CLU_20170106</span>
##### <span class="badge badge-success">Available</span>
Census of the Local Universe (CLU)

<a href="https://arxiv.org/pdf/1710.05016.pdf" target="_blank">Dave Cook's paper <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">CLU_20180513</span>
##### <span class="badge badge-success">Available</span>
Census of the Local Universe (CLU)

<a href="https://arxiv.org/pdf/1710.05016.pdf" target="_blank">Dave Cook's paper <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">IPHAS_DR2</span>
##### <span class="badge badge-success">Available</span>
The IPHAS DR2 Source Catalogue

<a href="http://www.iphas.org/dr2/" target="_blank">Original data and format description <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">TIC_7</span>
##### <span class="badge badge-success">Available</span>
The TESS Input Catalog v7

<a href="https://archive.stsci.edu/tess/bulk_downloads.html" target="_blank">Original data and format description <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">RFC_2017c</span>
##### <span class="badge badge-success">Available</span>
Radio Fundamental Catalog (RFC) 2017c

<a href="http://astrogeo.org/rfc/" target="_blank">Catalog of compact radio sources <i class="fa fa-external-link" aria-hidden="true"></i></a><br>
<a href="http://astrogeo.org/vlbi/solutions/rfc_2017c/rfc_2017c_cat.txt" target="_blank">Original catalog <i class="fa fa-external-link" aria-hidden="true"></i></a><br>
<a href="http://astrogeo.org/data_archive/vlbi_images.tar.bz2" target="_blank">Images and calibrated uv data (73 Gb) <i class="fa fa-external-link" aria-hidden="true"></i></a><br>
<a href="http://astrogeo.org/vlbi/solutions/rfc_2017c/rfc_2017c.spind" target="_blank">Spectral indices <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">NVSS_41</span>
##### <span class="badge badge-success">Available</span>
The NRAO VLA Sky Survey

<a href="http://www.cv.nrao.edu/nvss/" target="_blank">Original data and format description <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">FIRST_20141217</span>
##### <span class="badge badge-success">Available</span>
A radio catalog for the north and south Galactic caps (946,432 sources), derived from the 1993 through 2011 observations

<a href="http://sundog.stsci.edu/first/catalogs/readme_14dec17.html" target="_blank">Original data and format description <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">TGSS_ADR1</span>
##### <span class="badge badge-success">Available</span>
TIFR Giant Metrewave Radio Telescope (GMRT) Sky Survey (TGSS): the radio sky at 150 MHz (2010-2012)

<a href="http://tgssadr.strw.leidenuniv.nl/doku.php" target="_blank">Original data and format description <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">AMSG_20180302</span>
##### <span class="badge badge-success">Available</span>
Adam Miller's Star-Galaxy Catalog, edition 2018/03/02

<hr/>

### <span class="badge badge-primary">AllWISE</span>
##### <span class="badge badge-success">Available</span>
AllWISE catalog.

<a href="https://irsa.ipac.caltech.edu/data/download/wise-allwise/" target="_blank">Original data and format description <i class="fa fa-external-link" aria-hidden="true"></i></a> 

<hr/>

### <span class="badge badge-primary">SDSS_DR14</span>
##### <span class="badge badge-danger">TODO</span>
SDSS Data Release 14

<a href="https://data.sdss.org/sas/dr14/casload/" target="_blank">SDSS-IV Science Archive Server (SAS) <i class="fa fa-external-link" aria-hidden="true"></i></a><br>
<a href="http://skyserver.sdss.org/dr14/en/tools/toolshome.aspx" target="_blank">Data Access Tools <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">Galex_GR6/7</span>
##### <span class="badge badge-danger">TODO</span>
GALEX GR6/7 Data Release

<a href="http://galex.stsci.edu/GR6/" target="_blank">Original data and format description <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">FERMI</span>
##### <span class="badge badge-danger">TODO</span>

<a href="https://fermi.gsfc.nasa.gov/ssc/data/access/lat/" target="_blank">Original data and format description <i class="fa fa-external-link" aria-hidden="true"></i></a>

<hr/>

### <span class="badge badge-primary">CRTS</span>
##### <span class="badge badge-danger">TODO</span>

<hr/>

### <span class="badge badge-primary">Swift</span>
##### <span class="badge badge-danger">TODO</span>

<hr/>

### <span class="badge badge-primary">ROSAT</span>
##### <span class="badge badge-danger">TODO</span>

<hr/>

### <span class="badge badge-primary">XMM</span>
##### <span class="badge badge-danger">TODO</span>

<hr/>

### <span class="badge badge-primary">Chandra CSC 2.0</span>
##### <span class="badge badge-danger">TODO</span>

<hr/>

### <span class="badge badge-primary">TGSS-NVSS spectral index maps and catalog</span>
##### <span class="badge badge-danger">TODO</span>

<hr/>

### <span class="badge badge-primary">Spitzer/GLIMPSE</span>
##### <span class="badge badge-danger">TODO</span>

<hr/>

### <span class="badge badge-primary">VPHas DR2+DR3</span>
##### <span class="badge badge-danger">TODO</span>
This is southern IPHas, but will overlap ZTF at l = 10-40 deg and l = 210-220

see http://www.vphasplus.org/data.shtml)

<hr/>

### <span class="badge badge-primary">ATLAS</span>
##### <span class="badge badge-danger">TODO</span>
First Catalog of Variable Stars

<a href="https://arxiv.org/pdf/1804.02132.pdf" target="_blank">Original data description <i class="fa fa-external-link" aria-hidden="true"></i></a>
