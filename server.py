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
    navigation = ""
    for entry in row:
        entry = "".join(entry)
        cur.execute('SELECT NAME FROM Pages WHERE CATEGORY = ? ORDER BY ord;', [entry])
        submenu = cur.fetchall()
        if submenu:
            submenu = "<li>" + "</li><li>".join(["".join(a) for a in submenu]) + "</li>"
        else:
            submenu = ""
        submenu = """<ul class='navi'>
            <li class='navi-heading'><em>""" + entry + "</em></li>"  + submenu + "</li></ul>"
        navigation += (submenu)
    print(navigation)
    values = {"derp": navigation}
    #print(row)
    render('test.html', response, values)
    con.close()

if __name__ == "__main__":
    server = Server()
    server.register("/", index)

server.run()