# Import libraries
import pandas as pd
import geopandas as gpd
import folium

# Load cleaned data
df = pd.read_csv('Data\gtd_cleaned.csv', parse_dates=['date'])

# Convert to GeoDataFrame
df['geometry'] = gpd.points_from_xy(df['lon'], df['lat'])
gdf = gpd.GeoDataFrame(df, crs='epsg:4326', geometry='geometry')

# Create a folium map centered globally
gtd_map = folium.Map(location=[0, 0], zoom_start=2, tiles='CartoDB positron')

# Add points to the map
for _, row in gdf.iterrows():
    
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        popup=folium.Popup(
            f"<strong>Date:</strong> {row['date']}<br>"
            f"<strong>Country:</strong> {row['country']}<br>"
            f"<strong>City:</strong> {row['city']}<br>"
            f"<strong>Attack Type:</strong> {row['attack_type']}<br>"
            f"<strong>Target Type:</strong> {row['target_type']}<br>"
            f"<strong>Weapon Type:</strong> {row['weapon_type']}<br>"
            f"<strong>Killed:</strong> {row['killed']}<br>"
            f"<strong>Wounded:</strong> {row['wounded']}<br>"
            f"<strong>Group Name:</strong> {row['group_name']}<br>",
            max_width=300
        ),
        radius=3,
        icon=folium.Icon(
            color='red' if row['killed'] > 0 else 'blue',
            icon='info-sign')
    ).add_to(gtd_map)

# Save the map to an HTML file
gtd_map.save('Plots/gtd_map.html')

print("Map has been created and saved as 'Plots/gtd_map.html'. You can open this file in a web browser to view the interactive map.")