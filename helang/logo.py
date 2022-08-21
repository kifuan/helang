from PIL import Image
from time import time


def print_logo(img_width):
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


def print_logo_small():
	print_logo(100)


def print_logo_middle():
	print_logo(130)


def print_logo_big():
	print_logo(180)
