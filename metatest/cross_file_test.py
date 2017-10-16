import os,sys
import numpy as np
import json
import re
from collections import OrderedDict

class Crosstest():

    @classmethod
    def run(cls):
        for i in dir(cls):
            if i.startswith('crosstest'):
                result = getattr(cls, i)()
               
    @classmethod
    def crosstest_01_foreign_key(cls):
        print("Testing Foreign Keys...")
        with open("metatest/temp/keys.json") as json_data:
            keys = json.load(json_data)
        # Primary Key exists
        for dataset in keys["foreign_keys"]:
            for key in keys["foreign_keys"][dataset]:
                foreign_key = keys["foreign_keys"][dataset][key]["primary_key"]
                foreign_dataset = keys["foreign_keys"][dataset][key]["target"]
                try:
                    assert foreign_dataset in keys["primary_keys"],\
                        "[ERROR]: The dataset %s doesn't exist." % foreign_dataset 
                    assert foreign_key in keys["primary_keys"][foreign_dataset],\
                        "[ERROR]: The primary key %s in %s doesn't exist." % (
                            foreign_key, foreign_dataset
                         )   
                except Exception as error:
                    print(error)
        
        print("...check")
    
    @classmethod
    def crosstest_99_clean_temp(cls):
        print("Clean metadata/temp/")
        os.system("sh metatest/clean_temp.sh")

    @classmethod
    def preparation(cls, dataset):
        # Write primary keys and foreign keys in a file for crossfile tests
        try:
            with open("metatest/temp/keys.json") as json_data:
                keys = json.load(json_data)        
        except:
            keys = OrderedDict()
            keys["primary_keys"] = OrderedDict()
            keys["foreign_keys"] = OrderedDict()
        
        for var in dataset.metadata["resources"][0]["schema"]["fields"]:
        
            if var.get("primary_key", "false") is not "false":
                values = [ int(i) for i in dataset.dataset[var["name"]].unique() ]
                keys["primary_keys"][dataset.metadata["name"]] = dict()
                keys["primary_keys"][dataset.metadata["name"]][var["name"]] = dict(
                    values = values,
                )
            if var.get("foreign_key", "false") is not "false":
                values = [ int(i) for i in dataset.dataset[var["name"]].unique() ]
                keys["foreign_keys"][dataset.metadata["name"]] = dict()
                keys["foreign_keys"][dataset.metadata["name"]][var["name"]] = dict(
                    target = re.search('(.*)\/', var["foreign_key"]).group(1),
                    primary_key = re.search('.*\/(.*)', var["foreign_key"]).group(1),
                    values = values,
                )
        with open("metatest/temp/keys.json", "w") as outfile:
            json.dump(keys, outfile, indent=2)

