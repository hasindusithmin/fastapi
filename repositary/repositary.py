import pymongo


myCluster = pymongo.MongoClient("mongodb+srv://*****:*****@cluster0.8aoun.mongodb.net/pythondb?retryWrites=true&w=majority")

mydb = myCluster["pythondb"]
mycol = mydb["user"]

def addUser(user):
    mycol.insert_one(user)
    return "inserted!"

def getUser():
    myList = []
    for x in mycol.find():
        x.pop("_id")
        myList.append(x)
    return myList

def GetSpecUser(query):
    myDict = {}
    for x in mycol.find(query):
        x.pop("_id")
        myDict.update(x) 
    return myDict

def UpdateUser(query,value):
    mycol.update_one(query,value)
    return "updated!"


def DeleteUser(query):
    mycol.delete_one(query)
    return "deleted"
    
