import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

temp = []
dir_data = "01-data-collection/output/"
for file in os.listdir(dir_data):
    temp.append(os.path.splitext(file)[0])
files = set(temp)

for data in files:
    d1 = Dataset()
    try:
        d1.read_tdp(dir_data + data + ".csv", dir_data + data + ".json")
    except:
        try:
            d1.read_stata(dir_data + data + ".dta")
        except:
            print("Can't find a match for " + data + " as tdp ot stata dataset")
            continue
        
