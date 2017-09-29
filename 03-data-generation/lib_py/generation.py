import os,sys, shutil
import numpy as np
from os import listdir
import re

sys.path.append(os.path.abspath("."))
from metatest.test import Metatest

from lib_py.generation_scripts import Generations

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

def import_data(dataset, format, testscript):
    
    print("")
    print("[Generation]: Import Data (%s)" % dataset)

    d1 = Dataset()

    if format == "tdp":
        d1.read_tdp(
            "02-temp/" + dataset + ".csv", 
            "02-temp/" + dataset + ".json"
        )
        
    elif format == "stata":
        d1.read_stata(
            "02-temp/" + dataset + ".dta"
        )
    
    else:
        print("[ERROR]: Wrong format: %s for %s" % (format, dataset))

    d1.write_tdp(
        "03-data-generation/input/" + dataset + ".csv", 
        "03-data-generation/input/" + dataset + ".json"
    )
    

def process(dataset, format, generationscript, splitlong, stats):

    print("")
    print("[Generation]: Data Processing (%s)" % dataset)

    d1 = Dataset()

    if format == "tdp":
        d1.read_tdp(
            "03-data-generation/input/" + dataset + ".csv", 
            "03-data-generation/input/" + dataset + ".json"
        )
        
    elif format == "stata":
        d1.read_stata(
            "03-data-generation/input/" + dataset + ".dta"
        )
    
    else:
        print("[ERROR]: Wrong format: %s for %s" % (format, dataset))
    
    d2 = Metatest(d1)
    d1.write_tdp(
        "03-data-generation/output/" + dataset + ".csv", 
        "03-data-generation/output/" + dataset + ".json"
    )

    #statistics before generations
    if stats == "json":
        d1.write_stats(
            "03-data-generation/output/" + dataset + "_stats.json"
        )
    elif stats == "html":
        d1.write_stats(
            "03-data-generation/output/" + dataset + "_stats.html", file_type="html"
        )
    elif stats == "yaml":
        d1.write_stats(
            "03-data-generation/output/" + dataset + "_stats.yaml", file_type="yaml"
        )
    else:
        print("The format for statistics %s is not supported" % stats)

    # split long dataset
    if splitlong == 1:
        d2 = Generations(d1)
        d2.splitlong()

    # generations
    if isinstance(generationscript, str):
        
        d2 = Generations(d1)
        
        try:
            eval("d2." + generationscript + "()")
        except:
            print("[Error]: The generationscript %s doesn't exist" % generationscript)
        
        d2 = Metatest(d1)
        d1.write_tdp(
            "03-data-generation/output/" + dataset + "_gen.csv", 
            "03-data-generation/output/" + dataset + "_gen.json"
        )
        
        #statistics after generations
        if stats == "json":
            d1.write_stats(
                "03-data-generation/output/" + dataset + "_gen_stats.json"
            )
        elif stats == "html":
            d1.write_stats(
                "03-data-generation/output/" + dataset + "_gen_stats.html", file_type="html"
            )
        elif stats == "yaml":
            d1.write_stats(
                "03-data-generation/output/" + dataset + "_gen_stats.yaml", file_type="yaml"
            )
        else:
            print("The format for statistics %s is not supported" % stats)
            
      
def export_data(dataset, testscript):

    print("")
    print("[Generation]: Export Data (%s)" % dataset)

    file_names = [f for f in listdir("03-data-generation/output/") if re.search("^" + dataset + "(\.|\_)", f)]
    
    
    for file_name in file_names:
        print("Copy " + file_name + " in 03-temp/")
        shutil.copy2("03-data-generation/output/" + file_name, "03-temp/" + file_name)
        

