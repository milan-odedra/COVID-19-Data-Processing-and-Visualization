# covid19 Vaccine dataset | Covid Year 2022

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