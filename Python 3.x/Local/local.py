import os
from REST.API import SherlockAPI

# Image Recognition Service
imrec = SherlockAPI(
	# Service URL
	url = 'https://gateway.watsonplatform.net/visual-recognition-beta/api',
	# Credentails (User, Pass)
	auth = ( 'b6242a28-6669-48fb-bb66-3792e4cd5ebc', 'x0CdIbEPu0yb' ),
	# REST API Services
	operations = {
		'recognize': {
			'method':	'POST',
			'path':		'/v1/tag/recognize'
		},
		'getlabels': {
			'method': 'GET',
			'path': '/v1/tag/labels'
		}
	} );

# Language Identification Service
langide = SherlockAPI(
	url = 'https://gateway.watsonplatform.net/language-identification-beta/api',
	auth = ( '9724b4b9-1810-47bb-b0b2-b9f2e7aceb8a', 'NpndGDCF1yK1' ),
	operations = {
		'fetchLang': {
			'method':	'POST',
			'path':		'/v1/txtlid/0'
		}
	} );

# Visual Recognition (get labels)
response = imrec.getlabels();
print( 'List of labels: ' + response );

input( 'Press Enter to continue...' );

# Visual Recognition (test image)
files = { 'img_File': open( 'images/test.jpg', 'rb' ) };
response = imrec.recognize( files = files );
print( 'Labels for image: ' + response );

input( 'Press Enter to continue...' );

# Language Identification (recognize language)
response = langide.fetchLang( params = {
	'sid':	'lid-generic',
	'rt':	'text',
	'txt':	'Hi, what\'s up?'
} );

print( 'Language detected: ' + response );

input( 'Done' )