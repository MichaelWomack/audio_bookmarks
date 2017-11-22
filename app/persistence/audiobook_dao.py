from app.persistence.database_manager import ConnectionManager
from app.config.app_config import Config
from app.model.audiobook import AudioBook

connection_manager = ConnectionManager()


class AudiobookDAO( object ):
	def __init__( self, config ):
		self.config = config



	def get_by_id( self ):
		pass



	def get_all( self ):
		audiobooks = [ ]

		with connection_manager as conn:
			a1 = AudioBook( name='The Intelligent Investor', author='Benjamin Graham', publishYear=1932 )
			a2 = AudioBook( name='Security Analysis', author='Benjamin Graham', publishYear=1944 )
			a3 = AudioBook( name='Little Book of Common Sense Investing', author='John C. Bogle', publishYear=2006 )
			a4 = AudioBook(name='What is the test?', author='Not Sure')
			audiobooks.extend([a1, a2, a3, a4])
			return audiobooks



def main():
	config = Config()
	ab = AudiobookDAO( config )
	print(ab.get_all())


if __name__ == '__main__':
	main()
