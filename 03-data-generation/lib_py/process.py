import os,sys
import numpy as np

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

def process(dataset, format, generationscript, stats):

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
    if generationscript != np.nan:
        module = __import__(generationscript)
    
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
