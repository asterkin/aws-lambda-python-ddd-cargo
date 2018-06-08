"""Store Location Definition."""

from Voyage import Locations

locations = Locations.put_client()

def put_location(location, name):
    item = {
        'location' : locations,
        'name' : name
    }
    return locations.put_item(item)
