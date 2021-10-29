import json
import time

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
# Params: None
# Returns the list of event object
def get_10_last_events():
	return events[:10]
