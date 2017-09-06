import os,sys
import numpy as np
from os import listdir
import re

from lib_py.generation_scripts import Generations

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

def import_data(dataset, format, testscript):
    
    print("")
    print("[Generation]: Import Data (%s)" % dataset)

    d1 = Dataset()

    if format == "tdp":
        d1.read_tdp(
            "02-temp/" + dataset + ".csv", 
            "02-temp/" + dataset + ".json"
        )
        
    elif format == "stata":
        d1.read_stata(
            "02-temp/" + dataset + ".dta"
        )
    
    else:
        print("[ERROR]: Wrong format: %s for %s" % (format, dataset))

    # Export test
    if testscript != "":
        sys.path.append('03-data-generation/test')
        import import_test

    d1.write_tdp(
        "03-data-generation/input/" + dataset + ".csv", 
        "03-data-generation/input/" + dataset + ".json"
    )
    

def process(dataset, format, generationscript, stats):

    print("")
    print("[Generation]: Data Processing (%s)" % dataset)

    d1 = Dataset()

    if format == "tdp":
        d1.read_tdp(
            "03-data-generation/input/" + dataset + ".csv", 
            "03-data-generation/input/" + dataset + ".json"
        )
        
    elif format == "stata":
        d1.read_stata(
            "03-data-generation/input/" + dataset + ".dta"
        )
    
    else:
        print("[ERROR]: Wrong format: %s for %s" % (format, dataset))

    d1.write_tdp(
        "03-data-generation/output/" + dataset + ".csv", 
        "03-data-generation/output/" + dataset + ".json"
    )

    #statistics before generations
    if stats == "json":
        d1.write_stats(
            "03-data-generation/output/" + dataset + "_stats.json"
        )
    elif stats == "html":
        d1.write_stats(
            "03-data-generation/output/" + dataset + "_stats.html", file_type="html"
        )
    elif stats == "yaml":
        d1.write_stats(
            "03-data-generation/output/" + dataset + "_stats.yaml", file_type="yaml"
        )
    else:
        print("The format for statistics %s is not supported" % stats)

    # generations
    if isinstance(generationscript, str):
        
        d2 = Generations(d1)
        
        try:
            eval("d2." + generationscript + "()")
        except:
            print("[Error]: The generationscript %s doesn't exist" % generationscript)
    
        d1.write_tdp(
            "03-data-generation/output/" + dataset + "_gen.csv", 
            "03-data-generation/output/" + dataset + "_gen.json"
        )
        
        #statistics after generations
        if stats == "json":
            d1.write_stats(
                "03-data-generation/output/" + dataset + "_gen_stats.json"
            )
        elif stats == "html":
            d1.write_stats(
                "03-data-generation/output/" + dataset + "_gen_stats.html", file_type="html"
            )
        elif stats == "yaml":
            d1.write_stats(
                "03-data-generation/output/" + dataset + "_gen_stats.yaml", file_type="yaml"
            )
        else:
            print("The format for statistics %s is not supported" % stats)
            
      
def export_data(dataset, testscript):

    print("")
    print("[Generation]: Export Data (%s)" % dataset)

    d1 = Dataset()
    
    fil = [f for f in listdir("03-data-generation/output/") if re.search("^" + dataset + "(\.|\_)", f)]
    
    
    for i in fil:
        print(i)
    
    d1.read_tdp(
        "03-data-generation/output/" + dataset + ".csv", 
        "03-data-generation/output/" + dataset + ".json"
    )

    # Export test
    sys.path.append('03-data-generation/test')
    import export_test

    d1.write_tdp(
        "03-temp/" + dataset + ".csv", 
        "03-temp/" + dataset + ".json"
    )
    # shutil.copy2("03-data-generation/output/" + dataset + "_stats." + stats)
    # to doooooooooooooooooooooooooooo
    #
    # 
    #
    #
    #
    #!!!!!!!!!!!
    
    try:
        d1.read_tdp(
            "03-data-generation/output/" + dataset + "_gen.csv", 
            "03-data-generation/output/" + dataset + "_gen.json"
        )

        # Export test
        sys.path.append('03-data-generation/test')
        import export_test

        d1.write_tdp(
            "03-temp/" + dataset + "_gen.csv", 
            "03-temp/" + dataset + "_gen.json"
        )
        
    except:
        pass
        

