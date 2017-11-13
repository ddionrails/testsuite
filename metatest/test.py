import os,sys
import numpy as np
import logging

logging.basicConfig(filename="metatest/log/test.log", level=logging.WARNING)
logger = logging.getLogger(__name__)

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
        logger.info("Testing Primary Keys...")
        # -------------------------------------------
        # Check if dataset is long with variable wave
        # -------------------------------------------
        for var in self.metadata["resources"][0]["schema"]["fields"]:
            if var.get("primary_key", "false") is not "false" and var["primary_key"] == True:
                try:
                    x = list(zip(self.dataset[var["name"]], self.dataset["wave"]))
                    assert len(set(x)) == len(x), "[Error]: %i case(s) in %s and wave are not unique" % (len(x)-len(set(x)), var["name"])
                    logger.info("...check")
                except Exception as error:
                    logger.warning("{}: {}".format(self.metadata["name"], error))
        
    def metatest_range(self):
        logger.info("Testing Range...")
        for var in self.metadata["resources"][0]["schema"]["fields"]:
            if var["type"] == "number" or var["type"] == "cat":
                if var.get("min", "false") is not "false" and var.get("max", "false") is not "false":
                    try:
                        assert self.dataset[var["name"]].min() >= var["min"], "[Error]: Value %i in %s is not in range" % (self.dataset[var["name"]].min(), var["name"])
                    except Exception as error:
                        logger.warning("{}: {}".format(self.metadata["name"], error))
                    try:
                        assert self.dataset[var["name"]].max() <= var["max"], "[Error]: Value %i in %s is not in range" % (self.dataset[var["name"]].max(), var["name"])
                    except Exception as error:
                        logger.warning("{}: {}".format(self.metadata["name"], error))
        logger.info("...check")
        
    def metatest_values(self):
        logger.info("Testing Values...")
        for var in self.metadata["resources"][0]["schema"]["fields"]:
            if var["type"] == "cat":
                for val in var["values"]:
                    if val["value"] == var["min"]:
                        try:
                            assert val["label"] != "", "[Error]: The value %i of variable %s has not a label" % (var["min"], var["name"])
                        except Exception as error:
                            logger.warning("{}: {}".format(self.metadata["name"], error))
                    if val["value"] == var["max"]:
                        try:
                            assert val["label"] != "", "[Error]: The value %i of variable %s has not a label" % (var["max"], var["name"])
                        except Exception as error:
                            logger.warning("{}: {}".format(self.metadata["name"], error))
        logger.info("...check")
        
    def metatest_type(self):
        logger.info("Testing Strings And Numbers...")
        for var in self.metadata["resources"][0]["schema"]["fields"]:
            if var["type"] == "number" or var["type"] == "cat":
                wrong_type = []
                for value in self.dataset[var["name"]]:
                    try:
                        assert not type(value) is str, "[ERROR]: There is a string in %s." % (var["name"])
                    except Exception as error:
                        logger.warning("{}: {}".format(self.metadata["name"], error))
                        break
                        
        logger.info("...check")
