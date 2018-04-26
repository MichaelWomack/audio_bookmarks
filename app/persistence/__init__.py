from .database_manager import ConnectionManager
from .audiobook_dao import AudiobookDAO
from app.config import config
from .setup import setup_db


connection_manager = ConnectionManager(config=config.DB_CONFIG)

