from .event import Event

class EventManager(object):

    events = []

    def __init__(self, events = []):
        self.events = events
        
    def append(self, event):
        if(not isinstance(event, Event)):
            raise TypeError("Invalid Event");
            
        self.events.append(event)
        
    def get_latest(self, count):
        return self.events[-int(count):]
        
    def get_by_category(self, category):
        return [event for event in self.events if event.category == str(category)]
        
    def get_by_person(self, person):
        return [event for event in self.events if event.person == str(person)]
        
    def get_by_date_range(self, time_from, time_to):
        return [event for event in self.events if time_from <= event.time and event.time <= time_to]
        
    def get_by(self, filter):
        filter_type = filter.type
        value = filter.value

        if (filter_type == "category"):
            return self.get_by_category(value)
        elif (filter_type == "person"):
            return self.get_by_person(value)
        elif (filter_type =="time"):
            return self.get_by_date_range(value)
        elif (filter_type == "latest"):
            return self.get_latest(10)
        else:
            raise ValueError("Invalid filter")
            
    def get_10_latest(self, filter):
        events_filtered = self.get_by(filter)
        return events_filtered[-10:]
        