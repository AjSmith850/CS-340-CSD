# Anthony J Smith CS-340-R3334 Client/Server Development 24EW3

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        USER = 'aacuser'
        PASS = 'snhu1234'
        DB = 'aac'
        COL = 'animals'
        CONNECTION_STRING = f'mongodb+srv://{USER}:{PASS}@animalshelter.pqfi7pt.mongodb.net/{DB}'

        self.client = MongoClient(CONNECTION_STRING)
        self.database = self.client[DB]
        self.collection = self.database[COL]
        
    def create(self, data):
        if data:
            try:
                result = self.collection.insert_one(data)
                return result.inserted_id
            except Exception as e:
                raise Exception(f"An error occurred during insert: {e}")
        else: 
            raise Exception("Nothing to save; empty entry")
        
    def read(self, query):
        try:
            if query is not None:
                results = self.collection.find(query)
                return list(results)
            else:
                raise Exception("Nothing to query")
        except Exception as e:
            print(f"Error: {e}")
            return None

        
    def update(self, query, update_data):
        if query is not None and update_data is not None:
            result = self.collection.update_many(query, {'$Set': update_data})
            result = result.modified_count
        else:
            raise Exception("Query or data missing")

    def delete(self, query):
        if query is not None:
            result = self.collection.delete_many(query)
        else:
            raise Exception("Query missing")