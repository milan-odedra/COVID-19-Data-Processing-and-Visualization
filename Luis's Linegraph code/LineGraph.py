##    What to do:     ##
#-Plot covid lockdown timeline in the UK 3
#Remember to download the "pandas" library before running code if it isn't installed yet.
#Use "pip install pandas" in the cmd before hand. Do the same for matplotlib.
import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np

################## Functions #################


def regionList(List):
    """This puts the separated data from .csv file into a list with their day mean and returns this"""
    highestDate=1
    Confirmed=[]
    Deaths=[]
    Recovered=[]
    Active=[]
    # newCases=[]
    # newDeaths=[]
    # newRecovered=[]
    for x in dayVals["Date"]:
        # print(x)
        
        if highestDate!=x:
            highestDate=x
            #Puts the data with the corresponding date to CurrDate
            CurrDate=dayVals[(dayVals["Date"]==(x))]
            #Finds the mean of each column for that date
            Confirmed.append((CurrDate["Confirmed"]).mean())
            Deaths.append((CurrDate["Deaths"]).mean())
            Recovered.append((CurrDate["Recovered"]).mean())
            Active.append((CurrDate["Active"]).mean())
            #######################################
            ###Incase I want to re-add all of the rest of the plots.###
            # newCases.append((CurrDate["New cases"]).mean())
            # newDeaths.append((CurrDate["New deaths"]).mean())
            # newRecovered.append((CurrDate["New recovered"]).mean())
            # Timelist.append([Confirmed,Deaths,Recovered,Active,newCases,newDeaths,newRecovered])
            #######################################
    return Confirmed, Deaths, Recovered, Active
def plotGraph(Name):
    """Plots the graph using the inputs and then shows them"""
    fig0, ax0=plt.subplots(figsize=(10,5))
    fig0.suptitle("Covid-19 cases")
    ax0.set_title("Covid-19 cases in "+Name)
    ax0.set_xlabel("Dates")
    ax0.set_ylabel("Number of people")
    ax0.plot(Seconds,Confirmed,label="Confirmed")
    ax0.plot(Seconds,Deaths,label="Deaths")
    ax0.plot(Seconds,Recovered,label="Recovered")
    ax0.legend()
    
    ###Incase I want to re-add all of the rest of the plots.###
    # ax[1].plot(Seconds,Active,label="Active")
    # ax[1].plot(Seconds,newCases,label="New Cases")
    # ax[1].plot(Seconds,newDeaths,label="New Deaths")
    # ax[1].plot(Seconds,newRecovered,label="New Recovered")
    ######################
    fig1, ax1=plt.subplots(figsize=(10,5))
    ax1.set_title("Covid-19 cases in the UK")
    ax1.set_xlabel("Dates")
    ax1.set_ylabel("Number of people")
    ax1.plot(Seconds,UK["Confirmed"],label="Confirmed")
    ax1.plot(Seconds,UK["Deaths"],label="Deaths")
    ax1.plot(Seconds,UK["Recovered"],label="Recovered")
    ax1.legend()
    plt.tight_layout()
    #Need to put each label into their own graphs with the major WHO reigons being shown.##Current##
    fig0.show()
    fig1.show()
    input("To close the figure, input any key: ")
###################### Main code ###########################

# This puts the data from day_wise file into the dayVals variable
dayVals=pd.read_csv("Dataset\Covid-19 Dataset\\full_grouped.csv")
#These separate the data in the UK, not in the UK as well as, into individual regions.
UK=dayVals[(dayVals["Country/Region"]==("United Kingdom"))]
allRegions=dayVals[(dayVals["Country/Region"]!=("United Kingdom"))]
eastMed=dayVals[(dayVals["WHO Region"]==("Eastern Mediterranean"))]
Euro=dayVals[(dayVals["WHO Region"]==("Europe"))]
Africa=dayVals[(dayVals["WHO Region"]==("Africa"))]
America=dayVals[(dayVals["WHO Region"]==("Americas"))]
WstPacific=dayVals[(dayVals["WHO Region"]==("Western Pacific"))]
SouthEastAsia=dayVals[(dayVals["WHO Region"]==("South-East Asia"))]
####################################
#Prints the UK and notUK csv files (Test code)
# print(Date)
# print (UK)
# print (notUK)
######################################
#Separates the dates
time=1
#Used purely for the graph (the X axis)
Seconds=[]
for x in dayVals["Date"]:
    # print(x)
    if time!=x:
        time=x
        #Converts time to a readable format that can be plotted by matplotlib
        Seconds.append(np.datetime64(x))
######################################
##########Temporary menu##############
######################################
#Puts the data from the list into reigionList and returns them into these variables
leave=0
while leave!=True:
    Region=input("1:All Regions\n2:Eastern Mediterranean\n3:Europe\n4:Africa\n5:Americas\n6:Western Pacific\n7:South-East Asia\nQ:Quit\nPlease enter a number corresponding to the Region in the list: ")
    if Region=='1':
        Confirmed, Deaths, Recovered, Active=regionList(allRegions)
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
    elif Region=='Q':
        leave=1
########################################
# print(Seconds)
# #Creates a random number for each date, Checks if the dates work
# X = np.random.randn(len(Seconds))
# fig, ax=plt.subplots()
# ax.plot(Seconds,X)
# #################################
# ax[0].set_title("Covid-19 cases in the UK")
# ax[0].set_xlabel("Dates")
# ax[0].set_ylabel("Number of people")
# ax[0].plot(Seconds,UK["Confirmed"],label="Confirmed")
# ax[0].plot(Seconds,UK["Deaths"],label="Deaths")
# ax[0].plot(Seconds,UK["Recovered"],label="Recovered")
####################################
###Incase I want to re-add all of the rest of the plots.###
# ax[0].plot(Seconds,UK["Active"],label="Active")
# ax[0].plot(Seconds,UK["New cases"],label="New Cases")
# ax[0].plot(Seconds,UK["New deaths"],label="New Deaths")
# ax[0].plot(Seconds,UK["New recovered"],label="New Recovered")
# ax[0].legend()
# plt.tight_layout()
# #Need to put each label into their own graphs with the major WHO reigons being shown.##Current##
# plt.show()
plotGraph("the world")