import json
address_points = json.load(open('Address_Points.geojson'))
print(len(address_points['features']))
print(address_points.keys())
print(address_points['features'])


