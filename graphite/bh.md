# Codebook


## Variable 1: hid - HID

:---- VARIABLE ----:
{"study": "soep-test", "analysis_unit": "h", "period": 2001, "conceptual_dataset": "net", "sub_type": "net", "boost": 1, "dataset": "bh", "dataset_cs": "bh", "variable": "hid", "name": "hid", "name_cs": "hid", "label": "HID", "scale": "num", "uni": {"density": [0.06807956358302689, 0.07244497958471803, 0.07591075263064148, 0.07864546688408743, 0.08087505043576096, 0.08282944736469279, 0.08469728272804376, 0.08659719163503647, 0.08856742982236486, 0.09056928055182341, 0.09249709199811042, 0.09418918133181849, 0.09543798099279999, 0.09600210935299672, 0.09562505460831616, 0.09406369670127658, 0.09112558125959137, 0.08670873857764985, 0.0808343488462243, 0.07366241389559143], "min": 2.0, "max": 10.0, "by": 0.42105263157894735, "total": 7, "valid": 7, "missing": [0], "num_missings": {"frequencies": [], "labels": [], "values": []}}, "error": "No Errors", "bi": {"wave": {"min": 2.0, "max": 10.0, "by": 0.42105263157894735, "label": "wave", "categories": {"1999": {"density": [0.06807956358302689, 0.07244497958471803, 0.07591075263064148, 0.07864546688408743, 0.08087505043576096, 0.08282944736469279, 0.08469728272804376, 0.08659719163503647, 0.08856742982236486, 0.09056928055182341, 0.09249709199811042, 0.09418918133181849, 0.09543798099279999, 0.09600210935299672, 0.09562505460831616, 0.09406369670127658, 0.09112558125959137, 0.08670873857764985, 0.0808343488462243, 0.07366241389559143], "total": 7, "valid": 7, "missing": [0], "num_missings": {"frequencies": [], "labels": [], "values": []}, "label": 1999}}}}}
:------------------:
    

## Variable 2: wave - wave

:---- VARIABLE ----:
{"study": "soep-test", "analysis_unit": "h", "period": 2001, "conceptual_dataset": "net", "sub_type": "net", "boost": 1, "dataset": "bh", "dataset_cs": "bh", "variable": "wave", "name": "wave", "name_cs": "wave", "label": "wave", "scale": "num", "uni": {"density": [], "min": 1999.0, "max": 1999.0, "by": 0, "total": 7, "valid": 7, "missing": [0], "num_missings": {"frequencies": [], "labels": [], "values": []}}, "error": "No Errors"}
:------------------:
    

## Variable 3: income - Household Net Income

:---- VARIABLE ----:
{"study": "soep-test", "analysis_unit": "h", "period": 2001, "conceptual_dataset": "net", "sub_type": "net", "boost": 1, "dataset": "bh", "dataset_cs": "bh", "variable": "income", "name": "income", "name_cs": "income", "label": "Household Net Income", "scale": "num", "uni": {"density": [1.3406545193702616e-06, 1.3175567722417737e-06, 1.2410171484799274e-06, 1.12048239591235e-06, 9.700438056303158e-07, 8.058409525564157e-07, 6.433880357129848e-07, 4.954363683750107e-07, 3.707453792014442e-07, 2.738222658827038e-07, 2.0542478540234003e-07, 1.634819345953334e-07, 1.4409104261300257e-07, 1.4235910214395405e-07, 1.530042739210036e-07, 1.70756329817259e-07, 1.9065370700170707e-07, 2.083247084959872e-07, 2.2028402267601002e-07, 2.2420974276026857e-07], "min": 20.0, "max": 1000000.0, "by": 52630.52631578947, "total": 7, "valid": 7, "missing": [0], "num_missings": {"frequencies": [], "labels": [], "values": []}}, "error": "No Errors", "bi": {"wave": {"min": 20.0, "max": 1000000.0, "by": 52630.52631578947, "label": "wave", "categories": {"1999": {"density": [1.3406545193702616e-06, 1.3175567722417737e-06, 1.2410171484799274e-06, 1.12048239591235e-06, 9.700438056303158e-07, 8.058409525564157e-07, 6.433880357129848e-07, 4.954363683750107e-07, 3.707453792014442e-07, 2.738222658827038e-07, 2.0542478540234003e-07, 1.634819345953334e-07, 1.4409104261300257e-07, 1.4235910214395405e-07, 1.530042739210036e-07, 1.70756329817259e-07, 1.9065370700170707e-07, 2.083247084959872e-07, 2.2028402267601002e-07, 2.2420974276026857e-07], "total": 7, "valid": 7, "missing": [0], "num_missings": {"frequencies": [], "labels": [], "values": []}, "label": 1999}}}}}
:------------------:
    

## Variable 4: neighbor - Neighborhood Of Household

:---- VARIABLE ----:
{"study": "soep-test", "analysis_unit": "h", "period": 2001, "conceptual_dataset": "net", "sub_type": "net", "boost": 1, "dataset": "bh", "dataset_cs": "bh", "variable": "neighbor", "name": "neighbor", "name_cs": "neighbor", "label": "Neighborhood Of Household", "scale": "cat", "uni": {"frequencies": [2, 3, 1, 0, 1], "values": [1, 2, 3, 4, 5], "missings": ["False", "False", "False", "False", "False"], "labels": ["Res. Area Old", "Res. Area New", "Mixed Resid., Comm. Area", "Commercial Area", "Industrial Area"]}, "error": "No Errors", "bi": {"wave": {"values": [1, 2, 3, 4, 5], "missings": ["False", "False", "False", "False", "False"], "labels": ["Res. Area Old", "Res. Area New", "Mixed Resid., Comm. Area", "Commercial Area", "Industrial Area"], "label": "wave", "categories": {"1999": {"frequencies": [2, 3, 1, 0, 1], "label": 1999}}}}}
:------------------:
    

## Variable 5: text - text

:---- VARIABLE ----:
{"study": "soep-test", "analysis_unit": "h", "period": 2001, "conceptual_dataset": "net", "sub_type": "net", "boost": 1, "dataset": "bh", "dataset_cs": "bh", "variable": "text", "name": "text", "name_cs": "text", "label": "text", "scale": "str", "uni": {"frequencies": [5], "missings": [1]}, "error": "No Errors", "statistics": {"names": ["Valid", "Invalid"], "values": ["5", "2"]}, "bi": {"wave": {"label": "wave", "categories": {"1999": {"frequencies": [5], "missings": [1], "label": 1999}}}}}
:------------------:
    
