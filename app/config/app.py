import configparser
import os

from pkg_resources import resource_filename


class Config():

	def __init__( self, env=None ):
		if not env or env.lower() not in ('test', 'np', 'pr'):
			self.env = os.environ.get( 'ABM_LCP', 'NP' ).lower()
		else:
			self.env = env.lower()

		config = configparser.ConfigParser()
		config_file_path = resource_filename( 'app.resources.conf', '{}.ini'.format( self.env ) )
		config.read( config_file_path )

		# TODO use environment variables for all db config and GCP project specific items
		self.db_config = {
			'host': config[ 'database' ][ 'host' ],
			'port': config[ 'database' ][ 'port' ],
			'dbname': config[ 'database' ][ 'dbname' ],
			'user': config[ 'database' ][ 'user' ],
			'password': config[ 'database' ][ 'password' ]
		}

		self.api_key = config[ 'google' ][ 'books_api_key' ]
		self.storage_bucket = config[ 'google' ][ 'storage_bucket' ]
