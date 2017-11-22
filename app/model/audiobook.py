from app.model.base.json_serializable import JsonSerializable


class AudioBook( JsonSerializable ):
	def __init__( self, **kwargs ):
		self._id = kwargs.get( 'id', None )
		self._user_id = kwargs.get( 'userId', None )
		self._name = kwargs.get( 'name', None )
		self._author = kwargs.get( 'author', None )
		self._publish_year = kwargs.get( 'publishYear', None )



	@property
	def id( self ):
		return self._id



	@property
	def user_id( self ):
		return self._user_id



	@property
	def name( self ):
		return self._name



	@property
	def author( self ):
		return self._author



	@property
	def publish_year( self ):
		return self._publish_year



	def json( self ):
		json = {
			'id': self.id,
			'userId': self.user_id,
			'name': self.name,
			'author': self.author,
			'publishYear': self.publish_year,
		}

		return { k : json[ k ] for k in json.keys() if json[ k ] }



	def __repr__( self ):
		return 'AudioBook({})'.format( self.json() )


if __name__ == '__main__':
	a1 = AudioBook( name='The Intelligent Investor', author='Benjamin Graham', publishYear=1932 )
	print( a1 )
