import os

import certifi
from pymongo import MongoClient

_connection_string = os.environ["CONNECTION_STRING"]

cluster = MongoClient(_connection_string, tlsCAFile=certifi.where())
db = cluster["TDD"]

