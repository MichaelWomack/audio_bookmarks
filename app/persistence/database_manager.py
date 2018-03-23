import psycopg2
from contextlib import ContextDecorator
from app.config import Config


class ConnectionManager( ContextDecorator ):

	def __init__( self, config: Config = None ):
		self.config = config

	def __enter__( self ):
		self.conn = psycopg2.connect( **self.config.db_config )
		return self.conn

	def __exit__( self, *exc ):
		self.conn.close()
		return

