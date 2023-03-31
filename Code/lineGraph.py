import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics as stat

################## Functions #################


def regionList(RegionList):
    # This puts the separated data from .csv file into a list with their day mean and returns this
    highestDate=1
    Confirmed=[]
    Deaths=[]
    Recovered=[]
    Active=[]

    for x in dayVals["Date"]:

        
        if highestDate!=x:
            highestDate=x
            #Puts the data with the corresponding date to CurrDate
            CurrDate=RegionList[(dayVals["Date"]==(x))]
            #Finds the mean of each column for that date
            Confirmed.append(stat.mean(CurrDate["Confirmed"]))
            Deaths.append(stat.mean(CurrDate["Deaths"]))
            Recovered.append(stat.mean(CurrDate["Recovered"]))
            Active.append(stat.mean(CurrDate["Active"]))

    return Confirmed, Deaths, Recovered, Active
def plotGraph(Name):
    # Plots the graph using the inputs and then shows them
    fig0, ax0=plt.subplots(figsize=(10,5))
    ax0.set_title("Covid-19 cases in "+Name)
    ax0.set_xlabel("Dates")
    ax0.set_ylabel("Number of people")
    ax0.plot(Seconds,Confirmed,label="Confirmed")
    ax0.plot(Seconds,Deaths,label="Deaths")
    ax0.plot(Seconds,Recovered,label="Recovered")
    ax0.legend()

    plt.tight_layout()

    fig0.show()

###################### Main code ###########################

# This puts the data from day_wise file into the dayVals variable
dayVals=pd.read_csv("Data\\full_grouped.csv")
#These separate the data in the UK, not in the UK as well as, into individual regions.
UK=dayVals[(dayVals["Country/Region"]==("United Kingdom"))]
eastMed=dayVals[(dayVals["WHO Region"]==("Eastern Mediterranean"))]
Euro=dayVals[(dayVals["WHO Region"]==("Europe"))]
Africa=dayVals[(dayVals["WHO Region"]==("Africa"))]
America=dayVals[(dayVals["WHO Region"]==("Americas"))]
WstPacific=dayVals[(dayVals["WHO Region"]==("Western Pacific"))]
SouthEastAsia=dayVals[(dayVals["WHO Region"]==("South-East Asia"))]

time=1
Seconds=[]
for x in dayVals["Date"]:
    if time!=x:
        time=x
        #Converts time to a readable format that can be plotted by matplotlib
        Seconds.append(np.datetime64(x))

#Made to show the graphs plotting the#
#             Figures                #
leave=False
while leave!=True:
    Region=str.upper(input("1:All Regions\n2:Eastern Mediterranean\n3:Europe\n4:Africa\n5:Americas\n6:Western Pacific\n7:South-East Asia\n8:UK\nQ:Quit\nPlease enter a number corresponding to the Region in the list : "))
    #Also showes the UK graph just to allow a comparison
    if Region=='1':
        #Puts the data from the list into reigionList and returns them into these variables
        Confirmed, Deaths, Recovered, Active=regionList(dayVals)
        plotGraph("the world")
    elif Region=='2':
        Confirmed, Deaths, Recovered, Active=regionList(eastMed)
        plotGraph("Eastern Mediterranean")
    elif Region=='3':
        Confirmed, Deaths, Recovered, Active=regionList(Euro)
        plotGraph("Europe")
    elif Region=='4':
        Confirmed, Deaths, Recovered, Active=regionList(Africa)
        plotGraph("Africa")
    elif Region=='5':
        Confirmed, Deaths, Recovered, Active=regionList(America)
        plotGraph("Americas")
    elif Region=='6':
        Confirmed, Deaths, Recovered, Active=regionList(WstPacific)
        plotGraph("Western Pacific")
    elif Region=='7':
        Confirmed, Deaths, Recovered, Active=regionList(SouthEastAsia)
        plotGraph("South-East Asia")
    elif Region=='8':
        Confirmed, Deaths, Recovered, Active=regionList(UK)
        plotGraph("the UK")
    elif Region=='Q':
        leave=True
