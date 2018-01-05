#!/usr/bin/env python
"""
conda install gdal cartopy
"""
install_requires = ['numpy','cartopy','gdal']
tests_require=['nose','coveralls']

# %%
from setuptools import setup, find_packages

setup(name='groundwatertable',
      packages=find_packages(),
      version = '0.1.0',
      description='Plotting of groundwater table using .shp shape files.',
      author = 'Michael Hirsch, Ph.D.',
      url = 'https://github.com/scivision/groundwatertable',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: GIS',
      'Programming Language :: Python :: 3',
      ],
      install_requires=install_requires,
      extras_require={'plot':['matplotlib'],
                      'tests':tests_require,},
      tests_require=tests_require,
      python_requires='>=3.5',
	  )

