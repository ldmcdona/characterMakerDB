import sqlite3

def raceChoose(con, cur):
    cur.execute("select * from races")
    race_data = cur.fetchall()
    race_names = []
    for row in race_data:
        print(row)
        race_names.append(row[0])
    while True:
        print("Select character race. (Enter Race name)")
        x = input(">")
        if x in race_names:
            break
        else:
            print("Invalid Input.")
    
    cur.execute("select * from races where rname = '%s'" % x)
    choice = cur.fetchone()
    return choice

def testing():
    con = sqlite3.connect('testing.db')
    cur = con.cursor()

    sql_file = open("database.sql")
    sql_as_string = sql_file.read()
    cur.executescript(sql_as_string)
    cur.execute("select * from races")
    a = cur.fetchone()
    if a == None:
        sql_file2 = open("insert.sql")
        sql_as_string2 = sql_file2.read()
        cur.executescript(sql_as_string2)

    z = raceChoose(con, cur)
    print("Race Chosen:")
    print(z)

#testing()