# Codebook


## Variable 1: hid - HID

:---- VARIABLE ----:
{"study": "soep-test", "analysis_unit": "h", "period": 2001, "conceptual_dataset": "net", "sub_type": "net", "boost": 1, "dataset": "ch", "dataset_cs": "ch", "variable": "hid", "name": "hid", "name_cs": "hid", "label": "HID", "scale": "num", "uni": {"density": [0.0478095766109232, 0.05059784497601558, 0.053279941680317154, 0.05627813035184547, 0.06005539511302416, 0.06502634226042153, 0.07146805934565556, 0.07944887798768077, 0.08878934931289431, 0.09906295474135805, 0.10963604023041885, 0.11973923428955255, 0.12855776617606582, 0.13532633591909324, 0.13941525891773401, 0.14039760375177363, 0.13809083954697723, 0.13257021072867525, 0.1241542282855229, 0.11336530383227536], "min": 3.0, "max": 10.0, "by": 0.36842105263157876, "total": 5, "valid": 5, "missing": [0], "num_missings": {"frequencies": [], "labels": [], "values": []}}, "error": "No Errors", "bi": {"wave": {"min": 3.0, "max": 10.0, "by": 0.36842105263157876, "label": "wave", "categories": {"2000": {"density": [0.0478095766109232, 0.05059784497601558, 0.053279941680317154, 0.05627813035184547, 0.06005539511302416, 0.06502634226042153, 0.07146805934565556, 0.07944887798768077, 0.08878934931289431, 0.09906295474135805, 0.10963604023041885, 0.11973923428955255, 0.12855776617606582, 0.13532633591909324, 0.13941525891773401, 0.14039760375177363, 0.13809083954697723, 0.13257021072867525, 0.1241542282855229, 0.11336530383227536], "total": 5, "valid": 5, "missing": [0], "num_missings": {"frequencies": [], "labels": [], "values": []}, "label": 2000}}}}}
:------------------:
    

## Variable 2: wave - wave

:---- VARIABLE ----:
{"study": "soep-test", "analysis_unit": "h", "period": 2001, "conceptual_dataset": "net", "sub_type": "net", "boost": 1, "dataset": "ch", "dataset_cs": "ch", "variable": "wave", "name": "wave", "name_cs": "wave", "label": "wave", "scale": "num", "uni": {"density": [], "min": 2000.0, "max": 2000.0, "by": 0, "total": 5, "valid": 5, "missing": [0], "num_missings": {"frequencies": [], "labels": [], "values": []}}, "error": "No Errors"}
:------------------:
    

## Variable 3: income - Household Net Income

:---- VARIABLE ----:
{"study": "soep-test", "analysis_unit": "h", "period": 2001, "conceptual_dataset": "net", "sub_type": "net", "boost": 1, "dataset": "ch", "dataset_cs": "ch", "variable": "income", "name": "income", "name_cs": "income", "label": "Household Net Income", "scale": "num", "uni": {"density": [5.026348136034054e-06, 5.030012749794374e-06, 4.902644266113472e-06, 4.656493684238778e-06, 4.313380203596311e-06, 3.902069596126507e-06, 3.4548994512376025e-06, 3.0041853365417438e-06, 2.57892792844192e-06, 2.202233034919138e-06, 1.8896912004690129e-06, 1.6487857448013575e-06, 1.479245923291138e-06, 1.3741581232549456e-06, 1.3215972356907412e-06, 1.3065329924077967e-06, 1.3127860707114825e-06, 1.324841416992938e-06, 1.3293630545419907e-06, 1.3162940797625952e-06], "min": 1500.0, "max": 200000.0, "by": 10447.368421052632, "total": 5, "valid": 5, "missing": [0], "num_missings": {"frequencies": [], "labels": [], "values": []}}, "error": "No Errors", "bi": {"wave": {"min": 1500.0, "max": 200000.0, "by": 10447.368421052632, "label": "wave", "categories": {"2000": {"density": [5.026348136034054e-06, 5.030012749794374e-06, 4.902644266113472e-06, 4.656493684238778e-06, 4.313380203596311e-06, 3.902069596126507e-06, 3.4548994512376025e-06, 3.0041853365417438e-06, 2.57892792844192e-06, 2.202233034919138e-06, 1.8896912004690129e-06, 1.6487857448013575e-06, 1.479245923291138e-06, 1.3741581232549456e-06, 1.3215972356907412e-06, 1.3065329924077967e-06, 1.3127860707114825e-06, 1.324841416992938e-06, 1.3293630545419907e-06, 1.3162940797625952e-06], "total": 5, "valid": 5, "missing": [0], "num_missings": {"frequencies": [], "labels": [], "values": []}, "label": 2000}}}}}
:------------------:
    

## Variable 4: neighbor - Neighborhood Of Household

:---- VARIABLE ----:
{"study": "soep-test", "analysis_unit": "h", "period": 2001, "conceptual_dataset": "net", "sub_type": "net", "boost": 1, "dataset": "ch", "dataset_cs": "ch", "variable": "neighbor", "name": "neighbor", "name_cs": "neighbor", "label": "Neighborhood Of Household", "scale": "cat", "uni": {"frequencies": [3, 2, 0, 0, 0], "values": [1, 2, 3, 4, 5], "missings": ["False", "False", "False", "False", "False"], "labels": ["Res. Area Old", "Res. Area New", "Mixed Resid., Comm. Area", "Commercial Area", "Industrial Area"]}, "error": "No Errors", "bi": {"wave": {"values": [1, 2, 3, 4, 5], "missings": ["False", "False", "False", "False", "False"], "labels": ["Res. Area Old", "Res. Area New", "Mixed Resid., Comm. Area", "Commercial Area", "Industrial Area"], "label": "wave", "categories": {"2000": {"frequencies": [3, 2, 0, 0, 0], "label": 2000}}}}}
:------------------:
    

## Variable 5: text - text

:---- VARIABLE ----:
{"study": "soep-test", "analysis_unit": "h", "period": 2001, "conceptual_dataset": "net", "sub_type": "net", "boost": 1, "dataset": "ch", "dataset_cs": "ch", "variable": "text", "name": "text", "name_cs": "text", "label": "text", "scale": "str", "uni": {"frequencies": [3], "missings": [1]}, "error": "No Errors", "statistics": {"names": ["Valid", "Invalid"], "values": ["4", "1"]}, "bi": {"wave": {"label": "wave", "categories": {"2000": {"frequencies": [3], "missings": [1], "label": 2000}}}}}
:------------------:
    
