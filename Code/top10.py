import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import style 


while True:
    df =pd.read_csv('Data/worldometer_data.csv')



    Menu=str.upper(input("\n1) Top 10 Recovered Countries Ranking Table \n2: Top 10 Total Covid In Population Ranking Table \n3: Top 10 Covid19 Death Countries Ranking Table \n4: Top 10 Active Covid19 Countries Ranking table \n5: Plot Graph Recovered Countries \n6: Plot Graph Total Covid In Populatiob  \n7: Plot Graph Covid19 Deaths  \n8: Plot Graph Top Active Covid19 Countries   \n9: Save Top 10 Recovered Countries Ranking Table to Excel File \n10: Save Top 10 Total Covid in Population Ranking Table to Excel File  \n11: Save Top 10 Covid19 Death Countries Ranking Table to Excel File  \n12: Save Top 10 Active Covid Countries Ranking Table to Excel File \nQ: Quit \n\nPlease select an option: "))

    ####################
    ####Table Format####
    ####################
    
    df_data = df.loc[:,['Country/Region', 'Population', 'TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases']].copy()


    allPopulation = df['Population'].sum()

    allTests = df['TotalTests'].sum()

    allDeaths = df['TotalDeaths'].sum()

    allCases = df['TotalCases'].sum()


    #####################
    ##  Scalping Data  ##
    ## Ascending Order ##
    #####################

    topTotalDeaths = df_data.sort_values('TotalDeaths', ascending=False)

    topTotalCases = df_data.sort_values('TotalCases', ascending=False)

    topTotalRecovered = df_data.sort_values('TotalRecovered', ascending=False)

    topActiveCases = df_data.sort_values('ActiveCases', ascending=False)


    ################
    # top 10 Deaths#
    ################
    top10Deaths = topTotalDeaths[0:10]



    #####################
    # Top 10 Total Cases#
    #####################
    top10Cases = topTotalCases[0:10]



    #########################
    # Top 10 Total Recovered#
    #########################
    top10Recovered = topTotalRecovered[0:10]


    ######################
    # Top 10 Active Cases#
    ######################                           
    top10Active = topActiveCases[0:10]


    


    if Menu =="1":
        ###################
        """%%Recovered%%"""
        ###################

        for col in top10Recovered.columns[4:5]:
            i_name = 'Percentage % ' + col
            i_group = (top10Recovered['TotalRecovered'] / top10Recovered['TotalCases']) * 100
            top10Recovered[i_name] = i_group

        print("[Top 10 Recovered Countries] Percentage of people recovered from Covid \n", top10Recovered)



    elif Menu =="2":

        ####################
        """%%Population%%"""
        ####################


        for col in top10Cases.columns[2:3]:
            i_name = 'Percentage % ' + col
            i_group = (top10Cases['TotalCases'] / top10Cases['Population']) * 100
            top10Cases[i_name] = i_group

        print("[Top 10 Total Case Countries] Percentage of total Covid cases in population \n",top10Cases)





    elif Menu =="3":
        ####################
        """%%%%Death%%%%%"""
        ####################


        for col in top10Deaths.columns[3:4]:
            i_name = 'Percentage % ' + col
            i_group = (top10Deaths['TotalDeaths'] / top10Deaths['TotalCases']) * 100
            top10Deaths[i_name] = i_group

        print("[Top 10 Death Countries] Percentage of total death from total Covidcases \n", top10Deaths)



    elif Menu =="4":
        ####################
        """%%%%Active%%%%"""
        ####################


        for col in top10Active.columns[5:6]:
            i_name = 'Percentage % ' + col
            i_group =(top10Active['ActiveCases'] / top10Active['TotalCases']) * 100
            top10Active[i_name] = i_group

        print("[Top 10 Active Countries] Percentage of Active Cases in Total Covid Cases \n", top10Active)


    elif Menu =="5":

        #X and Y axis Recovered Countries Plot graph
        YRecovered = top10Recovered['TotalRecovered']
        XRecovered = top10Recovered['Country/Region']

        #style name
        style.use('ggplot')
        # outter background
        plt.figure(facecolor='#89cff0')
        ax = plt.axes()
        # inner background
        ax.set_facecolor("#899cf0")

        # Bar Chart Data,Width,Labels, Color
        plt.bar(XRecovered, YRecovered, color ="aqua", width =0.5)
        # X label
        plt.xlabel('Country')
        # Y Label
        plt.ylabel("Covid19 Recoveries (millions)")
        # Title
        plt.title("Top 10 Covid19 Recovered Countries")
        # Show bar Chart
        plt.show()

    elif Menu =="6":
        # X and Y axis for Bar Chart
        YCases = top10Cases['TotalCases']
        XCases = top10Cases['Country/Region']


        #style name
        style.use('ggplot')
        # outter background
        plt.figure(facecolor='#89cff0')
        ax = plt.axes()
        # inner background
        ax.set_facecolor("#899cf0")

        # Bar Chart Data,Width,Labels, Color
        plt.bar(XCases, YCases, color ="aqua", width =0.5)
        # X label
        plt.xlabel('Country')
        # Y Label
        plt.ylabel("Total Covid19 Cases in Population (millions)")
        # Title
        plt.title("Top 10 Total Covid19 In Population")
        # Show bar Chart
        plt.show()

    elif Menu =="7":
        # X and Y axis for Bar Chart
        YDeath = top10Deaths['TotalDeaths']
        XDeath = top10Deaths['Country/Region']


        #style name
        style.use('ggplot')
        # outter background
        plt.figure(facecolor='#89cff0')
        ax = plt.axes()
        # inner background
        ax.set_facecolor("#899cf0")

        # Bar Chart Data,Width,Labels, Color
        plt.bar(XDeath, YDeath, color ="aqua", width =0.5)
        # X label
        plt.xlabel('Country')
        # Y Label
        plt.ylabel("Covid19 Deaths (millions)")
        # Title
        plt.title("Top 10 Covid19 Deaths In Countries")
        # Show bar Chart
        plt.show()


    elif Menu =="8":
        # X and Y axis for Bar Chart
        YActive = top10Active['ActiveCases']
        XActive = top10Active['Country/Region']

        #style name
        style.use('ggplot')
        # outter background
        plt.figure(facecolor='#89cff0')
        ax = plt.axes()
        # inner background
        ax.set_facecolor("#899cf0")

        # Bar Chart Data,Width,Labels, Color
        plt.bar(XActive, YActive, color ="aqua", width =0.5)
        # X label
        plt.xlabel('Country')
        # Y Label
        plt.ylabel("Active Covid19 (millions)")
        # Title
        plt.title("Top 10 Active Covid19Countries")
        # Show bar Chart
        plt.show()

    elif Menu =="9":

        # Line to write table xlsx file
        top10Recovered.to_excel('top10RecoveredXLSX.xlsx', index=False)

    elif Menu =="10":   

        # Line to write xlsx table file 
        top10Cases.to_excel('top10CasesXLSX.xlsx', index=False)   


    elif Menu =="11":

        # Line to write xlsx table file 
        top10Deaths.to_excel('top10DeathsXLSX.xlsx', index=False)

    elif Menu =="12":

        # Line to write xlsx table file 
        top10Active.to_excel('top10ActiveXLSX.xlsx', index=False)

    elif Menu =="Q":
        # close program
        print("Exited program") 
        break