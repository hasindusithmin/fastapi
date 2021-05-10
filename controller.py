

from fastapi import FastAPI
from models.model import User
from repositary import repositary

app =  FastAPI()

@app.post("/user")
def user(user:User):
   return repositary.addUser(user.dict())

@app.get("/user")
def user():
    return repositary.getUser()

@app.get("/user/{id}")
def user(id:int):
    MyDict = {"id":id}
    return repositary.GetSpecUser(MyDict)

@app.put("/user/{id}")
def user(user:User,id:int):
    myquery = {"id":id}
    newValue = {"$set":user.dict()}
    return repositary.UpdateUser(myquery,newValue)

@app.delete("/user/{id}")
def user(id:int):
    myquery = {"id":id}
    return repositary.DeleteUser(myquery)



