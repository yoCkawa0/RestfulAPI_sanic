# from api import app
from api import app
from sanic.response import json
from models import ConnectTodo


@app.route('/connect', methods=['POST'])
async def connect_todo(request):
    # todo_id = request.json["todo_id"]
    todo = request.json["todo"]
    tag = request.json["tag"]
    # tag_id = request.json["tag_id"]
    print(todo)
    print(tag)
    ConnectTodo.create(todo=todo, tag=tag)
    # ConnectTodo.create(todo_id=todo_id,tag_id=)
    return json({'message': 'connect todo & tags!'})
