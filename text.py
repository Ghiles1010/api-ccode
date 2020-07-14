def treshold_inv(img, large, long):

	

	for i in range(long):
		for j in range(large):
		
			R = img[i,j][0]
			G = img[i,j][1]
			B = img[i,j][2]
			

			lum = 0.2126 * R + 0.7152 * G + 0.0722 * B

			if lum < 80:

				img[i,j] = (255, 255, 255)
			
			else:
				img[i,j] = (0, 0, 0)

	return img

def treshold(img, large, long):

	

	for i in range(long):
		for j in range(large):
		
			R = img[i,j][0]
			G = img[i,j][1]
			B = img[i,j][2]

			lum = 0.2126 * R + 0.7152 * G + 0.0722 * B

			if lum < 180:

				img[i,j] = (0, 0, 0)
			
			else:
				img[i,j] = (255, 255, 255)
	return img

				













def img2text(imgB, img, large, long):

	import pytesseract as tess
	from PIL import Image
	import numpy as np

	#tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

	tess.pytesseract.tesseract_cmd = r'/app/.apt/usr/bin/tesseract'



	R = 0
	G = 0
	B = 0


	for i in range(long):
		for j in range(large):
			
			#print(i,j)

			R += img[i,j][0]
			G += img[i,j][1]
			B += img[i,j][2]


	size = long*large
	R /= size
	G /= size
	B /= size

	lum = 0.2126 * R + 0.7152 * G + 0.0722 * B

	if lum < 127:
		
		img = treshold_inv(img, large, long)
		
	else:
		img = treshold(img, large, long)
		
	
	text = tess.image_to_string(imgB)

	return text