from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def connect_db():
    try:
        client= MongoClient("mongodb://root:root@localhost:27017/")
        client.admin.command('ping')
        print("DB Connected")
        db=client['NoteService']
        collection=db['Notes']
        return collection
        


    except ConnectionFailure:
        print("Failed to Connect to database")
        return None

    except Exception as e:
        print("An error Occured While Connecting to Database: ",e)
        return None
    

