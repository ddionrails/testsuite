import os,sys
import numpy as np
import json

class Crosstest():
    def __init__(self):
        for i in dir(self):
            if i.startswith('crosstest'):
                result = getattr(self, i)()
               
    def crosstest_01_foreign_key(self):
        print("Testing Foreign Keys...")
        with open("metatest/temp/keys.json") as json_data:
            keys = json.load(json_data)
        # Primary Key exists
        for dataset in keys["foreign_keys"]:
            for key in keys["foreign_keys"][dataset]:
                prim_key = keys["foreign_keys"][dataset][key]["primary_key"]
                prim_dataset = keys["foreign_keys"][dataset][key]["target"]
                prim_path = keys["primary_keys"][prim_dataset][prim_key]
                try:    
                    assert "values" in prim_path, "[Error]: "
                except Exception as error:
                    print(error)
        print("...check")
    # TO DO
    '''
    def crosstest_99_clean_temp(self):
        print("Clean metadata/temp/")
        os.system("sh metatest/clean_temp.sh")
    '''
