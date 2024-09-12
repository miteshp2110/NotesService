from bson import ObjectId

def updateNoteWithId(note,collection):
    try:
        
        result= collection.update_one(
            {"notes._id":ObjectId(note.get("_id"))},
            {
                "$set":{
                    "notes.$.title":note.get('title'),
                    "notes.$.description":note.get('description')
                }
            }
        )

        if result.matched_count > 0 :
            return True
    
        else:
            return {"Error":"Failed To update Record"},500
            

       
    except Exception as e:
        print(e)
        return {"Error":"Some Error Occured"},500