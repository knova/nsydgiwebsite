import sqlite3

def navigation():
    con = sqlite3.connect("./models/data.db")
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
    con.close()
    return navigation
