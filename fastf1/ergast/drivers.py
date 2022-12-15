from fastf1.ergast.api import get
from fastf1.ergast.models.driver import Driver
from fastf1.ergast.results.result import Result

LIMIT = 100
EXCLUDED_INFO_KEYS = ['Drivers']

def drivers():
    return _get_drivers('drivers')

def drivers_for_season(season):
    return _get_drivers(str(season) + '/drivers', { 'season': season })

def drivers_for_season_and_round(season, round):
    filters = { 'season': season, 'round': round }
    return _get_drivers(str(season) + '/' + str(round) + '/drivers', filters)

def driver_info(driver_id):
    return _get_drivers('drivers/' + str(driver_id), { 'driver_id': driver_id })

def _get_drivers(path, filters={}):
    offset = 0
    count = 0
    drivers = []
    result_description = {}

    while True:
        results = get(path, limit=LIMIT, offset=offset)
        if results is not None:
            keys = set(list(results['MRData']['DriverTable'].keys())) - set(EXCLUDED_INFO_KEYS)
            result_description = { k: results['MRData']['DriverTable'][k] for k in keys }
            for driver in results['MRData']['DriverTable']['Drivers']:
                drivers.append(Driver(driver))
        else:
            return None

        offset += LIMIT
        count += len(results['MRData']['DriverTable']['Drivers'])

        if count >= int(results['MRData']['total']): break

    return Result(filters, result_description, drivers)
