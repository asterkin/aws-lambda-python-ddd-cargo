"""Retrieve the most recent event for particular cargo"""

from CargoHandlingEvent import Events

events = Events.query_client()

def get_last(cargo):
    return events.get_last(cargo)
