import urllib.request
import re
import json

from .exceptions import CyberNetworkException, CyberNotSupportedException


# The strings are got from https://pv.sohu.com/cityjson?ie=utf-8.
_AMERICAN_REGIONS = {
    'UNITED STATES',
    'JAPAN',
}


def _get_region() -> str:
    try:
        req = urllib.request.urlopen('https://www.taobao.com/help/getip.php')
    except Exception as e:
        raise CyberNetworkException(f'failed to request: {e}')
    if req.getcode() != 200:
        raise CyberNetworkException(f'request failed with status code {req.getcode()}')
    content = req.read().decode('utf-8')
    ip_list = re.findall(r'[0-9]+(?:\.[0-9]+){3}', content)
    if not ip_list:
        raise CyberNotSupportedException('failed to resolve IP')
    ip = ip_list[0]

    try:
        req2 = urllib.request.urlopen(f'https://opendata.baidu.com/api.php?query={ip}&co=&resource_id=6006&oe=utf8', )
    except Exception as e:
        raise CyberNetworkException(f'failed to request: {e}')
    if req2.getcode() != 200:
        raise CyberNetworkException(f'request failed with status code {req.getcode()}')
    info = req2.read().decode()
    data = json.loads(info)
    return data['data'][0]['location']


def check_cyberspaces():
    print('Getting your location...')
    region = _get_region()
    print(f'Your location is {region}.')
    if region in _AMERICAN_REGIONS:
        print('Congratulations! You are in the Cyber Spaces!')
    else:
        print('What a pity! It seems that you are not in the Cyber Spaces.')
