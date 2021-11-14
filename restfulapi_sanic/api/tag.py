from peewee import DoesNotExist
# from main import app
# from restfulapi_sanic.main import app
from api import app
from sanic.response import json
from models import Tag
import datetime
from sanic.exceptions import SanicException


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
    except DoesNotExist:
        raise SanicException("error.", status_code=500)
        # return json({'error_message': '存在しないIDのです.'})

    res = {'message': 'update tag!'}
    time_now = datetime.datetime.now()
    tag.tag_name = new_tag_name
    tag.update_at = time_now
    tag.save()
    return json({'message': 'update tag!'})
    return json(res)


# delete tag
@ app.route('/tag/<id:int>', methods=['DELETE'])
async def delete_todo(request, id):
    tag = Tag.get(Tag.id == id)
    time_now = datetime.datetime.now()
    tag.deleted_at = time_now
    tag.save()
    # tag.delete_instance()
    return json({'message': 'deleted tag!'})
