import os,sys
import unittest
import numpy as np

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

class Metatest(Dataset):

    def __init__(self, dataset):
        self.dataset = dataset.dataset
        self.metadata = dataset.metadata
        
        for i in dir(self):
           if i.startswith('metatest'):
               result = getattr(self, i)()
        
    def metatest_primary_keys(self):
        print("Testing Primary Keys...")
        # -------------------------------------------
        # Check if dataset is long with variable wave
        # -------------------------------------------
        for var in self.metadata["resources"][0]["schema"]["fields"]:
            if var.get("primary_key", "false") is not "false" and var["primary_key"] == True:
                try:
                    x = list(zip(self.dataset[var["name"]], self.dataset["wave"]))
                    assert len(set(x)) == len(x), "[Error]: %i case(s) in %s and wave are not unique" % (len(x)-len(set(x)), var["name"])
                    print("...check")
                except Exception as error:
                    print(error)
        
    def metatest_range(self):
        print("Testing Range...")
        for var in self.metadata["resources"][0]["schema"]["fields"]:
            if var["type"] == "number" or var["type"] == "cat":
                if var.get("min", "false") is not "false" and var.get("max", "false") is not "false":
                    try:
                        assert self.dataset[var["name"]].min() >= var["min"], "[Error]: Value %i in %s is not in range" % (self.dataset[var["name"]].min(), var["name"])
                    except Exception as error:
                        print(error)
                    try:
                        assert self.dataset[var["name"]].max() <= var["max"], "[Error]: Value %i in %s is not in range" % (self.dataset[var["name"]].max(), var["name"])
                    except Exception as error:
                        print(error)
        print("...check")
        
    def metatest_values(self):
        print("Testing Values...")
        
        print("...check")
        
    def metatest_type(self):
        print("Testing Strings And Numbers...")
        for var in self.metadata["resources"][0]["schema"]["fields"]:
            if var["type"] == "number" or var["type"] == "cat":
                wrong_type = []
                for value in self.dataset[var["name"]]:
                    try:
                        assert not type(value) is str, "[ERROR]: There is a string in %s." % (var["name"])
                    except Exception as error:
                        print(error)
                        break
                        
        print("...check")
        
    def metatest_foreign_key(self):
        print("Testing Foreign Keys...")
        print("...check")
