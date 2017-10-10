import re
import pandas as pd
import numpy as np
import os, sys, csv

from lib_py.collection import *

sys.path.append(os.path.abspath("."))
from metatest.cross_file_test import Crosstest

metadata = pd.read_csv("./metadata.csv", delimiter=",", header = 0)

for index, row in metadata.iterrows():
    
    export_data(
        dataset=row["dataset"],
        format=row["format"],
        testscript=row["testscript"]
    )
    
Crosstest()
    
