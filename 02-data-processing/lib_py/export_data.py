import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

def export_data(dataset, format, testscript):

    d1 = Dataset()

    if format == "tdp":
        d1.read_tdp(
            "02-data-processing/output/" + dataset + ".csv", 
            "02-data-processing/output/" + dataset + ".json"
        )
        
    elif format == "stata":
        d1.read_stata(
            "02-data-processing/output/" + dataset + ".dta"
        )
    
    else:
        print("[ERROR]: Wrong format: %s for %s" % (format, dataset))

    # Export test
    if testscript != "":
        sys.path.append('02-data-processing/test')
        import export_test

    d1.write_tdp(
        "02-temp/" + dataset + ".csv", 
        "02-temp/" + dataset + ".json"
    )
