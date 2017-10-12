import os,sys
import json
import re
from collections import OrderedDict

sys.path.append(os.path.abspath("."))
from metatest.test import Metatest

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
    
    # Write primary keys and foreign keys in a file for crossfile tests
    try:
        with open("metatest/temp/keys.json") as json_data:
            keys = json.load(json_data)        
    except:
        keys = OrderedDict()
        keys["primary_keys"] = OrderedDict()
        keys["foreign_keys"] = OrderedDict()
        
    for var in d1.metadata["resources"][0]["schema"]["fields"]:
        
        if var.get("primary_key", "false") is not "false":
            values = [ int(i) for i in d1.dataset[var["name"]].unique() ]
            keys["primary_keys"][d1.metadata["name"]] = dict()
            keys["primary_keys"][d1.metadata["name"]][var["name"]] = dict(
                    values = values,
                )
        if var.get("foreign_key", "false") is not "false":
            values = [ int(i) for i in d1.dataset[var["name"]].unique() ]
            keys["foreign_keys"][d1.metadata["name"]] = dict()
            keys["foreign_keys"][d1.metadata["name"]][var["name"]] = dict(
                    target = re.search('(.*)\/', var["foreign_key"]).group(1),
                    primary_key = re.search('.*\/(.*)', var["foreign_key"]).group(1),
                    values = values,
                )
    with open("metatest/temp/keys.json", "w") as outfile:
            json.dump(keys, outfile, indent=2)

def main():
    pass  
    
if __name__ == "__main__":
    main()
