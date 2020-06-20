# config.py
debug = True

import sys

sys.path.insert(0, '/lib/')
from lib import chaos

chaos.simple_fire()
