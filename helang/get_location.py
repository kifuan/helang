import json
from urllib import request
import re
import qrcode


def get_location():
    def get_location():
        url = "https://www.ip.cn/api/index?ip=&type=0"
        header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
        req = request.Request(url, headers=header, method='GET')
        response = request.urlopen(req)
        res = response.read().decode('utf8')
        return re.split('[ ]+', json.loads(res)['address'])[1]


def get_qrcode(content: str = '114514'):
    qr = qrcode.QRCode()
    qr.add_data(content)
    img = qr.make_image(fill_color='red')
    img.save('qrcode.png')
