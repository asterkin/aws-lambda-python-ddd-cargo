import CargoHandlingEvent

def event_point(event):
    return {
       CargoHandlingEvent.LOAD: 'load',
       CargoHandlingEvent.RECEIVE: 'load' 
    }.get(event.event_type, 'unload')
    
def expected_event(event):
    loc = event_point(event)
    # def p(leg):
    #     print(loc, event, leg[loc])
    #     return event.location == leg[loc].location and event.voyage == leg.voyage
    # return p
    return lambda leg: event.location == leg[loc].location and event.voyage == leg.voyage

class LegObject:
    def __init__(self, leg, it):
        self.leg = leg
        self.it  = it
    def __next__(self):
        l = next(self.it, None)
        return Leg((l, self.it))
    def load(self):
        return CargoHandlingEvent.load(self.leg.load.location, self.leg.voyage, self.leg.load.time)
    def unload(self):
        return CargoHandlingEvent.unload(self.leg.unload.location, self.leg.voyage, self.leg.unload.time)
    def claim(self):
        return CargoHandlingEvent.claim(self.leg.unload.location)
    def is_on_schedule(self, event):
        t = self.leg[event_point(event)].time
        if event.completion_time < t:    return 'AHEAD_OF_SCHEDULE'  
        elif event.completion_time == t: return 'ON_SCHEDULE' 
        else:                            return 'BEHIND_SCHEDULE'
    def is_expected(self, event):
        return expected_event(event)(self.leg)

def Leg(t):
    leg, it = t
    return LegObject(leg, it) if leg else None
