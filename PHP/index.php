<?php
	# App Url:	http://lukanovapp.eu-gb.mybluemix.net
	# API Doc:	http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/apis/

	function CallAPI( $method, $url, $data = false, $auth ) {
		$curl = curl_init();

		switch( $method ) {
			case 'POST':
				curl_setopt( $curl, CURLOPT_POST, 1 );

				if( $data )
					curl_setopt( $curl, CURLOPT_POSTFIELDS, $data );
			break;

			case 'PUT':
				curl_setopt($curl, CURLOPT_PUT, 1);
			break;

			default: # GET
				if( $data )
					$url = sprintf( "%s?%s", $url, http_build_query( $data ) );
		}

		# Authentication:
		curl_setopt( $curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC );
		curl_setopt( $curl, CURLOPT_USERPWD, "{$auth['user']}:{$auth['pass']}" );

		curl_setopt( $curl, CURLOPT_URL, $url );
		curl_setopt( $curl, CURLOPT_RETURNTRANSFER, 1 );

		$result = curl_exec( $curl );

		curl_close( $curl );

		return $result;
	}
?><!DOCTYPE html>
<html>
	<head>
		<title>Uni-Osnabrueck Test App (PHP)</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<link rel="stylesheet" href="style.css" />
	</head>

	<body>
		<table>
			<tr>
				<td style='width: 30%;'><img class = 'newappIcon' src='images/newapp-icon.png'>
				</td>
				<td>
					<h1 id = "message">Uni-Osnabrueck Test App</h1>
					<p>
						Welcome to the language-identification test app.
					</p>

					<?php
						$url = 'https://gateway.watsonplatform.net/language-identification-beta/api/v1/txtlid/0';

						$auth = array(
							'user'	=> 'fcd411f3-a7d9-4389-ba87-d66c9dfb8e63',
							'pass'	=> 'KUjmzTK5grlA'
						);

						function param( $txt ) {
							return array(
								'sid'	=> 'lid-generic',
								'rt'	=> 'text',
								'txt'	=> $txt
							);
						}

						$lang1 = CallAPI( 'POST', $url, param( 'Hello, how are you?' ), $auth );
						$lang2 = CallAPI( 'POST', $url, param( 'Hallo, wie geht\'s?' ), $auth );
						$lang3 = CallAPI( 'POST', $url, param( 'Здравей, как си?' ), $auth );

						print <<<LANGS
							Lang #1: {$lang1}<br />
							Lang #2: {$lang2}<br />
							Lang #3: {$lang3}
LANGS;
					?>
				</td>
			</tr>
		</table>
	</body>
</html>
