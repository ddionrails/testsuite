import os,sys, shutil

sys.path.append(os.path.abspath("../ddi.py"))
from ddi.dataset import Dataset

def export_data(dataset, testscript):

    d1 = Dataset()

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
    shutil.copy2("03-data-generation/output/" + dataset + "_stats." + stats)
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
