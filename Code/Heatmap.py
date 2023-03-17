import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# Reading files
covid_df =  pd.read_csv('Data\\country_wise_latest.csv', sep=",").iloc[:,:3]

codes = pd.read_csv("Geo\\all.csv").iloc[:,:4]
# Read shapefile using Geopandas
SHAPEFILE = 'Geo\\ne_10m_admin_0_countries.shp'
geo_df = gpd.read_file(SHAPEFILE)[['ADMIN', 'ADM0_A3', 'geometry']]

# Rename columns.
geo_df.columns = ['country', 'country_code', 'geometry']

# Drop row for 'Antarctica'. It takes a lot of space in the map and is not in the dataset
geo_df = geo_df.drop(geo_df.loc[geo_df['country'] == 'Antarctica'].index)

# Change country code because all.csv and country_wise_latest.csv have it different
geo_df.loc[14, "country_code"] = "SSD"

# Next, we need to ensure that our data matches with the country codes. 
covidcountry = pd.merge(left=codes,right=covid_df,how="left",left_on="name",right_on="Country/Region")
print(covidcountry.loc[covidcountry['name'] == 'Turkmenistan', 'Deaths'].iloc[0])
mergedata = pd.merge(left=geo_df, right=covidcountry, how='inner', left_on='country_code', right_on='alpha-3')

# Preparing to plot
title = 'Total COVID-19 deaths'
col = 'Deaths'
source = 'Kaggle'
vmin = mergedata[col].min()
vmax = mergedata[col].max()
cmap = 'viridis'

plt.figure(figsize=(16, 8))
ax = plt.gca()

ax.axis("off")
ax.set_title(title, fontdict={'fontsize': '25', 'fontweight': '3'})
ax.annotate(source, xy=(0.1, .08), xycoords='figure fraction', horizontalalignment='left', 
            verticalalignment='bottom', fontsize=10)

# Set the color of missing countries to black
mergedata.plot(column=col, edgecolor='none', ax=ax, linewidth=1, cmap=cmap, missing_kwds={'color': 'black'})

# Add a custom legend
handles = [plt.Rectangle((0,0),1,1, color='black', ec="k", lw=0.7)]
labels = ['Missing from data set']
ax.legend(handles, labels, loc='lower right', framealpha=1)
          
sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=vmin, vmax=vmax), cmap=cmap)
sm._A = []
cbaxes = ax.figure.add_axes([0.15, 0.25, 0.01, 0.4])
cbar = ax.figure.colorbar(sm, cax=cbaxes)

#Showing the plot
plt.show()





