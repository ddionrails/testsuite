import re
import pandas as pd
import numpy as np
import os, sys, csv

from lib_py.export import export

metadata = pd.read_csv("./metadata.csv", delimiter=",", header = 0)

for index, row in metadata.iterrows():
    
    export(
        dataset=row["dataset"],
        format=row["format"],
        testscript=row["testscript"]
    )
