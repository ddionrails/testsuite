import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

d1 = Dataset()

d1.read_tdp("01-data-collection/output/test.csv", "01-data-collection/output/test.json")

# Export test
sys.path.append('01-data-collection/test')
import export_test

d1.write_tdp("01-temp/test.csv", "01-temp/test.json")
