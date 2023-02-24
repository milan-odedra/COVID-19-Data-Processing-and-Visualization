#Remember to download the "pandas" library before running code.
#Use "pip install pandas" in the cmd before hand. Do the same for matplotlib
import pandas as pd
import matplotlib.pyplot as plt
# This puts the data from day_wise file into the dayVals variable
dayVals=pd.read_csv("Dataset\Covid-19 Dataset\\full_grouped.csv")
#These separate the data in the UK and not in the UK.
UK=dayVals[(dayVals["Country/Region"]==("United Kingdom"))]
notUK=dayVals[(dayVals["Country/Region"]!=("United Kingdom"))]
print (UK)
print (notUK)


#print(dayVals.to_string())
# print(dayVals)

UK.plot()
notUK.plot()
plt.show()