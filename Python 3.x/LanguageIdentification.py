import urllib.request
import urllib.parse
import base64

# Authentication
def encodeUserData( user, password ):
	return "Basic " + base64.b64encode( bytes( (user + ":" + password), 'utf-8' ) ).rstrip().decode('utf-8')

def CallAPI( url, params, User, Pass ):
	headers = {
		'Content-type':		'application/x-www-form-urlencoded',
		'Authorization':	encodeUserData( User, Pass )
	}

	data = urllib.parse.urlencode( params )
	data = data.encode( 'utf-8' )

	req = urllib.request.Request( url, data, headers )
	res = urllib.request.urlopen( req )

	CallAPI.n += 1

	print( "Lang #{0}: {1}".format( CallAPI.n, res.read().decode( 'utf-8' ) ) )

CallAPI.n = 0;

def buildParams( txt ):
	return {
		'sid':	'lid-generic',
		'rt':	'text',
		'txt':	txt
	}

url  = 'https://gateway.watsonplatform.net/language-identification-beta/api/v1/txtlid/0'

User = 'fcd411f3-a7d9-4389-ba87-d66c9dfb8e63'
Pass = 'KUjmzTK5grlA'

CallAPI( url, buildParams( 'Hello, how are you?' ), User, Pass )
CallAPI( url, buildParams( 'Hallo, wie geht\'s?' ), User, Pass )
CallAPI( url, buildParams( 'Здравей, как си?' ), User, Pass )

input( 'Done' )
