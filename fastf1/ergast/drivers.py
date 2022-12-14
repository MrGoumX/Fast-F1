from fastf1.ergast.api import get

def drivers():
    limit = 100
    offset = 0
    count = 0
    drivers = []
    path = 'drivers'

    while True:
        results = get(path, limit=limit, offset=offset)
        if results is not None:
            for driver in results['MRData']['DriverTable']['Drivers']:
                drivers.append({
                    'id': driver['driverId'],
                    'name': driver['givenName'],
                    'surname': driver['familyName'],
                    'dateOfBirth': driver['dateOfBirth'],
                    'nationality': driver['nationality']
                })
        else:
            return None
        
        offset += limit
        count += len(results['MRData']['DriverTable']['Drivers'])

        if count >= int(results['MRData']['total']): break

    return drivers

def drivers_for_year(year):
    limit = 100
    offset = 0
    count = 0
    drivers = []
    path = str(year) + '/drivers'

    while True:
        results = get(path, limit=limit, offset=offset)
        if results is not None:
            for driver in results['MRData']['DriverTable']['Drivers']:
                drivers.append({
                    'id': driver['driverId'],
                    'name': driver['givenName'],
                    'surname': driver['familyName'],
                    'dateOfBirth': driver['dateOfBirth'],
                    'nationality': driver['nationality']
                })
        else:
            return None
        
        offset += limit
        count += len(results['MRData']['DriverTable']['Drivers'])

        if count >= int(results['MRData']['total']): break

    return drivers

def drivers_for_year_and_round(year, round):
    limit = 100
    offset = 0
    count = 0
    drivers = []
    path = str(year) + '/' + str(round) + '/drivers'

    while True:
        results = get(path, limit=limit, offset=offset)
        if results is not None:
            for driver in results['MRData']['DriverTable']['Drivers']:
                drivers.append({
                    'id': driver['driverId'],
                    'name': driver['givenName'],
                    'surname': driver['familyName'],
                    'dateOfBirth': driver['dateOfBirth'],
                    'nationality': driver['nationality']
                })
        else:
            return None
        
        offset += limit
        count += len(results['MRData']['DriverTable']['Drivers'])

        if count >= int(results['MRData']['total']): break

    return drivers    