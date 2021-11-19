from pymongo import MongoClient


class modelUsers:
    client = None #Client to db
    db=None #database
    collection = None#collection

    def getUserById(self,id:int):
        result = self.collection.find_one({"id":id})
        return result
    
    def findUserByField(self,field:str,value):
        result = []
        mongoResult = self.collection.find({field:value})
        for element in mongoResult:
            result.append(element)
            mongoResult.next()
        return result

    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017") #Client to db
        self.db=self.client.users #database
        self.collection = self.db.users #collection