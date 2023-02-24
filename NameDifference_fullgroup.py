import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
from datetime import datetime, timedelta

# data =  pd.read_csv('Data\\full_grouped.csv', sep=",")
# data = data.rename(columns={'WHO Region': 'WHORegion','Country/Region': 'country'})
# data_german = data.query('country == "Germany"')
# data_UK = data.query('country == "United Kingdom"')
# print(data_german)
# plt.plot(data_german["Date"], data_german["Confirmed"], label="German")
# plt.plot(data_UK["Date"], data_UK["Confirmed"], label="UK")

# Reading files
covid_df =  pd.read_csv('Data\\full_grouped.csv', sep=",")
codes = pd.read_csv("Geo\\all.csv")

#Has 2 different congo sets, i combine them


#Which Country names are different
codesName = list(codes["name"])
codesNameUL = pd.DataFrame(list(codes["name"]), columns=["Code name"])
covidName = list(dict.fromkeys(covid_df["Country/Region"]))
covidNameUL = pd.DataFrame(list(dict.fromkeys(covid_df["Country/Region"])),columns=["Covid name"])
codesNamelist = list(codes["name"])
#print(codesName)
#print(covidName)

#print("Codes name length ",len(codesName))
#print("Covidname length ",len(covidName))



covidcountry = pd.merge(left=codesNameUL,right=covidNameUL,how="right",left_on="Code name",right_on="Covid name")
print(covidcountry)

notnumber = []
matches = []

#print(covidcountry["Covid name"])
#print(covidName)
codesName = list(covidcountry["Code name"])
covidcountry = list(covidcountry["Covid name"])

print(codesName)
print(covidcountry)

for i in range(0,len(codesName)):
    if pd.isna(codesName[i]):
        matches.append(covidcountry[i])
print(matches)
#print(list(codes["name"]))

    

