import os
import glob
import json
import yaml

file_names = [x for x in glob.glob("*") if x.endswith("yaml")]

for file_name in file_names:
    with open(file_name, "r") as f:
        content = f.read()
    data = yaml.safe_load(content)
    out_path = os.path.join("../instruments", file_name.replace(".yaml", ".json"))
    with open(out_path, "w+") as f:
        f.write(json.dumps(data))
