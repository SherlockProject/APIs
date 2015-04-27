try:
	from SocketServer import TCPServer as Server
except ImportError:
	from http.server import HTTPServer as Server
import os

def start( RequestHandler, port = 8000 ):
	port = int( os.getenv( 'VCAP_APP_PORT', port ) );

	httpd = Server( ( "", port ), RequestHandler );
	try:
		print( "Start serving at port %i" % port );
		httpd.serve_forever();
	except KeyboardInterrupt:
		pass;
	httpd.server_close();