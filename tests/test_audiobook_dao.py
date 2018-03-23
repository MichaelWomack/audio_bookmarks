import datetime

import pytest

from app.model import AudioBook
from app.persistence import AudiobookDAO
from tests.conftest import get_test_connection_manager


@pytest.mark.usefixtures('setup_test_db', 'load_test_records' )
class TestAudiobookDAO( object ):

	@pytest.fixture
	def dao( self ):
		connection_manager = get_test_connection_manager()
		return AudiobookDAO( connection_manager=connection_manager )


	def test_insert( self, dao: AudiobookDAO ):
		expected_name = 'The Name of the Wind'
		expected_author = 'Patrick Rothfus'
		ts = datetime.datetime.now()

		audiobook = AudioBook(name=expected_name, author=expected_author)
		dao.insert( audiobook )
		inserted = dao.get_by_id( 4 )

		assert inserted is not None
		assert inserted.name == expected_name
		assert inserted.author == expected_author
		assert inserted.created_timestamp > ts


	def test_update( self, dao: AudiobookDAO ):
		record = dao.get_by_id(1)
		update_name = 'New Title'
		update_author = 'New Author'
		record.name = update_name
		record.author = update_author
		dao.update(record)

		updated = dao.get_by_id(1)
		assert updated.name == update_name
		assert updated.author == update_author


	def test_delete( self, dao: AudiobookDAO ):
		r1 = dao.get_by_id( 1 )
		assert r1 is not None

		dao.delete( r1.id )
		r1 = dao.get_by_id( 1 )
		assert r1 is None


	def test_get_all( self, dao: AudiobookDAO ):
		records = dao.get_all()
		assert len( records ) == 3

		for index, record in enumerate( records, 1 ):
			assert index == record.id
