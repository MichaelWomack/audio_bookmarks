from .database_manager import ConnectionManager
import pkg_resources

def setup_db( resource_package, cm: ConnectionManager ):
	db_setup_sql_file = pkg_resources.resource_filename(resource_package, 'setup.sql')
	sql = open(db_setup_sql_file).read()

	with cm as conn:
		cursor = conn.cursor()
		cursor.execute( sql )
		conn.commit()

