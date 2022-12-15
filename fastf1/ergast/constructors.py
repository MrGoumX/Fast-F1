from fastf1.ergast.api import get
from fastf1.ergast.models.constructor import Constructor
from fastf1.ergast.results.result import Result

LIMIT = 100
EXCLUDED_INFO_KEYS = ['Constructors']

def constructors():
    return _get_constructors('constructors')

def constructors_for_season(season):
    return _get_constructors(str(season) + '/constructors', { 'season': season })

def constructors_for_season_and_round(season, round):
    filters = { 'season': season, 'round': round }
    return _get_constructors(str(season) + '/' + str(round) + '/constructors', filters)

def constructor_info(constructor_id):
    return _get_constructors('constructors/' + str(constructor_id), { 'constructor_id': constructor_id })

def _get_constructors(path, filters={}):
    offset = 0
    count = 0
    constructors = []
    result_description = {}

    while True:
        results = get(path, limit=LIMIT, offset=offset)
        if results is not None:
            keys = set(list(results['MRData']['ConstructorTable'].keys())) - set(EXCLUDED_INFO_KEYS)
            result_description = { k: results['MRData']['ConstructorTable'][k] for k in keys }
            for constructor in results['MRData']['ConstructorTable']['Constructors']:
                constructors.append(Constructor(constructor))
        else:
            return None

        offset += LIMIT
        count += len(results['MRData']['ConstructorTable']['Constructors'])

        if count >= int(results['MRData']['total']): break

    return Result(filters, result_description, constructors)
