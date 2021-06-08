from pymongo import *
from pymongo.errors import ConfigurationError

import  system.Config

import logging
try:



         
 client =  MongoClient(system.Config.Variable.MONGO_DB_URL)
except ConfigurationError:
    logging.info("Mongo DB URL Incorrect!, check whats wrong with it ")
sed = client['test']
db = sed['test']


