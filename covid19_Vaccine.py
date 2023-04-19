# covid19 Vaccine dataset | Covid Year 2021-2022

# Import Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Menu 
leave=False
while (leave==False):
    df=pd.read_csv('country_vaccinations.csv') # Read Vaccine Data into Pandas

    # Start Sorting Data

    # prints missing values
    print(df.isnull().sum())

    # Fill null values with 0 and drop countries with iso_code = 0
    print(df.fillna(0, inplace = True))
    print(df.drop(df.index[df['iso_code'] == 0], inplace = True))

    df.isnull().sum()

    # show datatypes of columns
    df.info()

    # Change data format
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

    # print the columns names 
    print(df.columns)

    # Drop data not needed for this analysis
    df.drop(["people_fully_vaccinated","daily_vaccinations_raw","people_fully_vaccinated_per_hundred",
            "daily_vaccinations_per_million","people_vaccinated_per_hundred", "source_name","source_website"],axis=1, inplace=True)

    # Vaccine Data for India (Bharat)
    df_India = df[df["iso_code"] == 'IND'].copy()

    # drop data which is null
    df_India.drop(df_India.index[df_India['total_vaccinations'] == 0], inplace = True)

    # ____________________________________________
    
    # Save United Kingdom (GBR) data into second dataframe
    df_GBR = df[df["iso_code"] == 'GBR'].copy()
    df_GBR

    # Drop the dates with values equal to 0
    df_GBR.drop(df_GBR.index[df_GBR['total_vaccinations'] == 0], inplace = True)

    # ___________________________________________________

    # World Vaccine Data

    # Group the data to show total vaccinations by countries and sort decending to show top 10 countries
    vaccines_per_country = df.groupby('country').max().sort_values('total_vaccinations', ascending=False)
    vaccines_per_country = vaccines_per_country.iloc[:10]
    print(vaccines_per_country)

    # Sort total vaccinations per 100 people
    vaccines_per_country = vaccines_per_country.sort_values('total_vaccinations_per_hundred', ascending=False)
    print(vaccines_per_country)

    # Sort total number of vaccinations delivered by countries and group by vaccine names
    vaccination_names_by_country = df.groupby('vaccines').max().sort_values('total_vaccinations', ascending=False)
    vaccination_names_by_country.head()
    print(vaccination_names_by_country)

    # Print top 10 vaccines by country
    vaccination_names_by_country = vaccination_names_by_country.iloc[:10]
    print(vaccination_names_by_country)

    # Reset index 
    vaccination_names_by_country=vaccination_names_by_country.reset_index()
    print(vaccination_names_by_country)

    Menu=str.upper(input("\n1) Print First 5 Rows \n2: Plot india Total Vaccinations \n3: Plot India Daily Vaccinations \n4: Plot UK Total Vaccinations \n5: Plot UK Daily Vaccinations \n6: Plot Total Vaccines By Countries  \n7: Plot Total Vaccines Per 100 People  \n8: Vaccines Taken the Most \n9: Total Vaccines per Hundred (Map) \nQ: Quit \n\nPlease select an option: "))

    if Menu=="1":
        # prints first five columns of dataset
        print(df.head())
    
    elif Menu=="2":
        # Plot the total vacinations as a data function
        plt.figure(figsize=(18,6))
        sns.lineplot(data=df_India, x="date", y="total_vaccinations")
        plt.title("Total number of Vaccinations - India")
        plt.show()

    elif Menu=="3":
        # Plot daily vaccionations as a data function
        plt.figure(figsize=(18,6))
        sns.lineplot(data=df_India, x="date", y="daily_vaccinations")
        plt.title("Daily number of Vaccinations - India")
        plt.xticks(rotation=45)
        plt.show()

    elif Menu=="4":
        # Plot the total number of vaccinations for UK
        plt.figure(figsize=(18,6))
        sns.lineplot(data=df_GBR, x="date", y="total_vaccinations")
        plt.title("Total vaccinations in the UK")
        plt.xticks(rotation=45)
        plt.show()


    elif Menu=="5":
        # Plot daily vaccinations as a data function
        plt.figure(figsize=(18,6))
        sns.lineplot(data=df_GBR, x="date", y="daily_vaccinations")
        plt.title("Daily number of Vaccinations - United Kingdom")
        plt.xticks(rotation=45)
        plt.show() 

    elif Menu=="6":
        # Countries total vaccinations
        plt.figure(figsize=(18,6))
        plt.bar(vaccines_per_country.index, vaccines_per_country.total_vaccinations)
        plt.title('Total vaccinations Per Country')
        plt.xticks(rotation = 45)
        plt.ylabel('Total Vaccinations')
        plt.xlabel('Country')
        plt.show()

    elif Menu=="7":
        # plot bar chart of vaccines per houndred poeple 
        plt.figure(figsize=(18,6))
        plt.bar(vaccines_per_country.index, vaccines_per_country.total_vaccinations_per_hundred)
        plt.xticks(rotation = 45)
        plt.ylabel('Vaccinations per 100 People')
        plt.xlabel('Country')
        plt.show()

    elif Menu=="8":
        # plot bar chart to show which vaccines are being taken the most
        plt.figure(figsize=(12,8))
        plt.title("Most Used Vaccines by Country")
        sns.barplot(data = vaccination_names_by_country, x='vaccines', y = 'total_vaccinations', hue= 'country', dodge=False)
        plt.xticks(rotation=45)
        plt.show()

    elif Menu=="9":
        # Plot choropleth showing vaccination data across the world (loads into browser)
        fig = px.choropleth(df.reset_index(), locations="iso_code",
                            color="total_vaccinations_per_hundred",
                            color_continuous_scale=px.colors.sequential.Electric,
                            title= "Total Vaccinations per 100 People")

        # Set plot layout with no margins on left, right, top, and bottom
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})  
        fig.show()  
    
    elif Menu==('Q'):
        leave=True

    else:
        leave=False
