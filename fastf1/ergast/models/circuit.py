from datetime import datetime

class Circuit:
    def __init__(self, obj):
        self.id = obj['circuitId']
        self.name = obj['circuitName']
        self.location = obj['Location']
        self.lat = obj['Location']['lat']
        self.long = obj['Location']['long']
        self.locality = obj['Location']['locality']
        self.country = obj['Location']['country']
        self.obj = {
            'id': obj['circuitId'],
            'name': obj['circuitName'],
            'lat': obj['Location']['lat'],
            'long': obj['Location']['long'],
            'locality': obj['Location']['locality'],
            'country': obj['Location']['country']
        }

    def to_raw(self):
        return self.obj
