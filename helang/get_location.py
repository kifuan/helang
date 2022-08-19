import requests
import re
import qrcode


def get_location():
    url = "https://www.ip.cn/api/index?ip=&type=0"
    response = requests.get(url)
    return re.split('[ ]+', response.json().get('address'))[1]


def get_qrcode(content: str = '114514'):
    qr = qrcode.QRCode()
    qr.add_data(content)
    img = qr.make_image(fill_color='red')
    img.save('qrcode.png')
