#!/usr/bin/env python
"""
apt install libgdal-dev
"""
from setuptools import setup


req = ['gdal','nose','numpy','matplotlib',
       'basemap',]

print(req)

setup(name='groundwatertable',
      packages=['groundwatertable'],
      version = '0.1',
      description='Plotting of groundwater table using .shp shape files.',
      author = 'Michael Hirsch, Ph.D.',
      url = 'https://github.com/scienceopen/groundwatertable',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: GIS',
      'Programming Language :: Python :: 3.6',
      ],
      install_requires=req,
      dependency_links=['https://downloads.sourceforge.net/project/matplotlib/matplotlib-toolkits/basemap-1.0.7/basemap-1.0.7.tar.gz',],
	  )

