"""Store Voyage Schedule."""

from Voyage import Voyages

voyages = Voyages.put_client()

def put_voyage(voyage, schedule):
    item = {
        'voyage' : voyage,
        'schedule' : schedule
    }
    return voyages.put_item(item)
