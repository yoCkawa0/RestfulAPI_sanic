from restfulapi_sanic.api import app
from sanic.response import json


@app.route('/', methods=['GET'])
async def hello_world(request):
    return json({'Hello': 'World!'})
