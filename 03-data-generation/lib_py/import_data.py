import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

def import_data(dataset, format, testscript):

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

    # Export test
    if testscript != "":
        sys.path.append('03-data-generation/test')
        import import_test

    d1.write_tdp(
        "03-data-generation/input/" + dataset + ".csv", 
        "03-data-generation/input/" + dataset + ".json"
    )
