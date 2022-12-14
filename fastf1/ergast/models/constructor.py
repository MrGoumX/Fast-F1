from datetime import datetime

class Constructor:
    def __init__(self, obj):
        self.id = obj['constructorId']
        self.name = obj['givenName']
        self.nationality = obj['nationality']
        self.obj = {
            'id': obj['driverId'],
            'name': obj['givenName'],
            'nationality': obj['nationality']
        }

    def to_raw(self):
        return self.obj
