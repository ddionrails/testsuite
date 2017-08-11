import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

def export_data(dataset, format, testscript):

    d1 = Dataset()

    if format == "tdp":
        d1.read_tdp(
            "01-data-collection/output/" + dataset + ".csv", 
            "01-data-collection/output/" + dataset + ".json"
        )
        
    elif format == "stata":
        d1.read_stata(
            "01-data-collection/output/" + dataset + ".dta"
        )
    
    else:
        print("[ERROR]: Wrong format: %s for %s" % (format, dataset))

    # Export test
    if testscript != "":
        sys.path.append('01-data-collection/test')
        import export_test

    d1.write_tdp(
        "01-temp/" + dataset + ".csv", 
        "01-temp/" + dataset + ".json"
    )
