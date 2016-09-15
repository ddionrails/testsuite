import os
os.system("./setup.sh")

# The environment loads all packages (pd, np), the config, and the data
from script.environment import *

convert.main(config, data_csv, data_json)
d, m = read_tdp("input/test2.csv", "input/test2.json")
write_stats(d, m, "output/test.json")
write_stats(d, m, "output/test.yaml", file_type="yaml")

