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
df_UK = df[df["iso_code"] == 'UK'].copy()
df_UK

# Drop the dates with values equal to 0
df_UK.drop(df_UK.index[df_India['total_vaccinations'] == 0], inplace = True)

# Plot the total number of vaccinations for UK
plt.figure(figsize=(18,6))
sns.lineplot(data=df_UK, x="date", y="total_vaccinations")
plt.title("Total vaccinations in the UK")
plt.xticks(rotation=45)
plt.show

# Plot daily vaccinations as a data function
