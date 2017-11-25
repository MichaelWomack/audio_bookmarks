from app.persistence.database_manager import ConnectionManager
from app.config.app_config import Config
from app.model.audiobook import AudioBook

connection_manager = ConnectionManager()


class AudiobookDAO( object ):


	def __init__( self, config ):
		self.config = config

	def insert( self, audiobook ):
		"""
		:param audiobook: audiobook object to insert
		:type audiobook: app.model.audiobook.Audiobook
		:return:
		"""
		with connection_manager as conn:
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



	def update( self, audiobook ):
		with connection_manager as conn:
			cur = conn.cursor()
			insert_query = """
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
			cur.execute( insert_query, record )
			conn.commit()



	def get_by_id( self, id ):
		"""
		:type id: int
		:param id: audiobook id
		:return: audiobook record
		:rtype: app.model.audiobook.Audiobook
		"""
		with connection_manager as conn:
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
				 FROM audiobooks
				 WHERE id = %s;
			"""
			cur.execute( query, (id,) )
			record = cur.fetchone()
			return AudioBook( id=record[ 0 ],
			                  name=record[ 1 ],
			                  description=record[ 2 ],
			                  publish_year=record[ 3 ],
			                  storage_url=record[ 4 ],
			                  audio_position_seconds=record[ 5 ],
			                  created_timestamp=record[ 6 ] )



	def get_all( self ):
		"""
		:rtype: list of app.model.audiobook.AudioBook
		:return: list of AudioBook
		"""
		with connection_manager as conn:
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
			audiobooks = [ AudioBook.from_tuple( ab ) for ab in result_set ]
			return audiobooks


def main():
	config = Config()
	dao = AudiobookDAO( config )
	ab = AudioBook( id=5, name='A Little Book of Common Sense Investing',
	                author='John C. Dogle',
	                publish_year=1900,
	                description='Investing with low-cost index funds',
	                storage_url='gs://audiobucket/media',
	                audio_position_seconds=19 )
	dao.update( ab )


if __name__ == '__main__':
	main()
