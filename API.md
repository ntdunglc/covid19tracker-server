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