from datetime import datetime

class Constructor:
    def __init__(self, obj):
        self.id = obj['constructorId']
        self.name = obj['name']
        self.nationality = obj['nationality']
        self.obj = {
            'id': obj['constructorId'],
            'name': obj['name'],
            'nationality': obj['nationality']
        }

    def to_raw(self):
        return self.obj
