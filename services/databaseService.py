from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
def connect_db():

    try:

        # mongo_host='localhost'
        # mongo_username='root'
        # mongo_password='root'
        mongo_host=os.getenv('MONGO_HOST')
        mongo_username=os.getenv('MONGO_USERNAME')
        mongo_password=os.getenv('MONGO_PASSWORD')
        # print(mongo_host,mongo_username,mongo_password)

        url="mongodb://"+mongo_username+":"+mongo_password+"@"+mongo_host+":27017/"

        # print(url)

        


        client= MongoClient(url)
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
    

