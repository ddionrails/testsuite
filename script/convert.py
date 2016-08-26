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

def get_missing_codes():
    missing_index = [0,1,2]
    missing_value = [-3,-2,-1]
    missing_label = ["nicht valide", "trifft nicht zu", "keine Angabe"]

    return missing_index, missing_value, missing_label

def get_dataframes(elem, file_csv):
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

    return df_nomis, df_mis

def uni_cat(elem, file_csv):
    df_nomis, df_mis = get_dataframes(elem, file_csv)
    
    # missings
    missing_index, missing_value, missing_label = get_missing_codes()
    missing_count = df_mis.value_counts() 

    frequencies = []
    weighted = []
    values = []
    missings = []
    labels = []
     
    # weighted frequencies
    f_w = file_csv.pivot_table(index=elem["name"], values="weight", aggfunc=np.sum)
       
    for index in missing_index:
        try:
            frequencies.append(int(missing_count[missing_value[index]]))
            weighted.append(int(f_w[missing_value[index]]))
        except:
            frequencies.append(0)
            weighted.append(0)
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
        try:
            weighted.append(int(f_w[value["value"]]))
        except:
            weighted.append(0)
        labels.append(value["label"])
        missings.append("false") 
        values.append(value["value"]) 

    cat_dict = dict(
        frequencies = frequencies,
        weighted = weighted,
        values = values,
        missings = missings,
        labels = labels,
        )

    return cat_dict

def uni_string(elem, file_csv):
    df_nomis, df_mis = get_dataframes(elem, file_csv)

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


    string_dict = dict(
        frequencies = frequencies,
        missings = missings, #includes system missings
        )

    return string_dict

def uni_number(elem, file_csv):
    df_nomis, df_mis = get_dataframes(elem, file_csv)

    # missings
    missing_index, missing_value, missing_label = get_missing_codes()
    missing_count = df_mis.value_counts()

    #missings        
    missings = dict(
        frequencies=[],
        weighted=[],
        labels=[],
        values=[],
    )
            
    density = []
    total = []
    valid = []
    missing = []
    weighted = []

    # min and max
    try:
        min = int(df_nomis.min())
        max = int(df_nomis.max())
    except:
        pass

    # weighted missings
    if elem["name"] != "weight":
        f_w = file_csv.pivot_table(index=elem["name"], values="weight", aggfunc=np.sum)

    for index in missing_index:
        try:
            missings["frequencies"].append(int(missing_count[missing_value[index]]))
        except:
            missings["frequencies"].append(0)
        try:
            missings["weighted"].append(int(f_w[missing_value[index]]))
        except:
            missings["weighted"].append(0)
        missings["labels"].append(missing_label[index])  
        missings["values"].append(missing_value[index])
    missing.append(sum(missings["frequencies"]))

    if elem["name"] == "weight":
        missings["weighted"] = missings["frequencies"][:]

    # density (placeholder)
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

    else:
        by = 0
        count = 0
        for index, value in enumerate(df_nomis):
            if value >= 0:
                count += 1
                density.append(count)

    # weighted placeholder
    weighted = density[:]
    
    # tranform to percentage
    '''
    x = sum(density)
    for i, c in enumerate(density):
        density[i] = density[i]/x
    '''
       
    # total and valid
    total = int(file_csv[elem["name"]].size)
    valid = total - int(file_csv[elem["name"]].isnull().sum())

    number_dict = dict(
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

    return number_dict

def uni(elem, scale, file_csv, file_json):

    statistics = {}
   
    if elem["type"] == "cat":
        
        cat_dict = uni_cat(elem, file_csv)

        statistics.update(
            cat_dict
        )

    elif elem["type"] == "string":

        string_dict = uni_string(elem, file_csv)

        statistics.update(
            string_dict
        )

    elif elem["type"] == "number": 

        number_dict = uni_number(elem, file_csv)

        statistics.update(
            number_dict
        )

    return statistics

def bi(base, elem, scale, file_csv, file_json, split=["split"]):
    # split variable for bi-variate analysis
    categories = dict()

    for j, temp in enumerate(file_json["resources"][0]["schema"]["fields"]):
        if temp["name"] in split:
            s = temp["name"]
            bi = dict()
            bi[s] = dict()
            for index, value in enumerate(temp["values"]):
                v = value["value"]
                temp_csv = file_csv.copy()
                for row in temp_csv.iterrows():
                    if temp_csv[s][row[0]] != v:
                        temp_csv[base][row[0]] = np.nan
                categories[v] = uni(elem, scale, temp_csv, file_json)
                categories[v]["label"] = temp["values"][index]["label"]

                if elem["type"] == "cat":
                    uni_source = uni(elem, scale, file_csv, file_json)
                    for i in ["values", "missings", "labels"]:
                        bi[s][i] = uni_source[i]
                        del categories[v][i]

                elif elem["type"] == "number":
                    uni_source = uni(elem, scale, file_csv, file_json)
                    for i in ["min", "max", "by"]:
                        bi[s][i] = uni_source[i]
                        del categories[v][i]

            bi[s].update(dict(
                label = temp["label"],
                categories = categories,
            ))


    return bi

def stat_dict(dataset_name, elem, file_csv, file_json, base = ["a1", "c1"]):
    scale = elem["type"][0:3]

    # base variable for bi-variate analysis

    stat_dict = dict(
        study = "testsuite",
        dataset = dataset_name,
        variable = elem["name"],
        label = elem["label"],
        scale = scale,
        uni = uni(elem, scale, file_csv, file_json),
        )
    if elem["name"] in base:
        stat_dict["bi"] = bi(elem["name"], elem, scale, file_csv, file_json)
    return stat_dict

def generate_stat(data_name, file_csv, file_json, config):
    dataset_name = re.sub(".csv", "", data_name)
      
    stat = []
    for i, elem in enumerate(file_json["resources"][0]["schema"]["fields"]):
        stat.append(
            stat_dict(dataset_name, elem, file_csv, file_json)
        )
        # Test for Visualization
        vistest(stat[-1], dataset_name, elem["name"], config)

    return stat

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

def main(config, data_csv, data_json):
    for name, data in data_csv.items():
        path_json = re.sub(".csv", ".json", name)
        file_json = data_json[path_json]
        file_csv = data
        parse_dataset(name, file_csv, file_json, config)
