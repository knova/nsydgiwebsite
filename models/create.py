import sqlite3 as lite

db = lite.connect('data.db')
print("creating db...")
cur = db.cursor()    

cur.execute("""CREATE TABLE Navigation (
    NAME TEXT UNIQUE NOT NULL,
    ORD INTEGER,
    CONTENT TEXT,
    PRIMARY KEY (name)
);""")
cur.execute("""CREATE TABLE Pages (
    NAME TEXT UNIQUE NOT NULL,
    CATEGORY TEXT NOT NULL,
    ORD INTEGER,
    CONTENT TEXT,
    PRIMARY KEY (name)
);""")

#navigation = ["Home", "Derp", "Pufferfish"]

#cur.executemany("INSERT INTO Navigation VALUES(?, NULL, '')", navigation)
cur.execute("INSERT INTO Navigation VALUES ('Home', 1, '')")
cur.execute("INSERT INTO Navigation VALUES ('Derp', 2, '')")
cur.execute("INSERT INTO Navigation VALUES ('Pufferfish', 3, '')")
cur.execute("INSERT INTO Pages VALUES ('One', 'Derp', 2, '1DerpPage')")
cur.execute("INSERT INTO Pages VALUES ('Two', 'Derp', 1, '2HerpPage')")
cur.execute("INSERT INTO Pages VALUES ('Three', 'Pufferfish', 1, '3SmurfPage')")
cur.execute("INSERT INTO Pages VALUES ('Four', 'Pufferfish', 2, '4BlerpPage')")
cur.execute("INSERT INTO Pages VALUES ('Five', 'Derp', 2, '5SpurfPage')")

db.commit()
db.close()
print("connection closed.")
