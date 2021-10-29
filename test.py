import json
import time

events = []

# Gets the event from the str and stores it to stream memory
# Params:
# str: event string, type: string
def push_new_event(str):
	event = {}
	strs = str.split("#")
	event["name"] = strs[0].removesuffix(" ")
	
	cat_person = strs[1].split("@")
	event["category"] = cat_person[0].removesuffix(" ")
	event["person"] = cat_person[1]
	event["time"] = time.time()
	
	events.insert(0, event)

# Gets 10 last events from the stream
# Returns the list of event object
def get_10_last_events():
	return events[:10]
	
"""
- it’s possible to get 10 last events from the top of the stream
- - by category (#update, #poll, #warn)
- - by person (@all, @john, @all-friends)
- - by time

I didn't understand this requirement correctly.
Does it require the sorting by category, person or time?
"""