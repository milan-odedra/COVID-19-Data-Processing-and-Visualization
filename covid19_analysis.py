# Live Feed Covid Data Analysis

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

# New Cases copy
new_cases = confirmed.copy()

# A day subtracted by previous day giving difference in new cases
for day in range(1,  len(confirmed)):
    new_cases.iloc[day] = confirmed.iloc[day] - confirmed.iloc[day - 1]

# Prints the new cases in the space of 10 days
#print(new_cases.tail(10))
#print(confirmed.tail(10))

# Growth rate
growth_rate = confirmed.copy()

# new cases divided by previous day cases showing percentage increase/decrease from day before
for day in range(1, len(confirmed)):
    growth_rate.iloc[day] = (new_cases.iloc[day] / confirmed.iloc[day - 1]) * 100

#print(growth_rate.tail(10))

# Active Cases
active_cases = confirmed.copy()

for day in range(0, len(confirmed)):
    active_cases.iloc[day] = confirmed.iloc[day] - deaths.iloc[day] - recoveries.iloc[day]


overall_growth_rate = confirmed.copy()

for day in range(1, len(confirmed)):
    overall_growth_rate.iloc[day] = ((active_cases.iloc[day] - active_cases.iloc[day - 1]) / active_cases.iloc[day-1]) * 100

print(overall_growth_rate.tail(10))

