from .config_objects import Config
from .auth import setup_oauth2
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.environ['DOTENV'], verbose=True)
oauth2 = setup_oauth2()
config = Config()