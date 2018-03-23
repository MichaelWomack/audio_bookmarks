from ..persistence import ConnectionManager
from ..model import AudioBook

class AudiobookDAO( object ):

	def __init__(self, connection_manager: ConnectionManager):
		self.connection_manager = connection_manager

	def insert( self, audiobook: AudioBook ):
		"""
		:param audiobook: audiobook object to insert
		:type audiobook: app.model.audiobook.Audiobook
		:return:
		"""
		with self.connection_manager as conn:
			cur = conn.cursor()
			insert_query = """
				INSERT INTO audiobooks (
					name, 
					author, 
					description, 
					publish_year, 
					storage_url, 
					audio_position_seconds,
					created_timestamp
				) VALUES (%s, %s, %s, %s, %s, %s, current_timestamp)
			"""
			record = (audiobook.name,
			          audiobook.author,
			          audiobook.description,
			          audiobook.publish_year,
			          audiobook.storage_url,
			          audiobook.audio_position_seconds)
			cur.execute( insert_query, record )
			conn.commit()



	def update( self, audiobook: AudioBook ):
		"""
		Updates the given audiobook
		:type audiobook: app.model.audiobook.AudioBook
		:param audiobook: audio book to update
		"""
		with self.connection_manager as conn:
			cur = conn.cursor()
			update_query = """
				UPDATE audiobooks 
				SET
					name = %s, 
					author = %s, 
					description = %s, 
					publish_year = %s, 
					storage_url = %s, 
					audio_position_seconds = %s
				WHERE id = %s
			"""
			record = (audiobook.name,
			          audiobook.author,
			          audiobook.description,
			          audiobook.publish_year,
			          audiobook.storage_url,
			          audiobook.audio_position_seconds,
			          audiobook.id)
			cur.execute( update_query, record )
			conn.commit()


	def get_by_id( self, id: int ) -> AudioBook:
		"""
		:type id: int
		:param id: audiobook id
		:return: audiobook record
		:rtype: app.model.audiobook.Audiobook
		"""
		with self.connection_manager as conn:
			cur = conn.cursor()
			query = """
				SELECT 
					id, 
				 	name,
				 	author,
				 	description,
				 	publish_year,
				 	storage_url,
				 	audio_position_seconds,
				 	created_timestamp	
				 FROM audiobooks
				 WHERE id = %s;
			"""
			cur.execute( query, (id,) )
			record = cur.fetchone()
			if record:
				return AudioBook( id=record[ 0 ],
								  name=record[ 1 ],
								  author=record [ 2 ],
								  description=record[ 3 ],
								  publish_year=record[ 4 ],
								  storage_url=record[ 5 ],
								  audio_position_seconds=record[ 6 ],
								  created_timestamp=record[ 7 ] )



	def get_all( self ) -> [AudioBook]:
		"""
		:rtype: list of app.model.audiobook.AudioBook
		:return: list of AudioBook
		"""
		with self.connection_manager as conn:
			cur = conn.cursor()
			query = """
				SELECT 
					id, 
				 	name,
				 	description,
				 	publish_year,
				 	storage_url,
				 	audio_position_seconds,
				 	created_timestamp	
				 FROM audiobooks;
			"""
			cur.execute( query )
			result_set = cur.fetchall()

			def from_tuple(tuple):
				return AudioBook(
					 id=tuple[ 0 ], name=tuple[ 1 ], description=tuple[ 2 ], publish_year=tuple[ 3 ],
						storage_url=tuple[ 4 ], audio_position_seconds=tuple[ 5 ], created_timestamp=tuple[ 6 ]
				)

			audiobooks = [ from_tuple( record_tuple ) for record_tuple in result_set ]
			return audiobooks


	def delete(self, id: int):
		with self.connection_manager as conn:
			cur = conn.cursor()
			query = """
				DELETE from audiobooks where id = %s;
			"""
			cur.execute(query, (id,))
			conn.commit()


