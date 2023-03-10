# Import Libraries
import pandas as pd
import matplotlib as plt

# Read data files
confirmed = pd.read_csv('covid19_confirmed.csv')
deaths = pd.read_csv('covid19_deaths.csv')
recoveries = pd.read_csv('covid19_recoveries.csv')

# Shows data for specfic columns 
confirmed = confirmed.drop(['Province/State', 'Lat', 'Long'], axis=1)
deaths = deaths.drop(['Province/State', 'Lat', 'Long'], axis=1)
recoveries = recoveries.drop(['Province/State', 'Lat', 'Long'], axis=1)

# Group the data by countries/regions and sum the data
confirmed = confirmed.groupby(confirmed['Country/Region']).aggregate('sum')
deaths = deaths.groupby(deaths['Country/Region']).aggregate('sum')
recoveries = recoveries.groupby(recoveries['Country/Region']).aggregate('sum')

# returns transposed data 
confirmed = confirmed.T
deaths = deaths.T
recoveries = recoveries.T 




# print(deaths)
# print(recoveries)

