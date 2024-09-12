from flask import Flask,Request,jsonify,request
from services.validateToken import verifyToken
from services.databaseService import connect_db
import json
from controllers.createUser import createUserSchema
from controllers.addNotes import insertNote
from controllers.getNotes import getAllNotes
from controllers.updateNotes import updateNoteWithId
from controllers.deleteNote import deleteNoteWithId




app=Flask(__name__)

collection=connect_db()





@app.route('/',methods=['GET'])
def getNote():
   header=(request.headers.get('Authorization'))
   if not header:
       return {"error":"No Token Provided"}
   token=header.split(" ")[1]
   tokenStatus=verifyToken(token)
   if(tokenStatus==200):
       body=request.data
       if not body:
          return jsonify({"Error":"No request body provided"}),400
       email= (json.loads(body.decode())).get('email')
       if not email:
          return jsonify({"Error":"No email provided"}),500
       all_notes=getAllNotes(email,collection)

       return all_notes
       
   return tokenStatus

@app.route('/',methods=['POST'])
def addNote():
   header=(request.headers.get('Authorization'))
   if not header:
       return {"error":"No Token Provided"}
   token=header.split(" ")[1]
   tokenStatus=verifyToken(token)
   if(tokenStatus==200):
       body=request.data
       if not body:
          return {"Error":"No body provided"},400
       noteObj=(json.loads(body.decode())).get('note')
       email=(json.loads(body.decode())).get('email')
       if not noteObj or not email:
          return jsonify({"Error":"Incomplete Details"}),400
       addStatus=insertNote(noteObj,collection,email)
       if(addStatus==True):
          return jsonify({"Success":"Note Added Successfully"}),201
       else:
          return addStatus
   return tokenStatus

@app.route('/',methods=['DELETE'])
def deleteNote():
   header=(request.headers.get('Authorization'))
   if not header:
       return {"error":"No Token Provided"}
   token=header.split(" ")[1]
   tokenStatus=verifyToken(token)
   if(tokenStatus==200):
       
       body=request.data
       if not body:
          return jsonify({"Error":"No body provided"}),400
       _id=(json.loads(body.decode())).get('id')
       if not _id :
          return jsonify({"Error":"Id not provided for Note"}),400
       
       deleteStatus=deleteNoteWithId(_id,collection)
       if deleteStatus == True:
          return jsonify({"Success":"Note Deleted"}),200
       else:
          return deleteStatus
       
   return tokenStatus

@app.route('/',methods=['PUT'])
def updateNote():
   header=(request.headers.get('Authorization'))
   if not header:
       return {"error":"No Token Provided"}
   token=header.split(" ")[1]
   tokenStatus=verifyToken(token)
   if(tokenStatus==200):
       body=request.data
       if not body:
          return jsonify({"Error":"Body Not provided"}),400
       data= json.loads(body.decode())
       
       note=data.get('note')

       if not note:
          return jsonify({"Error":"Invalid Paramaters"}),400
       

       updateStatus=updateNoteWithId(note,collection)

       if(updateStatus==True):
          return jsonify({"Success":"Updated Note"}),200
       else:
          return updateStatus

       
   return tokenStatus

@app.route('/createUser',methods=['POST'])
def createUser():
   header=(request.headers.get('Authorization'))
   if not header:
       return {"error":"No Token Provided"},400
   token=header.split(" ")[1]
   tokenStatus=verifyToken(token)
   if(tokenStatus==200):
       try:
        body=request.data
        if(not body):
            return jsonify({"error":"No Body Provided"}),400
        body=json.loads(body.decode())
        email=body.get('email')
        if not email:
           return jsonify({"Error":"Email not Provided"}),400
        # print(body.get('email'))

        createStatus=createUserSchema(email,collection)

        if(createStatus == True):
           return jsonify({"Success":"User Created Successfully"}),201
        else:
           return createStatus,403
        
       except Exception as e:
        print("error occures: ",e)
        return jsonify({"error":"Some Error Occured"}),500
   return 






if __name__=="__main__":
    
    app.run(port=3000,debug=True)