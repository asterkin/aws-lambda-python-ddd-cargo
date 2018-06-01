"""Store CargoHandlingEvent record in database"""

from mattea import PutClient
from CargoHandlingEvent import Events, CargoHandlingEvent
import time

events = PutClient(Events)

#TODO: non None validation in handler
def record(event):
    item = CargoHandlingEvent(event.cargo, event.eventType, event.location, event.voyage, event.completionTime)
    item['registrationTime'] = int(time.time()*1000)
    return events.put_item(item)
    