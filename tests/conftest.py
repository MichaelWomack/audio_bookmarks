import pkg_resources
import pytest
from app.persistence import ConnectionManager
from app.persistence.setup import setup_db
from app.config import Config

@pytest.fixture
def get_test_config():
	config = Config(env='test')
	return config

@pytest.fixture
def get_test_connection_manager():
	config = get_test_config()
	connection_manager = ConnectionManager(config=config)
	return connection_manager

@pytest.fixture
def setup_test_db():
	resource_package = 'tests.resources.sql'
	connection_manager = get_test_connection_manager()
	setup_db(resource_package, connection_manager)


#TODO: make this a parameterizable fixture. This will come in handy for other DAO tests.
# This causes weird issues with primary key syncronization. Load each record from csv?
@pytest.fixture
def load_test_records():
	# setup_test_db()
	csv_file = pkg_resources.resource_filename( 'tests.resources.data', 'audiobooks_sample.csv' )
	sync_query = pkg_resources.resource_filename('tests.resources.sql', 'sync_audiobook_ids.sql')
	connection_manager = get_test_connection_manager()

	with connection_manager as conn, open( csv_file ) as f, open(sync_query) as query_file:
		cursor = conn.cursor()
		next( f )  # skip header row
		cursor.copy_from( f, 'audiobooks', sep=',' )
		cursor.execute(query_file.read()) # sync id sequence table after loading csv's
		conn.commit()