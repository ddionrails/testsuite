import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

d1 = Dataset()

d1.read_tdp("02-temp/test.csv", "02-temp/test.json")
'''
print(d1.dataset)
print(d1.metadata)
'''
# Import test
sys.path.append('03-data-generation/test')
import import_test
# d1.test("import_test.yaml")


d1.write_tdp("03-data-generation/input/test.csv", "03-data-generation/input/test.json")
