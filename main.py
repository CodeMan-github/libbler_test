from .filter import Filter
from .event import Event
from .event_manager import EventManager

manager = EventManager()

event = Event.create("I just won a lottery #update @all")
manager.append(event)

filter = Filter.create("#update")
events = manager.get_10_latest(filter)

print(events)
