import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

d1 = Dataset()

d1.read_tdp("01-temp/test.csv", "01-temp/test.json")
'''
print(d1.dataset)
print(d1.metadata)
'''

# Import test
sys.path.append('02-data-processing/test')
import import_test

d1.write_tdp("02-data-processing/input/test.csv", "02-data-processing/input/test.json")
