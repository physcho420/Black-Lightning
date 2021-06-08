from pymongo import *
from pymongo.errors import ConfigurationError

from system.Config import Variable
import logging
try:



         
 client =  MongoClient(Variable.MONGO_DB_URL)
except ConfigurationError:
    logging.info("Mongo DB URL Incorrect!, check whats wrong with it ")
sed = client['test']
db = sed['test']


