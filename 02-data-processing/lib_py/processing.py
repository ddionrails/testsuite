import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset


def import_data(dataset, format, testscript):

    print("")
    print("[Data Processing]: Import Data (%s)" % dataset)

    d1 = Dataset()

    if format == "tdp":
        d1.read_tdp(
            "01-temp/" + dataset + ".csv", 
            "01-temp/" + dataset + ".json"
        )
        
    elif format == "stata":
        d1.read_stata(
            "01-temp/" + dataset + ".dta"
        )
    
    else:
        print("[ERROR]: Wrong format: %s for %s" % (format, dataset))

    # Export test
    if testscript != "":
        sys.path.append('02-data-processing/test')
        import import_test

    d1.write_tdp(
        "02-data-processing/input/" + dataset + ".csv", 
        "02-data-processing/input/" + dataset + ".json"
    )

    
def process(dataset, format, testscript):
    
    print("")
    print("[Data Processing]: Data Processing (%s)" % dataset)
    
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


def export_data(dataset, format, testscript):

    print("")
    print("[Data Processing]: Export Data (%s)" % dataset)

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

    
def main():
    pass  
    
if __name__ == "__main__":
    main()
    
    
