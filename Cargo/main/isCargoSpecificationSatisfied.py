"""Check whether Cargo Specification is satisfied by Itinerary."""

from nahash import jso

def isSatisfied(specification, itinerary):
    if not specification: return False
    elif not itinerary or len(itinerary) == 0: return False
    start = itinerary[0]
    finish = itinerary[-1]

    return specification.origin == start.loadLocation and specification.destination == finish.unloadLocation and specification.arrivalDeadline >= finish.unloadTime

def lambda_handler(input, context):
    jsinp = jso(input)
    return isSatisfied(jsinp.specification, jsinp.itinerary)