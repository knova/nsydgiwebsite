from tornado import Server
from template_engine import render
from pages import *
import sqlite3

from os import path
import sys
sys.path.append(path.dirname(path.realpath(__file__)))

def index(response):
    values = {
        "navigation": navigation(),
        "title": "derp",
        }
    render('index.html', response, values)

if __name__ == "__main__":
    server = Server()
    server.register("/", index)

server.run()
