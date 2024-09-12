from pymongo.errors import DuplicateKeyError




def createUserSchema(email,collection):
    try:
        baseObj={
            "email":email,
            "notes":[]
        }
        result = collection.insert_one(baseObj)
        # print(result)
        
        
        return True
    except DuplicateKeyError:
        # print(email," already exist")
        return {"Error":"Email already Exist"}
    except Exception as e:
        # print("Error: ",e)
        return e