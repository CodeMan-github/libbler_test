import time

"""
event object:
{
	"name": "",
	"category": "",
	"person": "",
	"time": "",
}
"""

# Stores all events
events = []

# Gets the event from the str and stores it to stream memory
# Params:
# str: event string, type: string
# Returns none
def push_new_event(str):
	event = {}
	strs = str.split("#")
	event["name"] = strs[0].rstrip()
	
	cat_person = strs[1].split("@")
	event["category"] = cat_person[0].rstrip()
	event["person"] = cat_person[1]
	event["time"] = time.time()
	
	events.insert(0, event)

# Gets 10 last events from the stream
# Params:
# category: category name to filter, values: "update", "poll", "warn", "", type: string
# person: person name to filter, values: "all", "john", "all-friends", "", type: string
# time: time value to filter, type: float
# Returns the list of event object
def get_10_last_events(category="", person="", time=0):
	if category != "update" and category != "poll" and category != "warn" and category != "":
		print("Invalid category")
		return []
	
	if person != "all" and person != "john" and person != "all-friends" and person != "":
		print("Invalid person")
		return []

	filtered = events
	if category != "":
		filtered = list( filter(lambda evt: (evt["category"] == category), filtered) )

	if person != "":
		filtered = list( filter(lambda evt: (evt["person"] == person), filtered) )

	if time != 0:
		filtered = list( filter(lambda evt: (evt["time"] >= time), filtered) )

	return filtered[:10]
