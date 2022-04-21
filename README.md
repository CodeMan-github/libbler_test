# Event Manager (Python Core)

## Functionality:

### it’s possible to push new event to the top of the stream. Service consumes events in the form of a string like “I just won a lottery #update @all”, parses them to JSON / Object format and stores in memory.

### it’s possible to get 10 last events from the top of the stream
#### by category (#update, #poll, #warn)
#### by person (@all, @john, @all-friends)
#### by time
