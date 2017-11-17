import os,sys, shutil
import numpy as np
from os import listdir
import re
import math

sys.path.append(os.path.abspath("."))
from metatest.test import Metatest
from metatest.cross_file_test import Crosstest

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
    

def process(dataset, format, generationscript, splitlong, stats, split):

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
    
    ################### Error Log ###################
    log_file = "metatest/log/test.log"
    with open(log_file) as l:
        log_temp = l.readlines()
    log = dict()
    for line in log_temp:
        matchObj = re.search( r'(WARNING:metatest.test:)(..)(: \[Error\]: )(.*)', line)
        if matchObj:
            try:
                log[matchObj.group(2)] = matchObj.group(4)
            except:
                pass
        else:
            print("No match!!")
    #################################################
    
    d1.write_tdp(
        "03-data-generation/output/" + dataset + ".csv", 
        "03-data-generation/output/" + dataset + ".json"
    )
    
    d1.write_stata(
        "03-data-generation/output/" + dataset + ".do"
    )

    #statistics before generations
    if stats == "json":
        d1.write_stats(
            "03-data-generation/output/" + dataset + "_stats.json", 
            log=log, split=split
        )
    elif stats == "html":
        d1.write_stats(
            "03-data-generation/output/" + dataset + "_stats.html", file_type="html", 
            log=log, split=split
        )
    elif stats == "yaml":
        d1.write_stats(
            "03-data-generation/output/" + dataset + "_stats.yaml", file_type="yaml", 
            log=log, split=split
        )
    elif stats == "md":
        d1.write_stats(
            "03-data-generation/output/" + dataset + "_stats.md", file_type="md", 
            log=log, split=split
        )    
    else:
        print("The format for statistics %s is not supported" % stats)

    Crosstest.preparation(d1)

    # split long dataset
    if splitlong == 1:
        print("Export the data in wide format")
        d2 = Generations(d1)
        d2.splitlong(log, stats, split)
        

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
        d1.write_stata(
            "03-data-generation/output/" + dataset + "_gen.do"
        )
        
        #statistics after generations
        if stats == "json":
            d1.write_stats(
                "03-data-generation/output/" + dataset + "_gen_stats.json", 
                log=log, split=split
            )
        elif stats == "html":
            d1.write_stats(
                "03-data-generation/output/" + dataset + "_gen_stats.html",
                file_type="html", 
                log=log, split=split
            )
        elif stats == "yaml":
            d1.write_stats(
                "03-data-generation/output/" + dataset + "_gen_stats.yaml", 
                file_type="yaml", 
                log=log, split=split
            )
        elif stats == "md":
            d1.write_stats(
                "03-data-generation/output/" + dataset + "_gen_stats.md", 
                file_type="md", 
                log=log, split=split
            )
        else:
            print("The format for statistics %s is not supported" % stats)
      
        Crosstest.preparation(d1)      
      
def export_data(dataset, testscript):

    print("")
    print("[Generation]: Export Data (%s)" % dataset)

    file_names = [f for f in listdir("03-data-generation/output/") if re.search("^" + dataset + "(\.|\_)", f)]
    
    
    for file_name in file_names:
        print("Copy " + file_name + " in 03-temp/")
        shutil.copy2("03-data-generation/output/" + file_name, "03-temp/" + file_name)
        

