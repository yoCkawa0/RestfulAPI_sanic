from peewee import *
from sanic import Sanic
from sanic.response import json
from models import User, TodoItem, Tag, ConnectTodo
from sanic.exceptions import SanicException
import datetime

app = Sanic(__name__)


@app.route('/', methods=['GET'])
async def hello_world(request):
    return json({'Hello': 'World!'})


@app.route('/todo/<id:int>', methods=['GET'])
async def get_todo(request, id):
    query = (
        TodoItem.select(TodoItem.id, TodoItem.todo_title, User.id, User.user_name, Tag.id, Tag.tag_name)
        .join(User)
        .switch(TodoItem)
        .join(ConnectTodo)
        .join(Tag)
        .where(TodoItem.id == id)
    )
    if len(query) == 0:
        raise SanicException("IDが一致するtodoが見つかりませんでした.", status_code=404)

    todo = {}
    for q in query:
        if q.id not in todo:
            todo[q.id] = {
                "id": q.id,
                "todo_title": q.todo_title,
                "user": {
                    "id": q.user.id,
                    "name": q.user.user_name
                },
                "tag": [{
                    "id": q.connecttodo.tag_id,
                    "name": q.connecttodo.tag.tag_name
                }]
            }
        else:
            todo[q.id]["tag"].append({
                "id": q.connecttodo.tag_id,
                "name": q.connecttodo.tag.tag_name
            })

    res = {
        "todo": [v for _, v in todo.items()]
    }

    return json(res)


@app.route('/todos', methods=['GET'])
async def get_all_todes(request):
    query = (
        TodoItem.select(TodoItem.id, TodoItem.todo_title, User.id, User.user_name, Tag.id, Tag.tag_name)
        .join(User)
        .switch(TodoItem)
        .join(ConnectTodo)
        .join(Tag)
    )
    todos = {}
    for q in query:
        if q.id not in todos:
            todos[q.id] = {
                "id": q.id,
                "todo_title": q.todo_title,
                "user": {
                    "id": q.user.id,
                    "name": q.user.user_name
                },
                "tag": [{
                    "id": q.connecttodo.tag_id,
                    "name": q.connecttodo.tag.tag_name
                }]
            }
        else:
            todos[q.id]["tag"].append({
                "id": q.connecttodo.tag_id,
                "name": q.connecttodo.tag.tag_name
            })

    res = {
        "todos": [v for _, v in todos.items()]
    }
    return json(res)


# connect todo
@app.route('/connect', methods=['POST'])
async def connect_todo(request):
    todo = request.json["todo"]
    tag = request.json["tag"]
    print(todo)
    print(tag)
    ConnectTodo.create(todo=todo, tag=tag)
    return json({'message': 'connect todo & tags!'})


# add tag
@app.route('/tag', methods=['POST'])
async def add_tag(request):
    tag_name = request.json["tag_name"]
    print(tag_name)
    Tag.create(tag_name=tag_name)
    return json({'message': 'added tag!'})


# update tag
@app.route('/tag/<id:int>', methods=['PATCH'])
async def update_tag(request, id):
    new_tag_name = request.json["tag_name"]
    try:
        tag = Tag.get(Tag.id == id)
        # print("========")
        # print(tag)
    except DoesNotExist:
        # raise self.model.DoesNotExist("error.", status_code=500)
        # raise Exception("error.", status_code=500)
        # raise HTTPError(404)
        raise SanicException("error.", status_code=500)
        # return json({'error_message': '存在しないIDのです.'})
        # print("error")

    res = {'message': 'update tag!'}
    time_now = datetime.datetime.now()
    tag.tag_name = new_tag_name
    tag.update_at = time_now
    tag.save()
    return json({'message': 'update tag!'})
    # return json(res)


# delete tag
@ app.route('/tag/<id:int>', methods=['DELETE'])
async def delete_todo(request, id):
    tag = Tag.get(Tag.id == id)
    time_now = datetime.datetime.now()
    tag.deleted_at = time_now
    tag.save()
    # tag.delete_instance()
    return json({'message': 'deleted tag!'})


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
