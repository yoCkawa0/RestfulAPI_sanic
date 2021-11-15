from api import app
from sanic.response import json
from models import TodoItem
import datetime


# add todo
@app.route('/todo', methods=['POST'])
async def add_todo(request):
    req = request.json["todo_title"]
    user = request.json["user"]
    # todo_title = "{}".format(req)
    print(req)
    print(user)
    TodoItem.create(todo_title=req, user_id=user)
    return json({'message': 'added todo!'})


# update todo
@app.route('/todo/<id:int>', methods=['PATCH'])
async def update_todo(request, id):
    new_todo_title = request.json["todo_title"]
    new_user = request.json["user"]
    todo = TodoItem.get(TodoItem.id == id)
    time_now = datetime.datetime.now()
    todo.todo_title = new_todo_title
    todo.user = new_user
    todo.update_at = time_now
    todo.save()
    return json({'message': 'update todo!'})


# delete todo
@app.route('/todo/<id:int>', methods=['DELETE'])
async def delete_todo(request, id):
    todo = TodoItem.get(TodoItem.id == id)
    time_now = datetime.datetime.now()
    todo.deleted_at = time_now
    todo.save()
    # todo.delete_instance()
    return json({'message': 'deleted todo!'})
