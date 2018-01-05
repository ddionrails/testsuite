import os,sys, shutil
import numpy as np
from os import listdir
import re
import logging

os.system("sh 04-data-distribution/setup.sh")

logging.basicConfig(filename="04-data-distribution/log/test.log", level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

def export_data():

    print("")
    print("[Distributon]: Export Data")
    
    file_names = [f for f in listdir("03-temp/")]
    
    for file_name in file_names:
        if "_stats" in file_name:
            print("Copy " + file_name + " in 04-data-distribution/statistics/")
            shutil.copy2(
                "03-temp/" + file_name, 
                "04-data-distribution/output/statistics/" + file_name
            )
        elif "_gen" in file_name:
            print("Copy " + file_name + " in 04-data-distribution/generations/")
            shutil.copy2(
                "03-temp/" + file_name, 
                "04-data-distribution/output/generations/" + file_name
            )
        else:
            print("Copy " + file_name + " in 04-data-distribution/data/")
            shutil.copy2(
                "03-temp/" + file_name, 
                "04-data-distribution/output/data/" + file_name
            )
                
def export_to_ddi():

    print("")
    print("[DDI Export]: Export Statistics from 04-data-distribution/output/statistics/ to ddionrails/datasets/")
    
    file_names = [f for f in listdir("04-data-distribution/output/statistics/")]
    
    for file_name in file_names:
        new_file_name = file_name.replace("_stats", "")
        print("Copy " + file_name + " in ddionrails/datasets/%s" % new_file_name)
        if file_name.endswith("json"):
            output_path = "ddionrails/datasets/"
        else:
            output_path = "graphite/"
        shutil.copy2(
        "04-data-distribution/output/statistics/" + file_name,
        output_path + new_file_name 
        )
