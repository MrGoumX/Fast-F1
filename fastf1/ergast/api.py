import json
import warnings

from fastf1.api import Cache
from fastf1.version import __version__

base_url = 'https://ergast.com/api/f1'
_headers = {'User-Agent': f'FastF1/{__version__}'}

def get(path, **params):
    return (_parse_json_response(
        Cache.requests_get(base_url + '/' + path + '.json', params=params, headers=_headers))
    )

def _parse_json_response(r):
    if r.status_code == 200:
        return json.loads(r.content.decode('utf-8'))
    else:
        warnings.warn(f"Request returned: {r.status_code}")
        return None