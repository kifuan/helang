from PIL import Image
from time import time


def _print_logo(img_width: int):
    img_height = int(img_width * 0.55)
    img = Image.open('./logo.png').resize((img_width,img_height), Image.ANTIALIAS)

    ascii_char = list('▓M@$%&Ww(({[+1i<>/!l-  ')
    ascii_charUnit = 257 / len(ascii_char)

    txt = ''
    t = time()

    for h in range(img_height):
        for w in range(img_width):
            color = img.getpixel((w, h)) #Get rgb
            gray = int((0.3334 * color[0] + 0.3333 * color[1] + 0.3333 * color[2]) / ascii_charUnit) #Calculate gray scale
            txt += ascii_char[gray]
        txt += '\n'

    print(txt)
    print(f'=== Generated in {time() - t}s ===')


class LogoSize():
    TINY = 100
    MEDIUM = 130
    LARGE = 180


def print_logo(size: LogoSize):
    _print_logo(size.value)
