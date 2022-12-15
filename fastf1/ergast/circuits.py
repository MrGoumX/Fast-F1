from fastf1.ergast.api import get
from fastf1.ergast.models.circuit import Circuit
from fastf1.ergast.results.result import Result

LIMIT = 100
EXCLUDED_INFO_KEYS = ['Circuits']

def circuits():
    return _get_circuits('circuits')

def circuits_for_season(season):
    return _get_circuits(str(season) + '/circuits', { 'season': season })

def circuits_for_season_and_round(season, round):
    filters = { 'season': season, 'round': round }
    return _get_circuits(str(season) + '/' + str(round) + '/circuits', filters)

def circuit_info(circuit_id):
    return _get_circuits('circuits/' + str(circuit_id), { 'circuit_id': circuit_id })

def _get_circuits(path, filters={}):
    offset = 0
    count = 0
    circuits = []
    result_description = {}

    while True:
        results = get(path, limit=LIMIT, offset=offset)
        if results is not None:
            keys = set(list(results['MRData']['CircuitTable'].keys())) - set(EXCLUDED_INFO_KEYS)
            result_description = { k: results['MRData']['CircuitTable'][k] for k in keys }
            for circuit in results['MRData']['CircuitTable']['Circuits']:
                circuits.append(Circuit(circuit))
        else:
            return None

        offset += LIMIT
        count += len(results['MRData']['CircuitTable']['Circuits'])

        if count >= int(results['MRData']['total']): break

    return Result(filters, result_description, circuits)
