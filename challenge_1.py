import json

places = []

while True:
    place = input("Enter a place (or type 'q' to quit): ")
    if place.lower() == 'q':
        break
    places.append(place)

places_json = json.dumps(places, indent=4)

print("\nPlaces entered:")
print(places_json)
