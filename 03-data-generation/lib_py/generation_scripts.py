import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

class Generations(Dataset):

    def __init__(self, dataset):
        self.dataset = dataset.dataset
        self.metadata = dataset.metadata
        
    def generate_bmi(self):
        self.dataset["bmi"] = self.dataset["body_weight"]/(self.dataset["body_height"]/100)/(self.dataset["body_height"]/100)

        del self.dataset["body_weight"]
        del self.dataset["body_height"]

        for x, y in enumerate(self.metadata["resources"][0]["schema"]["fields"]):
        
            if "body_weight" in y["name"] or "body_height" in y["name"]:
            
                del(self.metadata["resources"][0]["schema"]["fields"][x])
                
                if "body_weight" in self.metadata["resources"][0]["schema"]["fields"][x]["name"] or "body_height" in self.metadata["resources"][0]["schema"]["fields"][x]["name"]:
                    del(self.metadata["resources"][0]["schema"]["fields"][x])
        
        bmi = {"name": "bmi", "label": "BMI", "type": "number"}

        self.metadata["resources"][0]["schema"]["fields"].append(bmi)
