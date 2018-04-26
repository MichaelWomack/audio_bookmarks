from oauth2client.contrib.flask_util import UserOAuth2
import httplib2
import json
from flask import session, current_app


def setup_oauth2() -> UserOAuth2:
	oauth2 = UserOAuth2()
	def _request_user_info( credentials ):
		http = httplib2.Http()
		credentials.authorize( http )
		# resp, content = http.request('https://www.googleapis.com/plus/v1/people/me' )
		resp, content = http.request( 'https://www.googleapis.com/userinfo/v2/me')
		if resp.status != 200:
			current_app.logger.error( "Error while obtaining user profile: \n%s: %s", resp, content )
			return None

		### TODO put this in a datastore ---> Cloud MemoryStore???
		session[ 'profile' ] = json.loads( content.decode( 'utf-8' ) )

	oauth2.scopes = [ 'email', 'profile']
	oauth2.authorize_callback = _request_user_info
	return oauth2
