import sqlite3

def main():
    con = sqlite3.connect('testing.db')
    cur = con.cursor()
    sql_file = open("database.sql")
    sql_as_string = sql_file.read()
    cur.executescript(sql_as_string)

    print("Database testing.")
    while True:
        print("Enter 'C' to add a class. Enter 'F' to add a feat.\nEnter 'R' to add a race. Enter 'V' to view.\nEnter 'Q' to quit.")
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
    na = input(">")
    while True:
        print("Enter class Hit-Dice. (4-12)")
        hd = int(input(">"))
        if hd >= 4 and hd <= 12:
            break
        else:
            print("Invalid input.")
    while True:
        print("How many skill points does the class get?. (2-8)")
        sk = int(input(">"))
        if sk >= 2 and sk <= 8:
            break
        else:
            print("Invalid input.")
    while True:
        print("Enter Base Attack Bonus. (good/average/poor)")
        b = input(">")
        if b == "good" or b == "average" or b == "poor":
            break
        else:
            print("Invalid input.")
    while True:
        print("Is Fortitude a good save for this class? (Y/N)")
        c1 = input(">")
        if c1 == "Y" or c1 == "N":
            break
        else:
            print("Invalid input.")
    while True:
        print("Is Reflex a good save for this class? (Y/N)")
        c2 = input(">")
        if c2 == "Y" or c2 == "N":
            break
        else:
            print("Invalid input.")
    while True:
        print("Is Will a good save for this class? (Y/N)")
        c3 = input(">")
        if c3 == "Y" or c3 == "N":
            break
        else:
            print("Invalid input.")
    print("What is the classes signature ability?")
    ab = input(">")
    while True:
        print("Is the class a spellcaster? (Y/N)")
        sp = input(">")
        if sp == "Y" or sp == "N":
            break
        else:
            print("Invalid input.")

    saves = ""
    if c1 == "Y":
        saves += "fort"
    if c2 == "Y":
        if saves != "":
            saves += " ref"
        else:
            saves += "ref"
    if c3 == "Y":
        if saves != "":
            saves += " will"
        else:
            saves += "will"    

    if saves == "":
        saves = None
    if ab == "":
        ab = None

    if sp == "Y":
        sp = 1
    else:
        sp = 0

    e = [na, hd, sk, b, saves, ab, sp]
    return e

main()