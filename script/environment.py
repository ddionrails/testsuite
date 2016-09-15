from .packages import *
from .config import config

sys.path.append(os.path.abspath("../ddi.py"))

from ddi.statistics import convert
from ddi.convert.read_tdp import read_tdp
from ddi.convert.write_stats import write_stats

# Import data and scipts
from .importData import data_csv
from .importData import data_json
