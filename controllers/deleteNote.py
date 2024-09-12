from bson import ObjectId

def deleteNoteWithId(_id,collection):
    try:

        note_id=ObjectId(_id)
        result=collection.update_one(
            {"notes._id":note_id},
            {
                "$pull" : {
                    "notes": {
                        "_id": note_id
                    }
                }
            }
        )
        
        if result.modified_count > 0:
            return True
        else:
            return {"Error":"No Such Note Found"},400
    except Exception as e:
        print("Exception Occcred while Deleting: ",e)
        return False