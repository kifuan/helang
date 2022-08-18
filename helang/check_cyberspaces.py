import urllib.request
import re
import json

from .exceptions import CyberNetworkException


# The strings is got from https://pv.sohu.com/cityjson?ie=utf-8.
_AMERICAN_REGIONS = {
    'UNITED STATES',
    'JAPAN',
}


def _get_region() -> str:
    try:
        req = urllib.request.urlopen('https://pv.sohu.com/cityjson?ie=utf-8')
    except Exception as e:
        raise CyberNetworkException(f'failed to request: {e}')
    if req.getcode() != 200:
        raise CyberNetworkException(f'request failed with status code {req.getcode()}')
    info = json.loads(re.findall(r'{.+}', req.read().decode())[0])
    return info['cname']


def check_cyberspaces():
    print('Getting your location...')
    region = _get_region()
    print(f'Your location is {region}.')
    if region in _AMERICAN_REGIONS:
        print('Congratulations! You are in the Cyber Spaces!')
    else:
        print('What a pity! It seems that you are not in the Cyber Spaces.')
