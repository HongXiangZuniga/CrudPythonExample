from flask import Flask,request
import json

from pkg.users.controller import usersController

app = Flask(__name__)


@app.route('/user/id/<idUser>')
def getUserById(idUser):
    idUser = idUser
    controller = usersController()
    result = controller.getUserById(int(idUser))
    return result

@app.route('/user/<field>/<value>')
def getUserByField(field,value):
    field = field
    value = value
    controller = usersController()
    result = controller.findUserByField(field,value)
    return result



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8027)