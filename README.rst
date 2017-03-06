=======================
Ground Water Table Plot
=======================

Loads .SHP shape files and plots groundwater over them.

Install
=======
[reference](http://gis.stackexchange.com/a/74060)::

    apt install libgdal-dev
    export CPLUS_INCLUDE_PATH=/usr/include/gdal
    export C_INCLUDE_PATH=/usr/include/gdal
    
    python setup.py build_ext --include-dirs=/usr/include/gdal/
    python setup.py develop

If you have problems with missing ``/usr/include/gdal/cpl_vsi_error.h`` your ``libgdal-dev`` may be an old version.
The easiest fix may be to use your system's python3-gdal::

    sudo apt install python3-gdal python3-matplotlib python3-mpltoolkits.basemap python3-numpy


    /usr/bin/python3 PlotWatertable.py

