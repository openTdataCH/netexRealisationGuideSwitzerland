# Journeys passing midnight
  > [!CAUTION] 
  > **TODO** when using passingTimes: elements are called ArrivalDayOffset, DepartureDayOffset...
  > 
The time format consists only of the hour, minutes (and seconds) of a 24 hour clock, e.g. '23:55:00'. 
Times that pass midnight of the current OperatingDay are marked with a DayOffset element. 
If a ServiceJourney (in a particular Call) starts after midnight, then DayOffset must be set to '1'. 
E.g. when the S1 departs at 00:11 and it belongs to the previous operating day, then DayOffset is 1.

