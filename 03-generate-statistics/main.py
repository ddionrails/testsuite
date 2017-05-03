import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

d1 = Dataset()

# get data from data-processing
d1.read_tdp("02-data-processing/output/test.csv", "02-data-processing/output/test.json")
'''
print(d1.dataset)
print(d1.metadata)
'''

# test data
# d1.test()

# write data in 03-generate-statistics/input/
d1.write_tdp("03-generate-statistics/input/test.csv", "03-generate-statistics/input/test.json")

# generate bmi
import generate_bmi

# test data
# d1.test()

# write data in 03-generate-statistics/output/
d1.write_tdp("03-generate-statistics/output/test.csv", "03-generate-statistics/output/test.json")
