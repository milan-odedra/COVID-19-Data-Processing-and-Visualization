import pandas as pd
import folium
import geopandas as gpd
import csv

df_can = pd.read_excel('Canada.xlsx',skiprows=range(1),skipfooter=2)
df_can.head()
#print(df_can)
#df_can.drop(["AREA","REG","DEV","Type","Coverage"], axis=2, inplace=True)
df_can.rename(columns={"Odname":"Country", "AreaName":"Continent","RegName":"Region"}, inplace=True)
df_can.columns = list(map(str,df_can.columns))
df_can["Total"] = df_can.sum(axis=1)
df_can.head()

world_geo = pd.read_json("Geo2\world-countries.json")
world_map = folium.Map(location=[0,0],zoom_start=2)

print(world_geo)
print(df_can)

gdf_mask = gpd.read_file(
    gpd.datasets.get_path("naturalearth_lowres")
)

interfacegeo = gpd.GeoSeries(data=gdf_mask["geometry"]).__geo_interface__

mask2 = gpd.GeoDataFrame(interfacegeo, crs="EPSG:4326").to_json()

mask2.to_file("Geo2\gpdWorld.json", driver="GeoJSON")  
print(mask2)

world_geo2 = pd.read_json("Geo2\gpdWorld.json")

# folium.Choropleth(
#     geo_data=world_geo2,
#     #name="choropleth",
#     data=df_can,
#     columns=["OdName", "Total"],
#     key_on="feature.properties.name",
#     #threshold_scale=threshold_scale,
#     fill_color="YlOrRd",
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     legend_name="Imigration to Canada",
#     #reset=True
# ).add_to(world_map)
# folium.LayerControl().add_to(world_map)

# world_map.save("testCanada.html")

