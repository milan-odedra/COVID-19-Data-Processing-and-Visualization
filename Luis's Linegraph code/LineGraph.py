#Remember to download the "pandas" library before running code.
#Use "pip install pandas" in the cmd before hand. Do the same for matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt
# This puts the data from day_wise file into the dayVals variable
# dayVals=pd.read_csv("Dataset\Covid-19 Dataset\day_wise.csv")
UK=[]
# with open ("Dataset\Covid-19 Dataset\\full_grouped.csv","r") as split:
#     line = split.readlines()
#     print(line)
#     for x in line:
#         if x=="United Kingdom":
#             UK.append(x)
      
dayVals=pd.read_csv("Dataset\Covid-19 Dataset\\full_grouped.csv")
for x in (dayVals):
    for y in x:
        if x==("United Kingdom"):
            UK.append(x)

#print(dayVals.to_string())
# print(dayVals)

# dayVals.plot()
# plt.show()
print(UK)