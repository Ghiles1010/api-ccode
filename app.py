
from flask import Flask, render_template, request, Response, url_for, redirect, send_file
import text
from PIL import Image
import numpy as np




app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():

	if request.method == "POST":

		if request.files:





			i = request.files['image']



			imgB = Image.open(i)
			imgpx = imgB.load()
			large, long = imgB.size

			return text.img2text(imgB,imgpx, long, large)


	return 'Hello, World!'
	
if __name__ == "__main__":
	
	app.run(debug = True)
