import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
from datetime import datetime, timedelta

# data =  pd.read_csv('Data\\full_grouped.csv', sep=",")
# data = data.rename(columns={'WHO Region': 'WHORegion','Country/Region': 'country'})
# data_german = data.query('country == "Germany"')
# data_UK = data.query('country == "United Kingdom"')
# print(data_german)
# plt.plot(data_german["Date"], data_german["Confirmed"], label="German")
# plt.plot(data_UK["Date"], data_UK["Confirmed"], label="UK")

# Reading files
covid_df =  pd.read_csv('Data\\full_grouped.csv', sep=",")
codes = pd.read_csv("Geo\\all.csv")

#Which Country names are different
codes["name"]
covid_df["Country/Region"]


# covid_df = pd.DataFrame(covid)
# covid_df.head(3)
# print(covid_df)

SHAPEFILE = 'Geo\\ne_10m_admin_0_countries.shp'
# Read shapefile using Geopandas
geo_df = gpd.read_file(SHAPEFILE)[['ADMIN', 'ADM0_A3', 'geometry']]
#print(geo_df)
# Rename columns.
geo_df.columns = ['country', 'country_code', 'geometry']
# print(geo_df.head(3))
# Drop row for 'Antarctica'. It takes a lot of space in the map and is not of much use
geo_df = geo_df.drop(geo_df.loc[geo_df['country'] == 'Antarctica'].index)
# Print the map
geo_df.plot(edgecolor='white', linewidth=1, color='lightblue')

# Next, we need to ensure that our data matches with the country codes. 


covidcountry = pd.merge(left=codes,right=covid_df,how="inner",left_on="name",right_on="Country/Region")

covidcountryNotMatched = pd.merge(left=codes,right=covid_df,how="outer",left_on="name",right_on="Country/Region")
print(covidcountryNotMatched)

#mergedata = mergedata.rename(columns={'name': 'country','alpha-2': 'iso2_code','alpha-3': 'iso3_code'})
mergedata = pd.merge(left=geo_df, right=covidcountry, how='inner', left_on='country_code', right_on='alpha-3')
#print(mergedata)
# There are some countries for which the converter could not find a country code. 
# We will drop these countries.
# geo_df = geo_df.drop(geo_df.loc[geo_df['iso2_code'] == 'NULL'].index)
#print(geo_df.loc[geo_df['country_code'] == 'NULL'])

# print(mergedata)
title = 'Daily COVID-19 deaths'
col = 'Recovered'
source = 'none'
vmin = mergedata[col].min()
vmax = mergedata[col].max()
cmap = 'viridis'

fig, ax = plt.subplots(1, figsize=(20, 8))

ax.axis('off')
mergedata.plot(column=col,edgecolor='0.8', ax=ax, linewidth=1, cmap=cmap)
ax.set_title(title, fontdict={'fontsize': '25', 'fontweight': '3'})
ax.annotate(source, xy=(0.1, .08), xycoords='figure fraction', horizontalalignment='left', 
            verticalalignment='bottom', fontsize=10)
            
sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=vmin, vmax=vmax), cmap=cmap)
sm._A = []
cbaxes = fig.add_axes([0.15, 0.25, 0.01, 0.4])
cbar = fig.colorbar(sm, cax=cbaxes)

plt.show()

# #TTTTTTTTTTTTTTTTTTOOOOOOOOOOOOOOOOOOOOOODDDDDDDDDDDDDDDDDDDDDDDDOOOOOOOOOOOOOOOOOOOOOOOOO:
# #First merge all.csv and geo_df and then covid data