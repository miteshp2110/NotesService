import jwt
from jwt.exceptions import ExpiredSignatureError,InvalidTokenError
import os

JWT_SECRET_KEY = os.getenv('JWT_SECRET')

def verifyToken(token):
    if not token:
        return {"error":"No Token Provided"}
    try:
        decoded=jwt.decode(token,JWT_SECRET_KEY,"HS256")
        # print(decoded)
        return 200
    except ExpiredSignatureError:
        
        # print("Token has expired!")
        return {"Error":"Expired Token"}
    
    except InvalidTokenError:
        
        # print("Invalid token!")
        return {"Error":"Invalid Token"}
    except Exception as e:
        print("Error in decoding",e)
        return {"Error":"Some Error Occured"}
        