import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
latitudes = list(data["LAT"])
longitudes = list(data["LON"])
elevations = list(data["ELEV"])

def color_producer(elevation):
    if elevation<1000:
        return "green"
    elif 1000 <= elevation <3000 :
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38,-98],width='100%', height='100%',max_zoom=25,zoom_start=5, tiles="OpenStreetMap")

fgv = folium.FeatureGroup(name= "Volcanoes in USA")
for lt,ln, elv in zip(latitudes,longitudes, elevations):
    #fg.add_child(folium.CircleMarker(location=[lt,ln], radius=5, popup=(folium.Popup(str(elv) + " m",parse_html=True)), icon=folium.Icon(color=color_producer(elv))))
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=5, popup=(folium.Popup(str(elv) + " m",parse_html=True)), fill_color=color_producer(elv), fill = True,color ="grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name = "population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function= lambda x: {"fillColor":"blue" if x["properties"]["POP2005"]<5000000
else "green"  if 5000000 <= x["properties"]["POP2005"] <10000000
else "yellow" if 10000000 <= x["properties"]["POP2005"]<20000000
else "violet" if 20000000 <= x["properties"]["POP2005"]<50000000
 else "red"}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
