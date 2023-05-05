"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaauljhp8u791h1mpng-a.oregon-postgres.render.com",
        database="todo_ujuy",
        user="root",
        password="9yjAl0uQluDM5OSM5yGEYgFz5D48TfH2")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
