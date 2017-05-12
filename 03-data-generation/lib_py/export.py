import os,sys, shutil

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

d1 = Dataset()

d1.read_tdp("03-data-generation/output/test.csv", "03-data-generation/output/test.json")

# Export test
sys.path.append('03-data-generation/test')
import export_test

d1.write_tdp("03-temp/test.csv", "03-temp/test.json")
# shutil.copy2("03-data-generation/output/test_stats.json", "03-temp/test_stats.json")

d1.read_tdp("03-data-generation/output/test_gen.csv", "03-data-generation/output/test_gen.json")

# Export test
sys.path.append('03-data-generation/test')
import export_test

d1.write_tdp("03-temp/test_gen.csv", "03-temp/test_gen.json")
# shutil.copy2("03-data-generation/output/test_gen_stats.json", "03-temp/test_gen_stats.json")
