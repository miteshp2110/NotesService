from flask import Flask,Request,jsonify,request
import jwt
from jwt.exceptions import InvalidTokenError,ExpiredSignatureError

app=Flask(__name__)
JWT_SECRET_KEY = "SampleSeceretKey"



@app.route('/')
def helloWorld():
    token=(request.headers.get('Authorization')).split(" ")[1]
    return verifyToken(token)


@app.route('/getNotes',methods=['GET'])
def getNote():
   token=(request.headers.get('Authorization')).split(" ")[1]
   tokenStatus=verifyToken(token)
   if(tokenStatus==200):
       return "Get Notes"
   return tokenStatus


def verifyToken(token):
    try:
        decoded=jwt.decode(token,JWT_SECRET_KEY,"HS256")
        print(decoded)
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
        

if __name__=="__main__":
    
    app.run(port=3000,debug=True)