from peewee import *
# import psycopg2
import datetime


test_db = PostgresqlDatabase('postgres', host='localhost', port=8081, user='postgres', password='example')


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    deleted_at = DateTimeField(null=True)

    class Meta:
        database = test_db


class User(BaseModel):
    user_name = CharField(unique=True)

    class Meta:
        table_name = "users"


class TodoItem(BaseModel):
    todo_title = CharField()
    user = ForeignKeyField(User, backref='todo_items')

    class Meta:
        table_name = "todo_items"


class Tag(BaseModel):
    tag_name = CharField(unique=True)

    class Meta:
        table_name = "tags"


class ConnectTodo(BaseModel):
    todo = ForeignKeyField(TodoItem, backref='connect_todos')
    tag = ForeignKeyField(Tag, backref='connect_todos')

    class Meta:
        table_name = "connect_todos"


test_db.connect()
test_db.create_tables([User, TodoItem, Tag, ConnectTodo])
