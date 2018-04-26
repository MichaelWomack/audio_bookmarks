import os
class Config():
	GCP_BUCKET = os.environ[ 'GCP_BUCKET' ]
	AUDIOBOOK_PATH_TEMPLATE = 'users/{user_id}/audiobooks/{audiobook_id}/{file_name}'

	### Database
	DB_CONFIG = {
		'host': os.environ[ 'DB_HOST' ],
		'port': os.environ[ 'DB_PORT' ],
		'dbname': os.environ[ 'DB_NAME' ],
		'user': os.environ[ 'DB_USER' ],
		'password': os.environ[ 'DB_PASSWORD' ]
	}
	### Application Secrets
	SECRET_KEY = os.environ[ 'SECRET_KEY' ]
	GOOGLE_OAUTH2_CLIENT_ID = os.environ[ 'GOOGLE_OAUTH2_CLIENT_ID' ]
	GOOGLE_OAUTH2_CLIENT_SECRET = os.environ[ 'GOOGLE_OAUTH2_CLIENT_SECRET' ]


