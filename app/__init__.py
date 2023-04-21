"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch134o33cv203bui8o0g-a",
        database="todo_8pu6",
        user="root",
        password="27DPXWeqhcjiCzUXmISxCUZYzWkOoXnZ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
