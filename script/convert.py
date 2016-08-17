from .packages import *
from .config import config

def get_names (name):
    # get name without path
    data_name = basename(name)
    # get folder name in output
    data_folder = re.sub(".csv", "/", data_name)
    return data_name, data_folder

def save_yaml(data_yaml, data_folder, format, stat, config):

    print("write \"" + data_yaml + "\" in \"output/" + data_folder + "\"")
    with open("".join((config["output"], data_folder, format, data_yaml)), "w") as yaml_file:
      yaml_file.write(yaml.dump(stat, default_flow_style=False))

def save_json(data_json, data_folder, format, stat, config):

    print("write \"" + data_json + "\" in \"output/" + data_folder + "\"")
    with open("".join((config["output"], data_folder, format, data_json)), "w") as json_file:
      json_file.write(json.dumps(stat, data_json))

def parse_dataset(name, file_csv, file_json, config):

    data_name, data_folder = get_names(name)

    print("create folder \"output/" + data_folder + "\"")
    os.mkdir("".join((config["output"], data_folder)))

    stat = generate_stat(data_name, file_csv, file_json)

    format = "statistics_"
    
    # yaml name
    data_yaml = re.sub(".csv", ".yaml", data_name) 
    save_yaml(data_yaml, data_folder, format, stat, config)

    # json name
    data_json = re.sub(".csv", ".json", data_name) 
    save_json(data_json, data_folder, format, stat, config)

def uni(elem, scale, file_csv, file_json):

    statistics = []
 
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

    # weighted
    weighted = []
   
    if elem["type"] == "cat":
        
        frequencies = []
        weighted = []
        values = []
        missings = []
        labels = []
            

        '''

        for v,l in value_labels.items():
            if v == 4294967293:
                v = -3
            if v == 4294967294:
                v = -2
            if v == 4294967295:
                v = -1
            values.append(v)
            labels.append(l)
            if v<0:
                missings.append("true")
            else:
                missings.append("false")
            count = 0
            for index, value in enumerate(df_data[var["name"]]):
                if value == v:
                    count += 1
            frequencies.append(count)
        '''
        statistics.append(
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

        statistics.append(
            dict(
                frequencies = frequencies,
                missings = missings,
            )
        )

    #number
    else:  
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

        #missings
        '''
        [-1] keine Angabe 
        [-2] trifft nicht zu 
        [-3] nicht valide
        [<(-4)] undefiniert
        '''
        count_missing = 0
        count_nv = 0
        count_tnz = 0
        count_kA = 0
        count_ud = 0
        for index, value in enumerate(df_mis):
            if value == -1:
                count_kA += 1
                count_missing += 1
            elif value == -2:
                count_tnz += 1
                count_missing += 1
            elif value == -3:
                count_nv += 1
                count_missing += 1
            elif value < -3:
                count_ud += 1
                count_missing += 1
            missing = count_missing
            nv = count_nv
            tnz = count_tnz
            kA = count_kA
            ud = count_ud

        # missing frequencies
        missings["frequencies"].append(kA)
        missings["frequencies"].append(tnz)
        missings["frequencies"].append(nv)
        # missings["frequencies"].append(ud)

        # missing labels
        missings["labels"].append("keine Angabe")
        missings["labels"].append("trifft nicht zu")
        missings["labels"].append("nicht valide")
        # missings["labels"].append("undefiniert")

        # missing values
        missings["values"].append(-1)
        missings["values"].append(-2)
        missings["values"].append(-3)
        # missings["values"].append("<-4")

        # missing weighted = missing frequencies (placeholder)
        missings["weighted"].append(kA)
        missings["weighted"].append(tnz)
        missings["weighted"].append(nv)
        # missings["weighted"].append(ud)

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

        statistics.append(
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


def generate_stat(data_name, file_csv, file_json):
    dataset_name = re.sub(".csv", "", data_name)
      
  
    stat = []
    for i, elem in enumerate(file_json["resources"][0]["schema"]["fields"]):
        scale = elem["type"]
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

    return stat

def main(config, data_csv, data_json):
    for name, data in data_csv.items():
        path_json = re.sub(".csv", ".json", name)
        file_json = data_json[path_json]
        file_csv = data
        '''
        for i, elem in enumerate(file_json["resources"][0]["schema"]["fields"]):
          print(elem["type"])
        '''
        parse_dataset(name, file_csv, file_json, config)
