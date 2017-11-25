from app.model.base import JsonSerializable


class AudioBook( JsonSerializable ):


	def __init__( self, **kwargs ):
		self._id = kwargs.get( 'id', None )
		self._user_id = kwargs.get( 'user_id', None )
		self._name = kwargs.get( 'name', None )
		self._author = kwargs.get( 'author', None )
		self._description = kwargs.get( 'description', None )
		self._publish_year = kwargs.get( 'publish_year', None )
		self._storage_url = kwargs.get( 'storage_url', None )
		self._audio_position_seconds = kwargs.get( 'audio_position_seconds', None )
		self._created_timestamp = kwargs.get('created_timestamp', None)



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
	def description( self ):
		return self._description



	@property
	def publish_year( self ):
		return self._publish_year



	@property
	def storage_url( self ):
		return self._storage_url



	@property
	def audio_position_seconds( self ):
		return self._audio_position_seconds


	@property
	def created_timestamp(self):
		return self._created_timestamp


	def json( self ):
		json = {
			'id': self.id,
			'userId': self.user_id,
			'name': self.name,
			'author': self.author,
			'description': self.description,
			'publishYear': self.publish_year,
			'storageUrl': self.storage_url,
			'audioPositionSeconds': self.audio_position_seconds,
			'createdTimestamp': self.created_timestamp
		}

		return { k: json[ k ] for k in json.keys() if json[ k ] }


	@classmethod
	def from_json( cls, **kwargs ):
		instance = cls()
		instance.id = kwargs.get( 'id', None )
		instance.user_id = kwargs.get( 'userId', None )
		instance.name = kwargs.get( 'name', None )
		instance.author = kwargs.get( 'author', None )
		instance.description = kwargs.get( 'description', None )
		instance.publish_year = kwargs.get( 'publishYear', None )
		instance.storage_url = kwargs.get( 'storageUrl', None )
		instance.audio_position_seconds = kwargs.get( 'audioPositionSeconds', None )
		instance.created_timestamp = kwargs.get('createdTimestamp', None)
		return instance

	@classmethod
	def from_tuple(cls, tuple):
		return cls( id=tuple[ 0 ],
		           name=tuple[ 1 ],
		           description=tuple[ 2 ],
		           publish_year=tuple[ 3 ],
		           storage_url=tuple[ 4 ],
		           audio_position_seconds=tuple[ 5 ],
		           created_timestamp=tuple[ 6 ] )



	def __repr__( self ):
		return 'AudioBook({})'.format( self.json() )


if __name__ == '__main__':
	a1 = AudioBook( name='The Intelligent Investor',
	                author='Benjamin Graham', publishYear=1932 )
	print( a1 )
