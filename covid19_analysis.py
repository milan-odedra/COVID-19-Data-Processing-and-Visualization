import pandas as pd
import matplotlib as plt

confirmed = pd.read_csv('covid19_confirmed.csv')
deaths = pd.read_csv('covid19_deaths.csv')
recoveries = pd.read_csv('covid19_recoveries.csv')

confirmed = confirmed.drop(['Province/State', 'Lat', 'Long'], axis=1)
deaths = deaths.drop(['Province/State', 'Lat', 'Long'], axis=1)
recoveries = recoveries.drop(['Province/State', 'Lat', 'Long'], axis=1)

confirmed = confirmed.groupby(confirmed['Country/Region']).aggregate('sum')
deaths = deaths.groupby(deaths['Country/Region']).aggregate('sum')
recoveries = recoveries.groupby(recoveries['Country/Region']).aggregate('sum')

confirmed = confirmed.T
deaths = deaths.T
recoveries = recoveries.T 

print(deaths)
print(recoveries)

