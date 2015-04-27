from . import requests

class SherlockAPI:
	def __init__( self, **kwargs ):
		self.auth		= kwargs['auth'];
		self.api_url	= kwargs['url'];

		for name, obj in kwargs['operations'].items():
			def request(
				self,
				method = obj['method'],
				path = obj['path'],
				headers = None,
				params = None,
				files = None,
				json = None,
				name = name
			):
				response = requests.request(
					method,
					self.api_url + path,
					auth = self.auth,
					params = params,
					files = files,
					json = json );

				return response.content.decode( 'utf-8' );

			setattr( SherlockAPI, name, request );