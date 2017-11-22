import mysql.connector
from contextlib import ContextDecorator
from app.config.app_config import Config


class ConnectionManager(ContextDecorator):

    def __init__(self, config=None):
        if not config:
            self.config = Config()
        else:
            self.config = config



    def __enter__(self):
        self.conn = mysql.connector.connect(**self.config.db_config)
        return self.conn

    def __exit__(self, *exc):
        self.conn.close()
        return
