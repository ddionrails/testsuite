import os,sys

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

d1 = Dataset()

d1.read_tdp("03-data-generation/input/test.csv", "03-data-generation/input/test.json")


d1.write_tdp("03-data-generation/output/test.csv", "03-data-generation/output/test.json")

# generate statistics
d1.write_stats("03-data-generation/output/test_stats.json")

# generate bmi
import generate_bmi

d1.write_tdp("03-data-generation/output/test_gen.csv", "03-data-generation/output/test_gen.json")

# generate statistics
d1.write_stats("03-data-generation/output/test_gen_stats.json")
