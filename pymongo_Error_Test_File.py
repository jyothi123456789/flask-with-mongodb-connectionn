from pymongo.errors import PyMongoError
from pymongo import MongoClient

try:
    # Your PyMongo code here
    client = MongoClient('mongodb://localhost:27017/')
    db = client['your_database_name']
    collection = db['your_collection_name']
    
    # Perform some MongoDB operations
    
except PyMongoError as e:
    print(f"An error occurred: {e}")
    # Handle the exception as needed
finally:
    # Close resources if necessary
    client.close()
from pymongo.errors import PyMongoError
from pymongo import MongoClient

try:
    # Your PyMongo code here
    client = MongoClient('mongodb://localhost:27017/')
    db = client['your_database_name']
    collection = db['your_collection_name']
    
    # Perform some MongoDB operations
    
except PyMongoError as e:
    print(f"An error occurred: {e}")
    # Handle the exception as needed
finally:
    # Close resources if necessary
    client.close()
