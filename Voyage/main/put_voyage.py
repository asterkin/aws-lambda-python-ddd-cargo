"""Store Voyage Schedule."""

from Voyage import Voyages
from matte import PutClient

voyages = PutClient(Voyages)

def put_voyage(voyage, schedule):
    item = {
        'voyage' : voyage,
        'schedule' : schedule
    }
    return voyages.put_item(item)
