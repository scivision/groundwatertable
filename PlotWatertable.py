#!/usr/bin/env python
from matplotlib.pyplot import show
from groundwatertable import waterplot

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('datdir',help='directory to .adf file')
    p.add_argument('shpfn',help='.shp file to overlay, points and text')
    p = p.parse_args()

    waterplot(p.datdir, p.shpfn)

    show()
