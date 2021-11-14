# from api import app
# from main import app
# from restfulapi_sanic.main import app
from api import app
from sanic.response import json
from models import User
import datetime


# add user
@app.route('/user', methods=['POST'])
async def add_user(request):
    user_name = request.json["user_name"]
    print(user_name)
    User.create(user_name=user_name)
    return json({'message': 'added user!'})


# update user
@app.route('/user/<id:int>', methods=['PATCH'])
async def update_tag(request, id):
    new_user_name = request.json["tag_name"]
    user = User.get(User.id == id)
    time_now = datetime.datetime.now()
    user.user_name = new_user_name
    user.update_at = time_now
    user.save()
    return json({'message': 'update user!'})


# delete user
@app.route('/user/<id:int>', methods=['DELETE'])
async def delete_todo(request, id):
    user = User.get(User.id == id)
    time_now = datetime.datetime.now()
    user.deleted_at = time_now
    user.save()
    # user.delete_instance()
    return json({'message': 'deleted user!'})
