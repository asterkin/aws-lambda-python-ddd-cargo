import CargoHandlingEvent

def eventPoint(event):
    return {
       CargoHandlingEvent.LOAD: 'load',
       CargoHandlingEvent.RECEIVE: 'load' 
    }.get(event.eventType, 'unload')
    
def eventLocation(event):
    return eventPoint(event) + 'Location'

def eventTime(event):
    return eventPoint(event) + 'Time'
    
def expectedEvent(event):
    loc = eventLocation(event)
    return lambda leg: event.location == leg[loc] and event.voyage == leg.voyage

class LegObject:
    def __init__(self, leg, it):
        self.leg = leg
        self.it  = it
    def __next__(self):
        l = next(self.it, None)
        return Leg((l, self.it))
    def load(self):
        return CargoHandlingEvent.load(self.leg.loadLocation, self.leg.voyage, self.leg.loadTime)
    def unload(self):
        return CargoHandlingEvent.unload(self.leg.unloadLocation, self.leg.voyage, self.leg.unloadTime)
    def claim(self):
        return CargoHandlingEvent.claim(self.leg.unloadLocation)
    def isOnSchedule(self, event):
        t = self.leg[eventTime(event)]
        if event.completionTime < t:    return 'AHEAD_OF_SCHEDULE'  
        elif event.completionTime == t: return 'ON_SCHEDULE' 
        else:                           return 'BEHIND_SCHEDULE'
    def isExpected(self, event):
        return expectedEvent(event)(self.leg)

def Leg(t):
    leg, it = t
    return LegObject(leg, it) if leg else None
