import mysql.connector
from contextlib import contextmanager

class DatabaseManager(object):

    def __init__(self, db_config):
        self.db_config = db_config

    def get_connection(self):
        return mysql.connector.connect(**self.db_config)
