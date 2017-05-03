from .packages import *
from .config import config

# For-loop to read all dta
data_csv = dict()
data_json = dict()

for file in glob.glob(config["input_csv"]):
  data_csv[file] = pd.read_csv(
    file,
    # iterator=True,
    # convert_categoricals=False,
    )

for file in glob.glob(config["input_json"]):
  with open(file) as json_file:
    metadata = json_file.read()
  data_json[file] = json.loads(metadata)
