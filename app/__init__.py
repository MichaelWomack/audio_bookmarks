from app.persistence import connection_manager as _connection_manager
from app.persistence.setup import setup_db as _setup_db
from app.config import config


resource_package = 'app.resources.sql'
_setup_db(resource_package, _connection_manager)