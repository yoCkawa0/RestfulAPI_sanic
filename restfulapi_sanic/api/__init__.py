from sanic import Sanic
app = Sanic(__name__)
# from restfulapi_sanic.main import app

from api.hello_world import *

from api.todo import *
from api.tag import *
from api.user import *
from api.connect_todo import *

from api.get_table import *
