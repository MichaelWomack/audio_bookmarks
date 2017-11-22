import os
import configparser

class Config():

    def __init__(self, env=None):
        if not env or env.lower() not in ('test', 'np', 'pr'):
            self.env = os.environ.get('ABM_LCP', 'NP').lower()
        else:
            self.env = env.lower()

        config = configparser.ConfigParser()
        config_file_path = os.path.join(os.path.dirname(__file__), '../resources/conf/{}.ini'.format(self.env))
        config.read(config_file_path)

        self.db_config = {
            'host': config['database']['host'],
            'port': config['database']['port'],
            'database': config['database']['database'],
            'user': config['database']['user'],
            'password': config['database']['password']
        }
