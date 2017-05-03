import os
os.system("./setup.sh")

# The environment loads all packages (pd, np), the config, and the data
from script.environment import *

d, m = read_tdp("input/test2.csv", "input/test2.json")
write_stats(d, m, "output/test2.json", vistest="output/vistest/")
write_stats(d, m, "output/test2.yaml", file_type="yaml")
