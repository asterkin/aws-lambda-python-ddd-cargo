"""Retrieve the most recent event for particular cargo"""

from mattea import QueryClient
from CargoHandlingEvent import Events, CargoHandlingEvent

events = QueryClient(Events)

def getLast(cargo):
    return events.get_last(cargo)
