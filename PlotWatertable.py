#!/usr/bin/env python
from matplotlib.pyplot import show
from groundwatertable import waterplot
from argparse import ArgumentParser


def main():
    p = ArgumentParser()
    p.add_argument('datdir', help='directory to .adf file')
    p.add_argument('shpfn', help='.shp file to overlay, points and text')
    p = p.parse_args()

    waterplot(p.datdir, p.shpfn)

    show()


if __name__ == '__main__':
    main()
