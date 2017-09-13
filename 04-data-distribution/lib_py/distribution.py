import os,sys, shutil
import numpy as np
from os import listdir
import re

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

def export_data(dataset, testscript):

    print("")
    print("[Distributon]: Export Data (%s)" % dataset)

    d1 = Dataset()
    
    file_names = [f for f in listdir("03-temp/") if re.search("^" + dataset + "(\.|\_)", f)]
    
    
    for file_name in file_names:
        # t1 = Test(file_name)
        # t1.exporttest()
        # statistics, generations, data
        if "_stats" in file_name:
            print("Copy " + file_name + " in 04-data-distribution/statistics/")
            shutil.copy2(
                "03-data-generation/output/" + file_name, 
                "04-data-distribution/output/statistics/" + file_name
                )
        elif "_gen" in file_name:
            print("Copy " + file_name + " in 04-data-distribution/generations/")
            shutil.copy2(
                "03-data-generation/output/" + file_name, 
                "04-data-distribution/output/generations/" + file_name
                )
        else:
            print("Copy " + file_name + " in 04-data-distribution/data/")
            shutil.copy2(
                "03-data-generation/output/" + file_name, 
                "04-data-distribution/output/data/" + file_name
                )
