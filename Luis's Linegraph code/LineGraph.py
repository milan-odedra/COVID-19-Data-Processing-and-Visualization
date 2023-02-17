#Remember to download the "pandas" library before running code.
#Use "pip install pandas" in the cmd before hand.
import pandas as pd
#This puts the data from day_wise file into the dayVals variable
dayVals=pd.read_csv("Dataset\Covid-19 Dataset\day_wise.csv")

print(dayVals.to_string())
"""for x in dayVals:
    print (x)"""