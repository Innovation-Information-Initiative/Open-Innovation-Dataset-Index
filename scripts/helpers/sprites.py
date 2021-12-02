# heavily adapted from a tutorial by Eric Davidson
import random
import sys
from PIL import (Image, ImageDraw)

r = lambda: random.randint(50,215)
rc = lambda: (r(), r(), r())

listSym = []

def create_square(border, draw, randColor, element, size):
	if (element == int(size/2)):
		draw.rectangle(border, randColor)
	elif (len(listSym) == element+1):
		draw.rectangle(border,listSym.pop())
	else:
		listSym.append(randColor)
		draw.rectangle(border, randColor)

def draw_sprite(border, draw, size):  
	x0, y0, x1, y1 = border
	squareSize = (x1-x0)/size
	randColors = [rc(), rc(), rc(), (255,255,255), (255,255,255), (255,255,255)]
	i = 1
	for y in range(0, size):
		i *= -1
		element = 0
		for x in range(0, size):
			topLeftX = x*squareSize + x0
			topLeftY = y*squareSize + y0
			botRightX = topLeftX + squareSize
			botRightY = topLeftY + squareSize

			create_square((topLeftX, topLeftY, botRightX, botRightY), draw, random.choice(randColors), element, size)
			if (element == int(size/2) or element == 0):  
				i *= -1
				element += i

def create_sprites(uuids):
	print('uuids length is', len(uuids))
	size = 7
	imgSize = 150
	origDimension = imgSize
	padding = imgSize/size
	topLeftX = padding/2
	topLeftY = padding/2
	botRightX = topLeftX + imgSize - padding
	botRightY = topLeftY + imgSize - padding

	for uuid in uuids:
		origImage = Image.new('RGB', (origDimension, origDimension), (255, 255, 255))  
		draw = ImageDraw.Draw(origImage)
		draw_sprite((topLeftX, topLeftY, botRightX, botRightY), draw, size)
		origImage.save("app/assets/thumbnails/" + uuid + ".png")

