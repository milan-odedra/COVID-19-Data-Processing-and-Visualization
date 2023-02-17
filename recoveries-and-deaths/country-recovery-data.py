import pandas as pd
import matplotlib.pyplot as plt

confirmed_cases = pd.read_csv('Dataset\Covid-19 Dataset\country_wise_latest.csv')
# countries_recovered = pd.read_csv('country_wise_latest.csv')
# deaths = pd.read_csv('country_wise_latest.csv')

# print(confirmed_cases)
confirmed = confirmed.drop(['Country/Region', 'recovered'])

# confirmed.plot()
# plt.show()
