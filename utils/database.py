import os

import certifi
from pymongo import MongoClient

connection_string = os.environ["CONNECTION_STRING"]

cluster = MongoClient(connection_string, tlsCAFile=certifi.where())
db = cluster["TDD"]

