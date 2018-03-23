from .database_manager import ConnectionManager
from .audiobook_dao import AudiobookDAO
from app.config import config

connection_manager = ConnectionManager(config=config)

