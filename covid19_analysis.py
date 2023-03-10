# Live Feed Covid Data Analysis

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

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

# New and confirmed cases
#print(new_cases.tail(10))
#print(confirmed.tail(10))

# Growth rate
growth_rate = confirmed.copy()

# new cases divided by previous day cases showing percentage increase/decrease from day before
for day in range(1, len(confirmed)):
    growth_rate.iloc[day] = (new_cases.iloc[day] / confirmed.iloc[day - 1]) * 100

# Percentage of growth rate
#print(growth_rate.tail(10))

# Active Cases
active_cases = confirmed.copy()

for day in range(0, len(confirmed)):
    active_cases.iloc[day] = confirmed.iloc[day] - deaths.iloc[day] - recoveries.iloc[day]

# 
overall_growth_rate = confirmed.copy()

for day in range(1, len(confirmed)):
    overall_growth_rate.iloc[day] = ((active_cases.iloc[day] - active_cases.iloc[day - 1]) / active_cases.iloc[day-1]) * 100

# Active cases compared to growth rate
print(overall_growth_rate.tail(10))      # Add specfic countries data

# Death per confirmed infections 
death_rate = confirmed.copy()

for day in range(0, len(confirmed)):
    death_rate.iloc[day] = (deaths.iloc[day] / confirmed.iloc[day]) * 100


hospitalization_rate_estimate = 0.05        # change this estimate

# Show what countries need the most hospitlsation
hospitalization_needed = confirmed.copy()

#for day in range(0, len(confirmed)):
#    hospitalization_needed.iloc[day] = active_cases * hospitalization_rate_estimate


# Visualization
    
countries = ['Italy', 'Austria', 'US', 'China', 'India', 'France', 'Spain']

ax = plt.subplot()
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.set_title('Covd-19 - Total Confirmed Cases by Country', color='white')


for country in countries:
    confirmed[country].plot(label=country)

plt.legend(loc='upper left')
plt.show()
