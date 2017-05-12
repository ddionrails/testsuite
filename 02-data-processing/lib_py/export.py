import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

d1 = Dataset()

d1.read_tdp("02-data-processing/output/test.csv", "02-data-processing/output/test.json")

# Export test
sys.path.append('02-data-processing/test')
import export_test

d1.write_tdp("02-temp/test.csv", "02-temp/test.json")
