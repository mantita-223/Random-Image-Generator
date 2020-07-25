#! /Users/hobbits/opt/miniconda3/envs/HELLO_WORLD/bin/python

from PIL import Image, ImageDraw
import random
def squares():
	red2 = random.randint(1, 255)
	green2 = random.randint(1, 255)
	blue2 = random.randint(1, 255)
	one = random.randint(1, 100)
	two = random.randint(1, 100)
	three = random.randint(1, 100)
	four = random.randint(1, 100)
	draw = ImageDraw.Draw(img)
	draw.rectangle((one, two, three, four), fill=(red2, green2, blue2))
for i in range(1, 50):
	red = random.randint(1, 255)
	green = random.randint(1, 255)
	blue = random.randint(1, 255)
	img = Image.new('RGB', (60, 30), color = (red, green, blue))
	for i in range(1, 50):
		squares()
	img.save('image' + str(random.randint(1,50)) + '.png')