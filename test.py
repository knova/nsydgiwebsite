import sqlite3

con = sqlite3.connect("nsydgiwebsite/models/data.db")
cur = con.cursor()
cur.execute('SELECT NAME FROM Navigation ORDER BY ord;')
row = cur.fetchall()
navigation = []
for entry in row:
    entry = "".join(entry)
    cur.execute('SELECT NAME FROM Pages WHERE CATEGORY = ? ORDER BY ord;', [entry])
    submenu = cur.fetchall()
    submenu = ["".join(a) for a in submenu]
    navigation.append((entry, submenu))
print(navigation)