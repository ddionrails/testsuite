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
        
    def splitlong(self):
        
        wave = ord("a")
        
        for year in sorted(list(set(self.dataset["wave"]))):
            
            temp = Dataset()
            temp.dataset = self.dataset.ix[self.dataset["wave"] == year]
            
            # TO DO: Metadaten anpassen!!!
            temp.metadata = self.metadata
            

            data_name = chr(wave) + re.search('(.*)(?!$)', temp.metadata["name"]).group(1)
            
            temp.write_tdp(
                "03-data-generation/output/" + data_name + ".csv",
                "03-data-generation/output/" + data_name + ".json"
            )
            
            wave = wave+1
