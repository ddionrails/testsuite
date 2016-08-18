from .packages import *
from .config import config

def get_names (name):
    # get name without path
    data_name = basename(name)
    # get folder name in output
    data_folder = re.sub(".csv", "/", data_name)
    return data_name, data_folder

def save_yaml(data_yaml, data_folder, format, stat, config):
    """
    Save YAML to file.
    """
    print("write \"" + data_yaml + "\" in \"output/" + data_folder + "\"")
    with open("".join((config["output"], data_folder, format, data_yaml)), "w") as yaml_file:
      yaml_file.write(yaml.dump(stat, default_flow_style=False))

def save_json(data_json, data_folder, format, stat, config):

    print("write \"" + data_json + "\" in \"output/" + data_folder + "\"")
    with open("".join((config["output"], data_folder, format, data_json)), "w") as json_file:
      json_file.write(json.dumps(stat, data_json))

def vistest(stat, dataset_name, var_name, config):
    vistest_name = "".join((dataset_name, "_", var_name, ".json"))
    print("write \"" + vistest_name + "\" in \"vistest/output/\"")
    with open("".join((config["vistest"], vistest_name)), "w") as json_file:
      json_file.write(json.dumps(stat, vistest_name))

def parse_dataset(name, file_csv, file_json, config):

    data_name, data_folder = get_names(name)

    print("create folder \"output/" + data_folder + "\"")
    os.mkdir("".join((config["output"], data_folder)))

    stat = generate_stat(data_name, file_csv, file_json, config)

    format = "statistics_"
    
    # yaml name
    data_yaml = re.sub(".csv", ".yaml", data_name) 
    save_yaml(data_yaml, data_folder, format, stat, config)

    # json name
    data_json = re.sub(".csv", ".json", data_name) 
    save_json(data_json, data_folder, format, stat, config)

def uni(elem, scale, file_csv, file_json):

    statistics = {}
 
    #create df without missings    
    df_nomis = file_csv[elem["name"]].copy()

    for index, value in enumerate(df_nomis):
        if isinstance(value, str)==False and value < 0: 
            df_nomis[index] = np.nan

    #create df with only missings
    df_mis = file_csv[elem["name"]].copy()
 
    for index, value in enumerate(df_mis):
        if isinstance(value, str)==False and value >= 0:
            df_mis[index] = np.nan

    # min and max
    try:
        min = int(df_nomis.min())
        max = int(df_nomis.max())
    except:
        pass

    # missings
    missing_count = df_mis.value_counts() 
    missing_index = [0,1,2]
    missing_value = [-3,-2,-1]
    missing_label = ["nicht valide", "trifft nicht zu", "keine Angabe"]
   
    if elem["type"] == "cat":
        
        frequencies = []
        weighted = []
        values = []
        missings = []
        labels = []
            
        for index in missing_index:
            try:
                frequencies.append(int(missing_count[missing_value[index]]))
            except:
                frequencies.append(0)
            labels.append(missing_label[index])
            missings.append("true")  
            values.append(missing_value[index])

        # loop for value codes
        value_count = df_nomis.value_counts()
        for index, value in enumerate(elem["values"]):
            try:
                frequencies.append(int(value_count[value["value"]]))
            except:
                frequencies.append(0)
            labels.append(value["label"])
            missings.append("false") 
            values.append(value["value"]) 

        # weighted placeholder
        weighted = frequencies[:]

        statistics.update(
            dict(
                frequencies = frequencies,
                weighted = weighted,
                values = values,
                missings = missings,
                labels = labels,
            )
        )

    elif elem["type"] == "string":

        frequencies = []
        missings = []

        len_unique = len(df_nomis.unique())
        len_missing = 0
        for i in df_nomis.unique():
            if "-1" in str(i):
                len_unique-=1
                len_missing+=1
            elif "-2" in str(i):
                len_unique-=1
                len_missing+=1
            elif "-3" in str(i):
                len_unique-=1
                len_missing+=1
            elif "nan" in str(i):
                len_unique-=1
                len_missing+=1
        frequencies.append(len_unique)
        missings.append(len_missing)

        statistics.update(
            dict(
                frequencies = frequencies,
                missings = missings, #includes system missings
            )
        )

    elif elem["type"] == "number": 
        #missings        
        missings = dict()
        missings["frequencies"] = []
        missings["weighted"] = []
        missings["labels"] = []
        missings["values"] = []
            
        density = []
        total = []
        valid = []
        missing = []
        weighted = []

        for index in missing_index:
            try:
                missings["frequencies"].append(int(missing_count[missing_value[index]]))
            except:
                missings["frequencies"].append(0)
            missings["labels"].append(missing_label[index])  
            missings["values"].append(missing_value[index])

        # weighted placeholder
        missings["weighted"] = missings["frequencies"][:]

        # density and weighted (placeholder)
        if max - min > 0:
            by = (max-min)/5
            x = min
            while(x < max):
                count = 0
                y = x + by
                
                for index, value in enumerate(df_nomis):
                    if value >= x and value < y:
                        count += 1
                    elif round(y) == max and value == max:
                        count += 1
                x = y
                
                density.append(count)
                weighted.append(count)

        else:
            by = 0
            count = 0
            for index, value in enumerate(df_nomis):
                if value >= 0:
                    count += 1
                    density.append(count)
                    weighted.append(count)
        
        # total and valid
        total = int(file_csv[elem["name"]].size)
        valid = total - int(file_csv[elem["name"]].isnull().sum())

        statistics.update(
            dict(
                density = density,
                weighted = weighted,
                min = min,
                max = max,
                by = by,
                total = total,
                valid = valid,
                missing = missing,
                missings = missings,
            )
        )


    return statistics


def generate_stat(data_name, file_csv, file_json, config):
    dataset_name = re.sub(".csv", "", data_name)
      
  
    stat = []
    for i, elem in enumerate(file_json["resources"][0]["schema"]["fields"]):
        scale = elem["type"][0:3]
        var_name = elem["name"]
        stat.append(
            dict(
                study = "testsuite",
                dataset = dataset_name,
                variable = elem["name"],
                label = elem["label"],
                scale = scale,
                uni = uni(elem, scale, file_csv, file_json),
            )
        )
        # Test for Visualization
        vistest(stat[-1], dataset_name, var_name, config)

    return stat

def main(config, data_csv, data_json):
    for name, data in data_csv.items():
        path_json = re.sub(".csv", ".json", name)
        file_json = data_json[path_json]
        file_csv = data
        parse_dataset(name, file_csv, file_json, config)
