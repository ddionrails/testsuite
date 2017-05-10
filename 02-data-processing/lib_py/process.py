import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

d1 = Dataset()

d1.read_tdp("02-data-processing/input/test.csv", "02-data-processing/input/test.json")

# do something with the data
# ...

d1.write_tdp("02-data-processing/output/test.csv", "02-data-processing/output/test.json")
