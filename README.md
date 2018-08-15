# Ground Water Table Plot

Loads `.SHP` shape files and plots groundwater over them.

## Install

The easiest way to get GDAL is from Anaconda/Miniconda Python:

    conda install gdal cartopy

    pip install -e .

## Usage

    ./PlotWatertable.py data/county/ data/county.shp

county/ is a folder containing `hdr.adf` and `w001w001.adf` if it's AIG
data.

[GDAL format reference](http://www.gdal.org/frmt_various.html)

## Notes

If you get error

> tensions/gdal_wrap.cpp:3168:10: fatal error: cpl_port.h: No such file or directory
>
>  #include "cpl_port.h"

or

> /usr/include/gdal/cpl_vsi_error.h

or

> extensions/gdal_array_wrap.cpp: In function 'void
> GDALRegister_NUMPY()': extensions/gdal_array_wrap.cpp:3528:45:
> error: 'GDALCreateDriver' was not declared in this scope poDriver =
> static_cast<GDALDriver*>(GDALCreateDriver());

your `libgdal-dev` may be an old version.

[reference](http://gis.stackexchange.com/a/74060):

    apt install gcc libgdal-dev

    CPLUS_INCLUDE_PATH=/usr/include/gdal C_INCLUDE_PATH=/usr/include/gdal python setup.py develop --include-dirs=/usr/include/gdal/

The easiest fix may be to use your system's `python3-gdal`:

    apt install python3-gdal python3-matplotlib python3-numpy


    /usr/bin/python3 PlotWatertable.py
