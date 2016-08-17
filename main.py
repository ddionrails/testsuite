import os
os.system("./setup.sh")

# The environment loads all packages (pd, np), the config, and the data
from script.environment import *

convert.main(config, data_csv, data_json)
