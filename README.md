Plex-EyeTV-Tools
================

A Plex Scanner for EyeTV libraries, allowing EyeTV recordings to be added to your Plex library.

It has been written for the EPG data available in the UK.

Installation
============

The package contains a standard Python `setup.py` script.

To create your own git clone and install the package, run the
following commands in Terminal.app:

    git clone git@github.com:steco/Plex-EyeTV-Tools.git
    cd Plex-EyeTV-Tools
    python setup.py install 

Developer documentation
=======================

All code resides in the bundle.  The scanners are thin API facades so
that Plex finds them, but the real code is in the bundle.
