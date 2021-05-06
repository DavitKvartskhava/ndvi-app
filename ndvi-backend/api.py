'''
Author: Davit Kvartskhava

Functionality: This file uses flask to provide an API for the image analysis interface. 
				Given the path to the NIR images, returns NDVI.
'''

import flask
from img_scripts import NDVI, VARI, TGI
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

OG_IMAGES_PATH = "./og-images/"
PR_IMAGES_PATH = "./processed-images/"

def prepare_image(filename, analysis_type):

	file_stem = filename.split('.')[0]
	out_filename = '{type}-{stem}.jpg'.format(stem=file_stem, type=analysis_type)


	#Add the full paths
	out_filename = PR_IMAGES_PATH+out_filename
	filename = OG_IMAGES_PATH+filename

	if(not file_exists(filename)):
		return '404.jpeg'

	if(not file_exists(out_filename)):
		#If the analysis has not been done previously, process according to analysis_type and save to disk.
		if(analysis_type=='ndvi'):
			ndvi_im = NDVI(filename, output_file=out_filename)
			ndvi_im.convert()
		elif(analysis_type=='vari'):
			vari_im = VARI(filename, output_file=out_filename)
			vari_im.convert_VARI()
		elif(analysis_type=='tgi'):
			tgi_im = TGI(filename, output_file=out_filename)
			tgi_im.convert_TGI()


	return out_filename

def file_exists(out_file):
	'''
	Checks if the analysis has already been saved to the disk.
	'''
	return os.path.exists(out_file)


@app.route('/nir', methods=['GET'])
def nir():
	filename = OG_IMAGES_PATH+flask.request.args['filename']
	if(not file_exists(filename)):
		filename = '404.jpeg'
	return flask.send_file(filename, mimetype='image/gif')

@app.route('/ndvi', methods=['GET'])
def ndvi():
	out_filename = prepare_image(flask.request.args['filename'], 'ndvi')
	return flask.send_file(out_filename, mimetype='image/gif')

@app.route('/tgi', methods=['GET'])
def tgi():
	out_filename = prepare_image(flask.request.args['filename'], 'tgi')
	return flask.send_file(out_filename, mimetype='image/gif')

@app.route('/vari', methods=['GET'])
def vari():
	out_filename = prepare_image(flask.request.args['filename'], 'vari')
	return flask.send_file(out_filename, mimetype='image/gif')


app.run()