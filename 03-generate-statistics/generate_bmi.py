from __main__ import *

d1.dataset["bmi"] = d1.dataset["body_weight"]/(d1.dataset["body_height"]/100)/(d1.dataset["body_height"]/100)


del d1.dataset["body_weight"]
del d1.dataset["body_height"]


for x, y in enumerate(d1.metadata["resources"][0]["schema"]["fields"]):
    if "body_weight" in y["name"] or "body_height" in y["name"]:
        del(d1.metadata["resources"][0]["schema"]["fields"][x])
        if "body_weight" in d1.metadata["resources"][0]["schema"]["fields"][x]["name"] or "body_height" in d1.metadata["resources"][0]["schema"]["fields"][x]["name"]:
            del(d1.metadata["resources"][0]["schema"]["fields"][x])
        
bmi = {"name": "bmi", "label": "BMI", "type": "number"}
d1.metadata["resources"][0]["schema"]["fields"].append(bmi)
