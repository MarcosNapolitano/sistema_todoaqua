"""
Warning Never, never, NEVER use Python string concatenation (+) or string
parameters interpolation (%) to pass variables to a SQL query string.
Not even at gunpoint.

The correct way to pass variables in a SQL command is using the second
argument of the execute() method:

>>> SQL = "INSERT INTO authors (name) VALUES (%s);" # Note: no quotes
>>> data = ("O'Reilly", )
>>> cur.execute(SQL, data) # Note: no % operator

"""

from os import environ
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from psycopg2.extensions import cursor
from typing import Callable, Concatenate, ParamSpec, TypeVar
from functools import wraps

P = ParamSpec("P")
R = TypeVar("R")

load_dotenv()

password = environ.get("PASS")


# to do: implement Error messagebox and try catch
def connect_db(
    func: Callable[Concatenate[cursor, P], R],
) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:

        conn = psycopg2.connect(
            database="aqua", user="aqua", password=password, port=5432
        )

        # return querys using dict style
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        res = func(cursor, *args, **kwargs)
        conn.commit()
        conn.close()

        return res

    return wrapper


@connect_db
def basic_exec(cursor, query, param):
    cursor.execute(query, param)
    return "Done"


@connect_db
def ultima_id(cursor, query):

    cursor.execute(query)
    return cursor.fetchone()[0]


@connect_db
def get_single(cursor, query, param):

    cursor.execute(query, param)
    return cursor.fetchone()


@connect_db
def get_all(cursor, query, param=False):

    if param:
        cursor.execute(query, param)
    else:
        cursor.execute(query)

    return cursor.fetchall()


@connect_db
def update_single(cursor, query, param):

    cursor.execute(query, param)
    return "Done"


# query = "SELECT * FROM CONCEPTOS_PRESUPUESTO WHERE ID_PRESUPUESTO = %s;"
# query = "UPDATE CLIENTES SET NIF = %s WHERE ID_CLIENTE = %s;"
# data = (4, )
# print(get_single(query, data)[23].split(";"))
