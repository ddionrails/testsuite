import re, os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

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
        
    def splitlong(self, stats):
        
        wave = ord("a")
        
        for year in sorted(list(set(self.dataset["wave"]))):
            
            temp = Dataset()
            temp.dataset = self.dataset.ix[self.dataset["wave"] == year]
            
            temp.metadata = self.metadata.copy()          

            data_name = chr(wave) + re.search('(.*)(?!$)', temp.metadata["name"]).group(1)
            temp.metadata["name"] = data_name
            temp.metadata["resources"][0]["path"] = data_name + ".csv"
            
            temp.write_tdp(
                "03-temp/" + data_name + ".csv",
                "03-temp/" + data_name + ".json"
            )
            
            if stats == "json":
                temp.write_stats(
                    "03-temp/" + data_name + "_stats.json"
                )
            elif stats == "html":
                temp.write_stats(
                    "03-temp/" + data_name + "_stats.html", file_type="html"
                )
            elif stats == "yaml":
                temp.write_stats(
                    "03-temp/" + data_name + "_stats.yaml", file_type="yaml"
                )
            else:
                print("The format for statistics %s is not supported" % stats)
            
            wave = wave+1
