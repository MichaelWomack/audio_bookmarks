from .base_dto import JsonSerializable


class AudioBook( JsonSerializable ):


	def __init__( self, **kwargs ):
		self.id = kwargs.get( 'id', None )
		self.user_id = kwargs.get( 'user_id', None )
		self.name = kwargs.get( 'name', None )
		self.author = kwargs.get( 'author', None )
		self.description = kwargs.get( 'description', None )
		self.publish_year = kwargs.get( 'publish_year', None )
		self.storage_url = kwargs.get( 'storage_url', None )
		self.audio_position_seconds = kwargs.get( 'audio_position_seconds', None )
		self.created_timestamp = kwargs.get('created_timestamp', None)



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


	def __repr__( self ):
		return 'AudioBook({})'.format( self.json() )

