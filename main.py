import os,sys, yaml
os.system("./setup.sh")

sys.path.append(os.path.abspath("../../ddi.py"))
from ddi.dataset import Dataset

d1 = Dataset()
# d1.read_stata("input/test3.dta")
d1.read_tdp("input/test3.csv", "input/test3.json")
d1.write_stats("output/test3_stats.json", split="split", weight="weight")
d1.write_stats("output/test3_stats.html", file_type="html", split="split", weight="weight")
d1.write_tdp("output/test3.csv", "output/test3.json")
d1.write_stata("output/test3.do")
