from tornado import Server
from template_engine import render
import sqlite3

from os import path
import sys
sys.path.append(path.dirname(path.realpath(__file__)))

def index(response):
    con = sqlite3.connect("models/data.db")
    cur = con.cursor()
    cur.execute('SELECT NAME FROM Navigation ORDER BY ord;')
    row = cur.fetchall()
    response.write("""<html><head><title>derp</title></head><body>
        "hello world"
        {{ row }}
    </body></html>""")

if __name__ == "__main__":
    server = Server()
    server.register("/", index)

server.run()