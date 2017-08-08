#!/usr/bin/env python
"""
apt install libgdal-dev
"""
req = ['nose','numpy','matplotlib','basemap',]
import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception as e:
    pip.main(['install'] + req)
# %%
from setuptools import setup

setup(name='groundwatertable',
      packages=['groundwatertable'],
      version = '0.1',
      description='Plotting of groundwater table using .shp shape files.',
      author = 'Michael Hirsch, Ph.D.',
      url = 'https://github.com/scivision/groundwatertable',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: GIS',
      'Programming Language :: Python :: 3.6',
      ],
      install_requires=req,
	  )

