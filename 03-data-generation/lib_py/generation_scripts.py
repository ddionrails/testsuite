import re, os,sys
import copy

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

sys.path.append(os.path.abspath("."))
from metatest.cross_file_test import Crosstest

class Generations(Dataset):

    def __init__(self, dataset):
        self.dataset = dataset.dataset
        self.metadata = dataset.metadata
        
    def generate_bmi(self):
        self.dataset["bmi"] = self.dataset["bodyweight"]/(self.dataset["bodyheight"]/100)/(self.dataset["bodyheight"]/100)

        del self.dataset["bodyheight"]
        
        self.metadata["resources"][0]["schema"]["fields"] = [ x for x in self.metadata["resources"][0]["schema"]["fields"] if x["name"] != "bodyheight" ]
        
        bmi = {"name": "bmi", "label": "BMI", "type": "number"}

        self.metadata["resources"][0]["schema"]["fields"].append(bmi)
        
    def splitlong(self, log, stats, split):
        
        wave = ord("a")
        
        for year in sorted(list(set(self.dataset["wave"]))):
            
            temp = Dataset()
            temp.dataset = self.dataset.ix[self.dataset["wave"] == year]
            
            temp.metadata = self.metadata.copy()          

            data_name = chr(wave) + re.search('(.*)(?!$)', temp.metadata["name"]).group(1)
            temp.metadata["name"] = data_name
            temp.metadata["conceptual_dataset"] = "net"
            temp.metadata["sub_type"] = "net"
            temp.metadata["resources"][0]["path"] = data_name + ".csv"
            
            var_path = temp.metadata["resources"][0]["schema"]["fields"]
            for var in var_path:
                try:
                    if var["foreign_key"] and wave == ord("a"):
                        foreign_origin = copy.deepcopy(var["foreign_key"])
                    var["foreign_key"] = chr(wave) + re.search('(.*)(.)(\/.*)', foreign_origin).group(1) + re.search('(.*)(.)(\/.*)', foreign_origin).group(3)
                except:
                    pass
            
            temp.write_tdp(
                "03-temp/" + data_name + ".csv",
                "03-temp/" + data_name + ".json"
            )
            
            if stats == "json":
                temp.write_stats(
                    "03-temp/" + data_name + "_stats.json", 
                    log=log, split=split
                )
            elif stats == "html":
                temp.write_stats(
                    "03-temp/" + data_name + "_stats.html", file_type="html", 
                    log=log, split=split
                )
            elif stats == "yaml":
                temp.write_stats(
                    "03-temp/" + data_name + "_stats.yaml", file_type="yaml", 
                    log=log, split=split
                )
            elif stats == "md":
                temp.write_stats(
                    "03-temp/" + data_name + "_stats.md", file_type="md", 
                    log=log, split=split
                )
            else:
                print("The format for statistics %s is not supported" % stats)
            
            Crosstest.preparation(temp)
            
            wave = wave+1
