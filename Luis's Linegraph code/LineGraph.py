#Remember to download the "pandas" library before running code.
#Use "pip install pandas" in the cmd before hand. Do the same for matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import csv

#Functions
#This calculates the average of the day in the csv file.
def dayAvg(x):
    Avg=0
    print(x)

#Main code


# This puts the data from day_wise file into the dayVals variable
dayVals=pd.read_csv("Dataset\Covid-19 Dataset\\full_grouped.csv")
#These separate the data in the UK and not in the UK.
UK=dayVals[(dayVals["Country/Region"]==("United Kingdom"))]
notUK=dayVals[(dayVals["Country/Region"]!=("United Kingdom"))]
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

for x in Date:
    # print(x)
    
    if time!=x:
        time=x
        #Puts the data with the corresponding date to CurrDate
        CurrDate=dayVals[(dayVals["Date"]==(x))]
        #Finds the mean of each column for that date
        Confirmed=(CurrDate["Confirmed"]).mean()
        Deaths=(CurrDate["Deaths"]).mean()
        Recovered=(CurrDate["Recovered"]).mean()
        Active=(CurrDate["Active"]).mean()
        newCases=(CurrDate["New cases"]).mean()
        newDeaths=(CurrDate["New deaths"]).mean()
        newRecovered=(CurrDate["New recovered"]).mean()
        Timelist.append([time,Confirmed,Deaths,Recovered,Active,newCases,newDeaths,newRecovered])

X=len(Timelist)
print(Timelist)

#Plots the UK and notUK data
for i in range(len(Timelist[0])):
    plt.plot(X,[pt[i]for pt in Timelist]),lebel='id %s'%i)
UK.plot()
notUK.plot()
plt.show()