import re
import pandas as pd
import numpy as np
import os, sys, csv

from lib_py.distribution import *

sys.path.append(os.path.abspath("."))
from metatest.cross_file_test import Crosstest
    
export_data()
    
export_to_ddi()
