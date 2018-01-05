 #!/usr/bin/env python
from matplotlib.pyplot import figure
import cartopy
from osgeo import osr,gdal


def waterplot(datfn,shpfn):#,mlat,mlon):
    """
    example;
    https://ocefpaf.github.io/python4oceanographers/blog/2015/03/02/geotiff/
    """

    ds = gdal.Open(datfn, gdal.GA_ReadOnly)
    if ds is None:
        raise OSError(f'could not read {datfn}')

    wt = ds.ReadAsArray() # numpy ndarray

    gt = ds.GetGeoTransform()
    proj = ds.GetProjection()

    inproj = osr.SpatialReference()
    inproj.ImportFromWkt(proj)

#    projcs = inproj.GetAuthorityCode('PROJCS')
#    projcs = inproj.GetAuthorityCode('LOCAL_CS')

    ax = figure().gca(projection=cartopy.crs.Mercator())
    ax.imshow(wt,origin='lower')




