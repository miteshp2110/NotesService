from bson.objectid import ObjectId

def insertNote(note,collection,email):
    try:
        
        
        new_note={
            "_id": ObjectId(),
            "title":note.get('title'),
            "description":note.get('description')
        }
        result= collection.update_one(
            {"email":email},
            {"$push":{"notes":new_note}}
        )
        
        if result.modified_count >0:
            return True
        else:
            return {"Error":"Invalid Email"},403
    except Exception as e:
        print("Error While Insertion: ",e)
        return {"Error":"Some Error Occured"},500