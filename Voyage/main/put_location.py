"""Store Location Definition."""

from Voyage import Locations
from matte import PutClient

locations = PutClient(Locations)

def put_location(location, name):
    item = {
        'location' : locations,
        'name' : name
    }
    return locations.put_item(item)
