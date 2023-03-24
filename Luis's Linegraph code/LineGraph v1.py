#Remember to download the "pandas" library before running code.
#Use "pip install pandas" in the cmd before hand. Do the same for matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
#Functions
#This calculates the average of the day in the csv file.
def dayAvg(x):
    Avg=0
    print(x)

###Main code###


# This puts the data from day_wise file into the dayVals variable
dayVals=pd.read_csv("Dataset\Covid-19 Dataset\\full_grouped.csv")
#These separate the data in the UK and not in the UK.
UK=dayVals[(dayVals["Country/Region"]==("United Kingdom"))]
notUK=dayVals[(dayVals["Country/Region"]!=("United Kingdom"))]
# Eastern Mediterranean
# Europe
# Africa
# Americas
# Western Pacific
# South-East Asia
eastMed=dayVals[(dayVals["WHO Region"]==("Eastern Mediterranean"))]
Euro=dayVals[(dayVals["WHO Region"]==("Europe"))]
Africa=dayVals[(dayVals["WHO Region"]==("Africa"))]
America=dayVals[(dayVals["WHO Region"]==("Americas"))]
WstPacific=dayVals[(dayVals["WHO Region"]==("Western Pacific"))]
SouthEastAsia=dayVals[(dayVals["WHO Region"]==("South-East Asia"))]
Date=dayVals["Date"]
#Prints the UK and notUK csv files
# print(Date)
# print (UK)
# print (notUK)
#Separates the dates
time=1
Timelist=[]
# An attempt to plot the graph
x=0
with open ("Dataset\Covid-19 Dataset\\full_grouped.csv","r") as d:
    lists=csv.reader(d)
    Timelist.append(list[0])
Seconds=[]
Confirmed=[]
Deaths=[]
Recovered=[]
Active=[]
newCases=[]
newDeaths=[]
newRecovered=[]
for x in Date:
    # print(x)
    
    if time!=x:
        time=x
        #Converts time to a readable format that can be plotted by matplotlib
        Seconds.append(np.datetime64(x))
        #Puts the data with the corresponding date to CurrDate
        CurrDate=dayVals[(dayVals["Date"]==(x))]
        #Finds the mean of each column for that date
        Confirmed.append((CurrDate["Confirmed"]).mean())
        Deaths.append((CurrDate["Deaths"]).mean())
        Recovered.append((CurrDate["Recovered"]).mean())
        Active.append((CurrDate["Active"]).mean())
        # newCases.append((CurrDate["New cases"]).mean())
        # newDeaths.append((CurrDate["New deaths"]).mean())
        # newRecovered.append((CurrDate["New recovered"]).mean())
        # Timelist.append([Confirmed,Deaths,Recovered,Active,newCases,newDeaths,newRecovered])
#Allows to see the time
# print(Seconds)
# #Creates a random number for each date, Checks if the dates work
# X = np.random.randn(len(Seconds))
# fig, ax=plt.subplots()
# ax.plot(Seconds,X)
#Plots the UK and notUK data on the same figure
fig, ax=plt.subplots(2)
fig.suptitle("Covid-19 cases")
ax[1].set_title("Covid-19 cases in the world")
ax[1].set_xlabel("Dates")
ax[1].set_ylabel("Number of people")
ax[1].plot(Seconds,Confirmed,label="Confirmed")
ax[1].plot(Seconds,Deaths,label="Deaths")
ax[1].plot(Seconds,Recovered,label="Recovered")
# ax[1].plot(Seconds,Active,label="Active")
# ax[1].plot(Seconds,newCases,label="New Cases")
# ax[1].plot(Seconds,newDeaths,label="New Deaths")
# ax[1].plot(Seconds,newRecovered,label="New Recovered")
ax[1].legend()
ax[0].set_title("Covid-19 cases in the UK")
ax[0].set_xlabel("Dates")
ax[0].set_ylabel("Number of people")
ax[0].plot(Seconds,UK["Confirmed"],label="Confirmed")
ax[0].plot(Seconds,UK["Deaths"],label="Deaths")
ax[0].plot(Seconds,UK["Recovered"],label="Recovered")
# ax[0].plot(Seconds,UK["Active"],label="Active")
# ax[0].plot(Seconds,UK["New cases"],label="New Cases")
# ax[0].plot(Seconds,UK["New deaths"],label="New Deaths")
# ax[0].plot(Seconds,UK["New recovered"],label="New Recovered")
ax[0].legend()
plt.tight_layout()
#Need to put each label into their own graphs with the major WHO reigons being shown.##Current##
plt.show()