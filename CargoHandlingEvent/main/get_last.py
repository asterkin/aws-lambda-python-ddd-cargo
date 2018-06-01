"""Retrieve the most recent event for particular cargo"""

from matte import QueryClient
from CargoHandlingEvent import Events, CargoHandlingEvent

events = QueryClient(Events)

def get_last(cargo):
    return events.get_last(cargo)
