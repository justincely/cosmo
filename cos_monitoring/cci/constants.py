from __future__ import absolute_import
"""Constants for monitor.py
"""

__author__ = 'Justin Ely'
__maintainer__ = 'Justin Ely'
__email__ = 'ely@stsci.edu'
__status__ = 'Active'

__all__ = ['X_UNBINNED',
           'Y_UNBINNED',
           'X_BINNING',
           'Y_BINNING',
           'XLEN',
           'YLEN',
           'X_VALID',
           'Y_VALID',
           'CCI_DIR',
           'MONITOR_DIR',
           'TEST_DIR',
           'WEBPAGE_DIR',
           'FUVA_string',
           'FUVB_string',
           'MODAL_GAIN_LIMIT',
           'TIMESTAMP']

import os
import time
from datetime import datetime
import glob
from astropy.io import fits
import numpy as np
import yaml

X_UNBINNED = 16384
Y_UNBINNED = 1024

X_BINNING = 8  # These values are believed to be optimal based on the
Y_BINNING = 2  # pore spacing of the detector

XLEN = X_UNBINNED // X_BINNING
YLEN = Y_UNBINNED // Y_BINNING

X_VALID = (0 // X_BINNING, 16384 // X_BINNING)
Y_VALID = (0 // Y_BINNING, 1024 // Y_BINNING)

#----Directory and File Constants
CCI_DIR = '/smov/cos/Data/CCI/' ## OPUS
#CCI_DIR = '/grp/hst/cos/Data/CumulativeImage/latest/CCI/' ## Dave


MONITOR_DIR = '/grp/hst/cos/Monitors/CCI/'
#MONITOR_DIR = '/grp/hst/cos/Monitors/CCI_DAVE/'
TEST_DIR = os.path.join( MONITOR_DIR, 'test_suite')
WEBPAGE_DIR = '/grp/webpages/COS/cci/'

FUVA_string = '_00_'
FUVB_string = '_01_'

MODAL_GAIN_LIMIT = 3

date_time = str(datetime.now())
TIMESTAMP = (date_time.split()[0]+'T'+date_time.split()[1] ).replace(':','-')
