import os,sys, shutil

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

shutil.copy2("03-temp/test.json", "04-data-distribution/data/test.json")
shutil.copy2("03-temp/test.csv", "04-data-distribution/data/test.csv")

# shutil.copy2("03-temp/test_stats.json", "04-data-distribution/statistics/test_stats.json")

shutil.copy2("03-temp/test_gen.json", "04-data-distribution/generations/test_gen.json")
shutil.copy2("03-temp/test_gen.csv", "04-data-distribution/generations/test_stats.csv")

# shutil.copy2("03-temp/test_gen_stats.json", "04-data-distribution/statistics/test_stats.json")
