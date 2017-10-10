import os,sys
import numpy as np

class Crosstest():
    def __init__(self):
        for i in dir(self):
            if i.startswith('crosstest'):
                result = getattr(self, i)()
               
    def crosstest_01_foreign_key(self):
        print("Testing Foreign Keys...")
        # TO DO
        print("...check")
        
    def crosstest_99_clean_temp(self):
        print("Clean metadata/temp/")
        os.system("sh metatest/clean_temp.sh")
