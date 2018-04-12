import os
from .app import Config
from .envs import Environment

lcp = os.environ.get('ABM_LCP', 'NP')
config = Config(env=lcp.lower())