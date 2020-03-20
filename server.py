from fastapi import FastAPI
from arcgis.gis import GIS
from arcgis.geocoding import geocode, reverse_geocode
import pprint
import firebase_admin
pp = pprint.PrettyPrinter(indent=4)

app = FastAPI()
gis = GIS()
default_app = firebase_admin.initialize_app()
            
@app.get("/place/autocomplete/{search_query}/{current_location}")
def autocomplete(search_query:str, current_location:str):
    geocode_result = geocode(address=search_query, as_featureset=True,search_extent=current_location)
    places = []
    for place in geocode_result.features:
        places.append({
            'name':place.attributes['PlaceName'],
            'address': place.attributes['Place_addr'],
            'lat': place.geometry.y,
            'long': place.geometry.x
            })
    return places

@app.get("/geolocation/{lat}/{long}")
def geolocation(lat:float, long:float):
    results = reverse_geocode([long, lat])
    if results:
        print(results)
        return {
            'name' : results['address']['LongLabel'],
            'address': results['address']['Address'],
        }
    return {}