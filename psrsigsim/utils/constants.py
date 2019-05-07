"""constants.py
A place to keep various constants needed for pulsar signals.
"""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import numpy as np
import scipy as sp
from astropy import units as u
from astropy import constants as c
from .utils import make_quant

#constant used to be more consistent with PSRCHIVE
DM_K =  make_quant(1.0/2.41e-4, 'MHz^-2 pc cm^-3 s^-1')