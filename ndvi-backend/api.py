'''
Author: Davit Kvartskhava

Functionality: This file uses flask to provide an API for the image analysis interface. 
				Given the path to the NIR images, returns NDVI.
'''

import flask
from ndvi import * 
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

OG_IMAGES_PATH = "./og-images/"
NDVI_IMAGES_PATH = "./ndvi-images/"

def isCached(out_file):
	'''
	Checks if the analysis has already been saved to the disk.
	'''
	return os.path.exists(out_file)


@app.route('/nir', methods=['GET'])
def nir():
	filename = OG_IMAGES_PATH+flask.request.args['filename']
	print(filename)
	return flask.send_file(filename, mimetype='image/gif')



@app.route('/ndvi', methods=['GET'])
def ndvi():
	filename = flask.request.args['filename']
	file_stem = filename.split('.')[0]
	out_filename = 'ndvi-{stem}.jpg'.format(stem=file_stem)

	#Add the full paths
	out_filename = NDVI_IMAGES_PATH+out_filename
	filename = OG_IMAGES_PATH+filename

	if(not isCached(out_filename)):
		#If the analysis has not been done previously, convert to NDVI and save to disk.
		ndvi_im = NDVI(filename, output_file=out_filename)
		ndvi_im.convert()


	return flask.send_file(out_filename, mimetype='image/gif')

app.run()