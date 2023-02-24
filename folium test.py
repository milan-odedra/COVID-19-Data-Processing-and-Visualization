import pandas as pd
import folium
import geopandas as gpd
import csv

covid_df =  pd.read_csv('Data\\full_grouped.csv', sep=",")
SHAPEFILE = 'Geo\\ne_10m_admin_0_countries.shp'
# Read shapefile using Geopandas
geo_df = gpd.read_file(SHAPEFILE)[['ADMIN', 'ADM0_A3', 'geometry']]
geo_df.columns = ['country', 'country_code', 'geometry']
geo_df = geo_df.drop(geo_df.loc[geo_df['country'] == 'Antarctica'].index)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
jason = pd.read_json("Geo\custom.geo.json")
print(world)

#Reaad geo Data and filter on first 3 columns
countryData = pd.read_csv("Geo\\all.csv")
countryData = countryData[["name", "alpha-2","alpha-3"]]
#print(countryData)



covidcountry = pd.merge(left=countryData,right=covid_df,how="inner",left_on="name",right_on="Country/Region")
mergedata = pd.merge(left=geo_df, right=covidcountry, how='inner', left_on='country_code', right_on='alpha-3')
#print(mergedata)

#state_geo = f"{url}/us-states.json"
#state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
#state_data = pd.read_csv(state_unemployment)

m = folium.Map(location=[48, -102], zoom_start=3)

url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
)
state_geo = f"{url}/us-states.json"
state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
state_data = pd.read_csv(state_unemployment)
print(state_data)
state_geo = pd.read_json("Geo2\\Us-State.json")

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(m)

# folium.Choropleth(
#     geo_data=jason,
#     name="choropleth",
#     data=mergedata,
#     columns=["country", "Confirmed"],
#     key_on="feature.id",
#     fill_color="YlGn",
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     legend_name="Covid cases",
# ).add_to(m)

folium.LayerControl().add_to(m)

m.save("tets.html")