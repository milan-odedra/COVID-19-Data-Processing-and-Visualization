#Remember to download the "pandas" library before running code.
#Use "pip install pandas" in the cmd before hand. Do the same for matplotlib
import pandas as pd
import matplotlib.pyplot as plt
# This puts the data from day_wise file into the dayVals variable
dayVals=pd.read_csv("Dataset\Covid-19 Dataset\\full_grouped.csv")
UK=dayVals[(dayVals["Country/Region"]==("United Kingdom"))]
print (UK)


#print(dayVals.to_string())
# print(dayVals)

dayVals.plot()
plt.show()
print(UK)