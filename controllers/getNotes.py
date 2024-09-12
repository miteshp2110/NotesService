from flask import jsonify
from bson import ObjectId
def getAllNotes(email,collection):
    try:

        
       
        user = collection.find_one({"email": email}, {"_id": 0})
        if user :
            convert_objectid_to_str(user)
            return jsonify(user)
        else:
            baseObj={
                "email":email,
                "notes":[]
            }
            result = collection.insert_one(baseObj)
            print("Created new user")
            return getAllNotes(email,collection)
            # return jsonify({"Error":"Some Error Occured while searching"}),500
        
    except Exception as e:
        print("Exception as ",e)
        return {"Error":"Some Error Occured"},500
    


def convert_objectid_to_str(data):
    if isinstance(data, list):
        for item in data:
            convert_objectid_to_str(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, ObjectId):
                data[key] = str(value)
            elif isinstance(value, (dict, list)):
                convert_objectid_to_str(value)

