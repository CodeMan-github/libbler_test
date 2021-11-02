class Event(object):

    message = None
    category = None
    person = None
    time = None

    def __init__(self, message, category, person, time):
        self.message = message
        self.category = category
        self.person = person
        self.time = time
       
    @staticmethod
    def create(input = ""):
		input = str(input)
		try:
            message, category, person = re.findall('^(.*)\s#(\S*)\s@(\S*)$', input)[0]
            return Event(message, category, person, datetime.datetime.now())
        except IndexError:
            raise ValueError("Invalid event string")
        