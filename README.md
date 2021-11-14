# RESTful API with Sanic

Sanic を用いて RESTful API を実装したい.

## TodoList API

## File structure

```

RESTfulAPI_sanic
├── README.md
├── README.rst
├── poetry.lock
├── pyproject.toml
├── restfulapi_sanic
│   ├── __init__.py
│   ├── __pycache__
│   │   └── models.cpython-38.pyc
│   ├── main.py
│   ├── migrate.py
│   └── models.py
└── tests
    ├── __init__.py
    └── test_restfulapi_sanic.py

```

---

## How to start this project

```sh
    $ cd restfulapi_sanic/
    $ python3 main.py

```

localhost:8081 に立てた PostgresSQL Server に接続するように指定している.

---

## API output

```json
{
  "todos": [
    {
      "id": 1,
      "todo_title": "Nero!",
      "user": {
        "id": 1,
        "name": "user1"
      },
      "tag": [
        {
          "id": 1,
          "name": "Programming"
        },
        {
          "id": 2,
          "name": "homework"
        }
      ]
    },
                ・
                ・
                ・
  ]
}
```
