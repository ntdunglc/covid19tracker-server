API
===
/place/autocomplete
-------------------
Description: used in Reporting page. Users manually type a location, the app try to suggest a list of closeby locations
```
Input:
   - search_query: for eg "Walm", "Walmart", "Targ", "Target"
   - current_location: circle_bound/rectangle_bound 
Output:
    - locations:
        - id:
        - name
        - address
        - lat/long
```

Suggestion:  
1. [Notinatim](https://nominatim.org/release-docs/develop/api/Search/): the below API doesn't respect viewbox, if user specify the city name, it looks correct, but without city name, it can return results all over places
```
http "https://nominatim.openstreetmap.org/search/shoprite, stamford?format=json&viewbox=-73.61029,41.06835,-73.43124,41.00361"
HTTP/1.1 200 OK
Access-Control-Allow-Methods: OPTIONS,GET
Access-Control-Allow-Origin: *
Connection: Upgrade, close
Content-Type: application/json; charset=UTF-8
Date: Sat, 14 Mar 2020 15:39:39 GMT
Expect-CT: max-age=0, report-uri="https://openstreetmap.report-uri.com/r/d/ct/reportOnly"
Server: Apache/2.4.29 (Ubuntu)
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Transfer-Encoding: chunked
Upgrade: h2

[
    {
        "boundingbox": [
            "41.047829",
            "41.0487889",
            "-73.5238003",
            "-73.5231102"
        ],
        "class": "shop",
        "display_name": "ShopRite, 200, Shippan Avenue, South End, Stamford, Fairfield, Connecticut, 06902, United States of America",
        "icon": "https://nominatim.openstreetmap.org/images/mapicons/shopping_supermarket.p.20.png",
        "importance": 0.201,
        "lat": "41.0482863",
        "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "lon": "-73.52346130991681",
        "osm_id": 164927474,
        "osm_type": "way",
        "place_id": 125376233,
        "type": "supermarket"
    },
    ....
```
2. [photon](https://github.com/komoot/photon): it support both search by a center, and search by viewbox
```
http "http://photon.komoot.de/api?q=shoprite, stamford&lat=41.063678&lon=-73.5418142"
HTTP/1.1 200 OK
Access-Control-Allow-Headers: *
Access-Control-Allow-Origin: *
Access-Control-Request-Method: get
Connection: keep-alive
Content-Encoding: gzip
Content-Type: application/json
Date: Sat, 14 Mar 2020 16:01:24 GMT
Server: nginx/1.9.3 (Ubuntu)
Transfer-Encoding: chunked

{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    -73.52346130991681,
                    41.0482863
                ],
                "type": "Point"
            },
            "properties": {
                "city": "Stamford",
                "country": "United States of America",
                "extent": [
                    -73.5238003,
                    41.0487889,
                    -73.5231102,
                    41.047829
                ],
                "housenumber": "200",
                "name": "ShopRite",
                "osm_id": 164927474,
                "osm_key": "shop",
                "osm_type": "W",
                "osm_value": "supermarket",
                "postcode": "06902",
                "state": "Connecticut",
                "street": "Shippan Avenue"
            },
            "type": "Feature"
        },
```
```
http "http://photon.komoot.de/api?q=shoprite&bbox=-73.61029,41.06835,-73.43124,41.00361"
...output is the same...
```

/geolocation
-----------
Description: convert (lat/long) -> address/place. Used to suggest a address/place when user manually mark a location in map. Also used to auto-suggest a list of locations from location tracking
```
Input:
    - lat
    - long
Output:
    - id
    - addresss
    - name (optional)
```

Curent solutions:  
[Notinatim](https://nominatim.org/release-docs/develop/api/Reverse/): will need to double check the accuracy for unknown/no-name location. It seems to try too much to map to an existing place, instead of simple return address.
```
http "https://nominatim.openstreetmap.org/reverse?lat=41.0482863&lon=-73.52346130991681&format=json"
HTTP/1.1 200 OK
Access-Control-Allow-Methods: OPTIONS,GET
Access-Control-Allow-Origin: *
Connection: Upgrade, close
Content-Type: application/json; charset=UTF-8
Date: Sat, 14 Mar 2020 15:44:33 GMT
Expect-CT: max-age=0, report-uri="https://openstreetmap.report-uri.com/r/d/ct/reportOnly"
Server: Apache/2.4.29 (Ubuntu)
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Transfer-Encoding: chunked
Upgrade: h2

{
    "address": {
        "city": "Stamford",
        "country": "United States of America",
        "country_code": "us",
        "county": "Fairfield",
        "hamlet": "South End",
        "house_number": "200",
        "postcode": "06902",
        "road": "Shippan Avenue",
        "state": "Connecticut",
        "supermarket": "ShopRite"
    },
    "boundingbox": [
        "41.047829",
        "41.0487889",
        "-73.5238003",
        "-73.5231102"
    ],
    "display_name": "ShopRite, 200, Shippan Avenue, South End, Stamford, Fairfield, Connecticut, 06902, United States of America",
    "lat": "41.0482863",
    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
    "lon": "-73.52346130991681",
    "osm_id": 164927474,
    "osm_type": "way",
    "place_id": 125376233
}

```
2. [photon](https://github.com/komoot/photon): it seems to return similar result
```
http "http://photon.komoot.de/reverse?lat=41.0482863&lon=-73.52346130991681"
HTTP/1.1 200 OK
Access-Control-Allow-Headers: *
Access-Control-Allow-Origin: *
Access-Control-Request-Method: get
Connection: keep-alive
Content-Encoding: gzip
Content-Type: application/json
Date: Sat, 14 Mar 2020 16:14:04 GMT
Server: nginx/1.9.3 (Ubuntu)
Transfer-Encoding: chunked

{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    -73.52346130991681,
                    41.0482863
                ],
                "type": "Point"
            },
            "properties": {
                "city": "Stamford",
                "country": "United States of America",
                "extent": [
                    -73.5238003,
                    41.0487889,
                    -73.5231102,
                    41.047829
                ],
                "housenumber": "200",
                "name": "ShopRite",
                "osm_id": 164927474,
                "osm_key": "shop",
                "osm_type": "W",
                "osm_value": "supermarket",
                "postcode": "06902",
                "state": "Connecticut",
                "street": "Shippan Avenue"
            },
            "type": "Feature"
        }
    ],
    "type": "FeatureCollection"
}
```

/cases/report
-----------
Description: when users get sick, users can report their location history to alert other users. Only authenticated users can use this API
```
Input:
    - user_id: some token in headers
    - locations
        - start_ts: example "2020-03-03T13:00:00Z"
        - end_ts: example "2020-03-03T15:00:00Z"
        - address
        - lat/long
        - name (optional)

Output:
    - status
```

/cases/search
-----------
Description: for user to search reported cases on a map. Users can search by a center point and radius. Optionally user can specify timestamp bound to filter result. Need to anonymize the response, ie dont send reporting user ID
```
Input:
    - address
    - center_lat/center_long
    - radius
    - start_ts (optional): example "2020-03-03T13:00:00Z"
    - end_ts (optional): example "2020-03-03T15:00:00Z"

Output:
    - cases:
        - start_ts: example "2020-03-03T13:00:00Z"
        - end_ts: example "2020-03-03T15:00:00Z"
        - address
        - lat/long
        - name (optional)
        - verified (optional): to distinguish cases from official source vs user report.
```