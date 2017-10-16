import os,sys

sys.path.append(os.path.abspath("."))
from metatest.test import Metatest
from metatest.cross_file_test import Crosstest

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

def export_data(dataset, format, testscript):

    print("")
    print("[Data-Collection]: Export Data (%s)" % dataset)

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
    d2 = Metatest(d1)

    d1.write_tdp(
        "01-temp/" + dataset + ".csv", 
        "01-temp/" + dataset + ".json"
    )

    Crosstest.preparation(d1)

def main():
    pass  
    
if __name__ == "__main__":
    main()
