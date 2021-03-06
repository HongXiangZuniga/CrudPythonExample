from .model import modelUsers
from bson.json_util import dumps


class usersController:
    model = None
    def getUserById(self,id:int):
        result = self.model.getUserById(id)
        return dumps(result)
    
    def findUserByField(self,field:str,value):
        result = self.model.findUserByField(field,value)
        if result == None:
            return None
        for element in result:
           element = dumps(element)
        return dumps(result)

    def __init__(self):
        self.model = modelUsers()