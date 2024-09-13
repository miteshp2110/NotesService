import jwt
from jwt.exceptions import ExpiredSignatureError,InvalidTokenError
import os

secretKey = str(os.getenv('JWT_SECRET'))

def verifyToken(token):
    token=str(token)
    # print(secretKey)
    if not token:
        return {"error":"No Token Provided"}
    try:
        decoded_token = jwt.decode(token, secretKey, algorithms=['HS256'])
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
        