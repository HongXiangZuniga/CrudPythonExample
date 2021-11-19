from http import HTTPStatus
from flask import Flask,jsonify,Response

from pkg.users.controller import usersController

app = Flask(__name__)


@app.route('/user/id/<idUser>')
def getUserById(idUser):
    idUser = idUser
    controller = usersController()
    result = controller.getUserById(int(idUser))
    if result==None:
        return Response(result, mimetype='application/json',status=404)
    return Response(result, mimetype='application/json',status=200)

@app.route('/user/<field>/<value>')
def getUserByField(field,value):
    field = field
    value = value
    if value.isnumeric():
        value = int(value)
    controller = usersController()
    result = controller.findUserByField(field,value)
    if result== None:
        return Response(None, mimetype='application/json',status=404)
    if len(result)== 0:
        return Response(None, mimetype='application/json',status=404)
    return Response(result, mimetype='application/json',status=200)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8027)