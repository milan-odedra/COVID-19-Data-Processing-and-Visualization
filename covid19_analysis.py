import pandas as pd
import matplotlib as plt

confirmed = pd.read_csv('covid19_confirmed.csv')
deaths = pd.read_csv('covid19_deaths.csv')
recoveries = pd.read_csv('covid19_recoveries.csv')

confirmed = confirmed.drop(['Province/State', 'Lat', 'Long'], axis=1)

confirmed = confirmed.groupby(confirmed['Country/Region']).aggregate('sum')
deaths = confirmed.groupby(deaths['Country/Region']).aggregate('sum')
recoveries = confirmed.groupby(recoveries['Country/Region']).aggregate('sum')

print(confirmed)

