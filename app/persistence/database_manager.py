import psycopg2
from contextlib import ContextDecorator


class ConnectionManager( ContextDecorator ):

	def __init__( self, config ):
		self.config = config

	def __enter__( self ):
		self.conn = psycopg2.connect( **self.config )
		return self.conn

	def __exit__( self, *exc ):
		self.conn.close()
		return

