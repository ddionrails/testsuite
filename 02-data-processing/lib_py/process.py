import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

def process(dataset, format, testscript):

    d1 = Dataset()

    if format == "tdp":
        d1.read_tdp(
            "02-data-processing/input/" + dataset + ".csv", 
            "02-data-processing/input/" + dataset + ".json"
        )
        
    elif format == "stata":
        d1.read_stata(
            "02-data-processing/input/" + dataset + ".dta"
        )
    
    else:
        print("[ERROR]: Wrong format: %s for %s" % (format, dataset))



    # do something with the data
    # ...


    d1.write_tdp(
        "02-data-processing/output/" + dataset + ".csv", 
        "02-data-processing/output/" + dataset + ".json"
    )
