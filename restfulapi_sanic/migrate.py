# import psycopg2
from peewee import *
from models import test_db, User, TodoItem, Tag, ConnectTodo
# from models import *


def migrate():
    ConnectTodo.drop_table(cascade=True)
    TodoItem.drop_table(cascade=True)
    Tag.drop_table(cascade=True)
    User.drop_table(cascade=True)
    test_db.create_tables([User, TodoItem, Tag, ConnectTodo])

    User.create(user_name="hayakawa", id=1)
    User.create(user_name="sujan", id=2)
    User.create(user_name="mazin", id=3)

    TodoItem.create(todo_title="Nero!", user_id=1)  # 1
    TodoItem.create(todo_title="detabase", user_id=2)  # 2
    TodoItem.create(todo_title="python", user_id=3)
    TodoItem.create(todo_title="python2", user_id=1)
    TodoItem.create(todo_title="sanic", user_id=1)
    TodoItem.create(todo_title="html", user_id=2)
    TodoItem.create(todo_title="css", user_id=3)

    Tag.create(tag_name="Programming", id=1)
    Tag.create(tag_name="homework", id=2)
    Tag.create(tag_name="job", id=3)
    Tag.create(tag_name="others", id=4)

    ConnectTodo.create(todo=1, tag=1)
    ConnectTodo.create(todo=1, tag=2)
    ConnectTodo.create(todo=2, tag=1)
    ConnectTodo.create(todo=2, tag=3)
    ConnectTodo.create(todo=2, tag=4)
    ConnectTodo.create(todo=3, tag=1)
    ConnectTodo.create(todo=6, tag=4)
    ConnectTodo.create(todo=7, tag=1)
    ConnectTodo.create(todo=2, tag=3)
    ConnectTodo.create(todo=5, tag=2)
    ConnectTodo.create(todo=3, tag=4)


if __name__ == "__main__":
    migrate()
