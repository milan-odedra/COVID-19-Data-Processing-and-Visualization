# covid19 Vaccine dataset | Covid Year 2021-2022

# Import Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# read data into pandas
df=pd.read_csv('country_vaccinations.csv')

# prints first five columns of dataset
print(df.head())

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

# remove uneeded data and keep mostly vaccine relevant data
df.drop(["people_fully_vaccinated","daily_vaccinations_raw","people_fully_vaccinated_per_hundred",
         "daily_vaccinations_per_million","people_vaccinated_per_hundred", "source_name","source_website"],axis=1, inplace=True)

# Vaccine Data for India (Bharat)

# Save India data in a first dataframe
df_India = df[df["iso_code"] == 'IND'].copy()
print(df_India)

# drop data which is null
df_India.drop(df_India.index[df_India['total_vaccinations'] == 0], inplace = True)

# Plot the total vacinations as a data function
plt.figure(figsize=(18,6))
sns.lineplot(data=df_India, x="date", y="total_vaccinations")
plt.title("Total number of Vaccinations - India")
plt.show()

# Plot daily vaccionations as a data function
plt.figure(figsize=(18,6))
sns.lineplot(data=df_India, x="date", y="daily_vaccinations")
plt.title("Daily number of Vaccinations - India")
plt.xticks(rotation=90)
plt.show()


# ___________________________

# Vaccine data for United Kingdom

# Save United Kingdom data into second dataframe
df_GBR = df[df["iso_code"] == 'GBR'].copy()
df_GBR

# Drop the dates with values equal to 0
df_GBR.drop(df_GBR.index[df_GBR['total_vaccinations'] == 0], inplace = True)

# Plot the total number of vaccinations for UK
plt.figure(figsize=(18,6))
sns.lineplot(data=df_GBR, x="date", y="total_vaccinations")
plt.title("Total vaccinations in the UK")
plt.xticks(rotation=45)
plt.show()

# Plot daily vaccinations as a data function

plt.figure(figsize=(18,6))
sns.lineplot(data=df_GBR, x="date", y="daily_vaccinations")
plt.title("Daily number of Vaccinations - United Kingdom")
plt.xticks(rotation=90)
plt.show()

# _______________________

# World Vaccine data
# Group the data to show total vaccinations by countries and sort decending to show top 10 countries
vaccines_per_country = df.groupby('country').max().sort_values('total_vaccinations', ascending=False)
vaccines_per_country = vaccines_per_country.iloc[:10]
print(vaccines_per_country)

# Countries total vaccinations
plt.figure(figsize=(18,6))
plt.bar(vaccines_per_country.index, vaccines_per_country.total_vaccinations)
plt.title('Total vaccinations per country')
plt.xticks(rotation = 90)
plt.ylabel('Total vaccinations')
plt.xlabel('Country')
plt.show()

# Sort total vaccinations per 100 people
vaccines_per_country = vaccines_per_country.sort_values('total_vaccinations_per_hundred', ascending=False)
print(vaccines_per_country)


# plot bar chart of vaccines per houndred poeple 
plt.figure(figsize=(18,6))
plt.bar(vaccines_per_country.index, vaccines_per_country.total_vaccinations_per_hundred)
plt.title('Vaccinations per 100 people')
plt.xticks(rotation = 90)
plt.ylabel('Vaccinations per 100')
plt.xlabel('Country')
plt.show()

# Sort total number of vaccinations delivered by countries and group by vaccine names
vacc_names_by_country = df.groupby('vaccines').max().sort_values('total_vaccinations', ascending=False)
vacc_names_by_country.head()
print(vacc_names_by_country)

# Print top 10 vaccines by country
vacc_names_by_country = vacc_names_by_country.iloc[:10]
print(vacc_names_by_country)

# Reset index 
vacc_names_by_country=vacc_names_by_country.reset_index()
print(vacc_names_by_country)

# plot bar chart to show which vaccines are being taken the most
plt.figure(figsize=(12,8))
sns.barplot(data = vacc_names_by_country, x='vaccines', y = 'total_vaccinations', hue= 'country', dodge=False)
plt.xticks(rotation=90)

# Plot choropleth showing vaccination data across the world
fig = px.choropleth(df.reset_index(), locations="iso_code",
                    color="total_vaccinations_per_hundred",
                    color_continuous_scale=px.colors.sequential.Electric,
                   title= "Total vaccinations per 100")

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})  #No margin on left, right, top and bottom
fig.show()



