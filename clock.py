class InvalidTimeError(Exception):
    pass


def findAngle(hour, minute):
    if hour>12 or hour<0 or minute>60 or minute<0:
        raise InvalidTimeError("Invalid time provided")
    # angle between minute hand taking 12 as starting
    ang_min = 6*minute
    # angle between hour hand taking 12 as starting
    ang_hour = 30*hour + minute/2
    # answer is absolute difference between both hands
    return abs(ang_hour-ang_min)