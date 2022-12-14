from datetime import datetime

class Driver:
    def __init__(self, obj):
        self.id = obj['driverId']
        self.name = obj['givenName']
        self.surname = obj['familyName']
        self.date_of_birth = datetime.strptime(obj['dateOfBirth'], '%Y-%m-%d').date()
        self.nationality = obj['nationality']
        self.permanent_number = obj['permanentNumber']
        self.code = obj['code']
        self.obj = {
            'id': obj['driverId'],
            'name': obj['givenName'],
            'surname': obj['familyName'],
            'date_of_birth': obj['dateOfBirth'],
            'nationality': obj['nationality'],
            'permanent_number': obj['permanentNumber'],
            'code': obj['code']
        }

    def to_raw(self):
        return self.obj
