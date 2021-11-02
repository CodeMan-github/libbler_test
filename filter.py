from datetime import datetime

class Filter(object):

    def __init__(self, type, value):
        self.type = type
        self.value = value

    @staticmethod
    def create(input = ""):
        input = str(input)
        if (input.startswith("#")):
            type = "category"
            value = input[1:]
        elif (input.startswith("@")):
            type = "person"
            value = input[1:]
        elif (input == ""):
            type = "latest"
            value = ""
        else:
            parts = input.split(" ")
            if(len(parts) != 2):
                raise ValueError("Invalid time filter")
            type = "time"
            time_from = datetime.strptime(parts[0], "%Y-%m-%d_%H:%M")
            time_to = datetime.strptime(parts[1], "%Y-%m-%d_%H:%M")
            value =[time_from, time_to]

        return Filter(type, value)
		