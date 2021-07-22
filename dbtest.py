import sqlite3

def main():
    con = sqlite3.connect('testing.db')
    cur = con.cursor()
    sql_file = open("database.sql")
    sql_as_string = sql_file.read()
    cur.executescript(sql_as_string)

    print("Database testing.")
    while True:
        print("Enter 'C' to add a class. Enter 'F' to add a fear.\nEnter 'R' to add a race. Enter 'V' to view.\nEnter 'Q' to quit.")
        x = input(">")
        if x == "C":
            y = addClass()
            cur.execute("insert into classes values (?, ?, ?, ?, ?, ?, ?)", (y[0], y[1], y[2], y[3], y[4], y[5], y[6]))
            con.commit()
        elif x == "F":
            pass
        elif x == "R":
            pass
        elif x == "V":
            cur.execute("select * from classes")
            print(cur.fetchall())
        elif x == "Q":
            con.close()
            break
        else:
            print("Invalid command. Please try again.")


def addClass():
    print("Enter class name.")
    a = input(">")
    while True:
        print("Enter Base Attack Bonus. (good/average/poor)")
        b = input(">")
        if b == "good" or b == "average" or b == "poor":
            break
        else:
            print("Invalid input.")
    while True:
        print("Enter Fortitude Save. (0/1)")
        c1 = int(input(">"))
        if c1 == 0 or c1 == 1:
            break
        else:
            print("Invalid input.")
    while True:
        print("Enter Reflex Save. (0/1)")
        c2 = int(input(">"))
        if c2 == 0 or c2 == 1:
            break
        else:
            print("Invalid input.")
    while True:
        print("Enter Will Save. (0/1)")
        c3 = int(input(">"))
        if c3 == 0 or c3 == 1:
            break
        else:
            print("Invalid input.")
    print("Abilities are not yet included.\nN/A")
    while True:
        print("Is the class a spellcaster? (0/1)")
        d = int(input(">"))
        if d == 0 or d == 1:
            break
        else:
            print("Invalid input.")

    e = [a, b, c1, c2, c3, "N/A", d]
    return e

main()