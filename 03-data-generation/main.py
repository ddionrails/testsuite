import re
import pandas as pd
import numpy as np
import os, sys, csv

from lib_py.generation import *

metadata = pd.read_csv("./metadata.csv", delimiter=",", header = 0)

for index, row in metadata.iterrows():
    
    import_data(
        dataset=row["dataset"],
        format=row["format"],
        testscript=row["testscript"]
    )
    
    process(
        dataset=row["dataset"],
        format=row["format"],
        generationscript=row["generationscript"],
        stats=row["stats"]
    )
    
    export_data(
        dataset=row["dataset"],
        testscript=row["testscript"]
    )
