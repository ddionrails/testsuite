import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

d1 = Dataset()

# get data from data-collection
d1.read_tdp("01-data-collection/output/test.csv", "01-data-collection/output/test.json")
'''
print(d1.dataset)
print(d1.metadata)
'''

# test raw data
# d1.test()

# write data in 02-data-processing/input/
d1.write_tdp("02-data-processing/input/test.csv", "02-data-processing/input/test.json")

# do something with the data
# ...

# test data
# d1.test()

# write data in 02-data-processing/output/
d1.write_tdp("02-data-processing/output/test.csv", "02-data-processing/output/test.json")
