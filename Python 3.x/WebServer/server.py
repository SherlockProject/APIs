# To upload the App to http://imagerecogtest.eu-gb.mybluemix.net:
# --------------------------------------------------------------------------------
# cf api https://api.eu-gb.bluemix.net
# cf login -u bluemix.tester.uos@gmail.com -o bluemix.tester.uos@gmail.com -s dev
# Password: uniosnabrueck1234
# cf push ImageRecogTest -p local/path/to/ImageRecogTest -m 512M
#
# To test locally:
# --------------------------------------------------------------------------------
# Run server.py
# Open http://localhost:4242/
#
# Use the services:
# - http://localhost:4242/getlabels
# - http://localhost:4242/recognize
# - http://localhost:4242/language_recognition
#
# Responses are printed in the Python console

try:
	from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
except ImportError:
	from http.server import SimpleHTTPRequestHandler as Handler
import os
import Web.Server
from REST.API import SherlockAPI

# Change current directory to avoid exposure of control files
os.chdir( 'static' );

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

class RequestHandler( Handler ):
	def do_GET( self ):
		if self.path == '/getlabels':
			response = imrec.getlabels();
			print( response );

			# Redirect to root
			self.path = '/';

		elif self.path == '/recognize':
			files = { 'img_File': open( '../images/test.jpg', 'rb' ) };
			response = imrec.recognize( files = files );
			print( response );

			# Redirect to root
			self.path = '/';

		elif self.path == '/language_recognition':
			response = langide.fetchLang( params = {
				'sid':	'lid-generic',
				'rt':	'text',
				'txt':	'Hi, what\'s up?'
			} );
			print( response );

			# Redirect to root
			self.path = '/';

		return Handler.do_GET( self );

# Start simple HTTP server at port 4242
Web.Server.start( RequestHandler, port = 4242 );