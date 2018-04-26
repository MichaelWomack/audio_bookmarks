import json

import pytest
from pytest_mock import mocker

from app.model import AudioBook
from app.persistence.audiobook_dao import AudiobookDAO
from app.main import create_app


class TestAudiobookApi( object ):

	@pytest.fixture
	def client( self ):
		### TODO: mock the oauth2
		app = create_app()
		app.testing = True
		return app.test_client()



	def test_get_all_audiobooks( self, client, mocker ):
		expected_name = 'The Name of the Wind'
		expected_author = 'Patrick Rothfus'
		mocked_get_all = mocker.patch.object( AudiobookDAO, 'get_all' )
		mocked_get_all.return_value = [ AudioBook( name=expected_name, author=expected_author ) ]

		res = client.get( 'api/audiobooks/' )
		mocked_get_all.assert_called()
		assert res.status_code == 200

		res_body = json.loads( res.get_data() )[ 0 ]
		audiobook = AudioBook.from_json( **res_body )
		assert audiobook.name == expected_name
		assert audiobook.author == expected_author



	def test_get_audiobook_by_id( self, client, mocker ):
		mocked_get_by_id = mocker.patch.object( AudiobookDAO, 'get_by_id' )
		id = 1
		mocked_get_by_id.return_value = AudioBook( name='Test Book Title', author='Test Author' )
		res = client.get( 'api/audiobooks/id/{}'.format( id ) )
		mocked_get_by_id.assert_called_with( id )
		assert res.status_code == 200

		body = json.loads( res.get_data() )
		assert body[ 'name' ] == 'Test Book Title'
		assert body[ 'author' ] == 'Test Author'



	def test_delete_audiobook( self, client, mocker ):
		mocked_delete_call = mocker.patch.object( AudiobookDAO, 'delete' )
		id = 1
		res = client.delete( 'api/audiobooks/id/{}'.format( id ) )
		mocked_delete_call.assert_called_with( id )
		assert res.status_code == 200



	def test_post_audiobook( self, client, mocker ):
		mocked_insert = mocker.patch.object( AudiobookDAO, 'insert' )
		mocked_from_json = mocker.patch.object( AudioBook, 'from_json' )
		audiobook = AudioBook( name='Test Book Title', author='Test Author' )
		mocked_from_json.return_value = audiobook

		json_data = audiobook.json()
		res = client.post( '/api/audiobooks/', data=json.dumps( json_data ), content_type='application/json' )
		assert res.status_code == 200
		mocked_insert.assert_called_with( audiobook )



	def test_put_audiobook( self, client, mocker ):
		mocked_update = mocker.patch.object( AudiobookDAO, 'update' )
		mocked_from_json = mocker.patch.object( AudioBook, 'from_json' )
		audiobook = AudioBook( name='Test Book Title', author='Test Author' )
		mocked_from_json.return_value = audiobook

		json_data = audiobook.json()
		res = client.put( '/api/audiobooks/', data=json.dumps( json_data ), content_type='application/json' )
		assert res.status_code == 200
		mocked_update.assert_called_with( audiobook )
