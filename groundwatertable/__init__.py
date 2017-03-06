#!/usr/bin/env python
from pathlib import Path
from matplotlib.pyplot import figure,show
from mpl_toolkits.basemap import Basemap
from osgeo import osr,gdal,ogr
from numpy import array,mgrid,mean
from numpy.ma import masked_where


def dumbwaterplot(datfn,shpfn,county):
    """
    not geographically registered, for where coordinate transform is not yet known
    """
    assert Path(datfn).is_file(),'{} not found'.format(datfn)
    ds = gdal.Open(datfn, gdal.GA_ReadOnly)

    wt = ds.ReadAsArray()
    nodata = ds.GetRasterBand(1).GetNoDataValue()
    wt = masked_where(wt==nodata,wt)

    xy = makegrid(ds)
#%% shape (points)
    assert Path(shpfn).is_file(),'{} not found'.format(shpfn)
    ps = ogr.Open(shpfn, gdal.GA_ReadOnly)
    layer = ps.GetLayer(0)

    #layerDefinition = daLayer.GetLayerDefn()
    #for i in range(layerDefinition.GetFieldCount()):
    #    print(layerDefinition.GetFieldDefn(i).GetName())
    xp=[]; yp=[]; name=[]
    for p in layer:
        if not p.GetField('COUNTY') == county:
            continue
        xp.append(p.GetField('X_COR'))
        yp.append(p.GetField('Y_COR'))
        name.append(p.GetField('NAME'))
#%%
    fg = figure()
    ax = fg.gca()
    hi = ax.pcolormesh(xy[0,:,:], xy[1,:,:], wt.T, cmap='gist_earth')
    fg.colorbar(hi,ax=ax).set_label('water table (feet)')
    ax.set_xlabel('meters east')
    ax.set_ylabel('meters north')

    # TODO origin not matching
#    for X,Y,N in zip(xp,yp,name):
#        ax.text(X,Y,N)



def waterplot(datfn,shpfn,county,mlat,mlon):

    ds = gdal.Open(datfn, gdal.GA_ReadOnly)

    wt = ds.ReadAsArray()

    m = Basemap(height=100e3,width=100e3,
                projection='omerc',
                lat_0=mean(mlat),lon_0=mean(mlon),
                lat_1=mlat[0],lon_1=mean(mlon),lat_2=mlat[1],lon_2=mean(mlon))

    xy = makegrid(ds)

    x,y = convertxy(xy,ds,m)
    m.pcolormesh(x,y,wt)

    # annotate
    m.drawcountries()
    m.drawcoastlines(linewidth=.5)

def makegrid(ds):
    gt = ds.GetGeoTransform()
    xres = gt[1]
    yres = gt[5]

    # get the edge coordinates and add half the resolution
    # to go to center coordinates
    xmin = gt[0] + xres * 0.5
    xmax = gt[0] + (xres * ds.RasterXSize) - xres * 0.5
    ymin = gt[3] + (yres * ds.RasterYSize) + yres * 0.5
    ymax = gt[3] - yres * 0.5

    xy = mgrid[xmin:xmax+xres:xres, ymax+yres:ymin:yres]

    return xy

def convertxy(xy,ds,m):
    # http://stackoverflow.com/questions/20488765/plot-gdal-raster-using-matplotlib-basemap

    proj = ds.GetProjection()

    inproj = osr.SpatialReference()
    inproj.ImportFromWkt(proj)
    outproj = osr.SpatialReference()
    outproj.ImportFromProj4(m.proj4string)

    shape = xy[0,:,:].shape
    size = xy[0,:,:].size

    # the ct object takes and returns pairs of x,y, not 2d grids
    # so the the grid needs to be reshaped (flattened) and back.
    ct = osr.CoordinateTransformation(inproj, outproj)
    xy_out = array(ct.TransformPoints(xy.reshape(2, size).T))

    x = xy_out[:,0].reshape(shape)
    y = xy_out[:,1].reshape(shape)

    return x, y

