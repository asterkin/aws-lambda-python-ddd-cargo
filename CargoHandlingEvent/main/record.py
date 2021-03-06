"""Store CargoHandlingEvent record in database"""

from CargoHandlingEvent import Events, CargoHandlingEvent
import time

events = Events.put_client()

#TODO: non None validation in handler
def record(event):
    item = CargoHandlingEvent(event.cargo, event.event_type, event.location, event.voyage, event.completion_time)
    item['registration_time'] = int(time.time()*1000)
    return events.put_item(item)
