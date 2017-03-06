#!/usr/bin/env python
from groundwatertable import waterplot

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('datfn',help='binary (or ASCII) .adf raster file')
    p.add_argument('shpfn',help='.shp file to overlay, points and text')
    p.add_argument('county',help='county/parish to plot')
    p.add_argument('mlat',help='lat limits',nargs='+',type=float)
    p.add_argument('mlon',help='lon limits',nargs='+',type=float)
    p = p.parse_args()

    #dumbwaterplot(p.datfn,p.shpfn,p.county)

    waterplot(p.datfn,p.shpfn,p.county,p.mlat,p.mlon)

    show()
