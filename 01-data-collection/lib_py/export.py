import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

d1 = Dataset()

d1.read_tdp("01-data-collection/output/test.csv", "01-data-collection/output/test.json")

# test data
# d1.test()

d1.write_tdp("01-temp/test.csv", "01-temp/test.json")
