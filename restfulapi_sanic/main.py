from peewee import *
from sanic import Sanic
# from sanic.response import json

from api import app

# app = Sanic(__name__)


# @app.route('/', methods=['GET'])
# async def hello_world(request):
#     return json({'Hello': 'World!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
