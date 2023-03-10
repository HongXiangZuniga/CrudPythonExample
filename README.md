# CrudPythonExample
It is a example to Crud Api in python with flask and connected to mongodb.

ENV:
```
PORT=
MONGO_URI=
MONGO_COLLECTIONS=
MONGO_DB=

```

The struct of mongo data is:

```json
{
  "id":22,
  "name":"Hong Xiang",
  "email":"hongxiang17@gmail.com",
  "age":27,
  "entryDate":{"$date":"2018-06-25T21:46:44.000Z"},
  "country":"Chile"
}
 ```
Endpoints:
```
GET /user/id/<idUser> <get user by id>
GET /user/field/:value <get users by field and value>
```

Run:
```
Make run
```

