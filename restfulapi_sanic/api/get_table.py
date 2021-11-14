# from logging import NullHandler
# from api import app
# from main import app
# from restfulapi_sanic.main import app
from api import app
from sanic.response import json
from models import TodoItem, User, ConnectTodo, Tag
from sanic.exceptions import SanicException


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
        # return json({"message": "There's no todo!"})

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
    # for k, v in todo.items():
    #     res["todo"].append(v)

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
