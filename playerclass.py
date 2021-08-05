import sqlite3

class Playerclass:
    def __init__(self, name, hd, sp, bab, saves, sig, spells):
        self.name = name
        self.hit_die = hd
        self.health = hd
        self.skill_points = sp
        self.skills = sp * 4
        self.bab = bab
        self.full_bab = ""
        self.saves = saves
        self.full_saves = [0, 0, 0]
        self.signature = sig
        self.spells = spells
        self.level = 1

    def levelSet(self, lev):
        self.level = lev
        x = int(self.level / 4)
        for _ in range(x):
            pass
        self.health = self.hit_die * lev
        self.skills = (self.skill_points * 4) + (self.skill_points * (lev - 1))
        self.saveline()
        self.babline()

    def levelUp(self):
        self.level += 1
        self.health += self.hit_die
        self.skills += self.skill_points
        if self.level % 4 == 0:
            pass
        else:
            pass
        self.saveline()
        self.babline()

    def saveline(self):
        snames = ["fort", "ref", "will"]
        temp = self.saves.split(" ")
        for i in range(3):
            if snames[i] in temp:
                self.full_saves[i] = int((self.level / 2) + 2)
            else:
                self.full_saves[i] = int(self.level / 3)
    
    def babline(self):
        if self.bab == "good":
            temp = self.level
        elif self.bab == "average":
            temp = int(self.level * 0.75)
        elif self.bab == "poor":
            temp = int(self.level / 2)
        
        while True:
            self.full_bab += "+" + str(temp)
            if temp > 5:
                temp -= 5
                self.full_bab += "/"
            else:
                break
                

"""
So, before I go too insane with this, let's actually try to think things out.
D&D Character creator.
What are we doing.
Well, you need a name, stats, race, class, level, alignment, skills, feats, abilities, inventory, and spells.
    Name is a name
    Stats is a list of numbers
    Race modifies stats and maybe gives abilities or a feat or skills
    Class has BAB, Saves, Abilities, and Spells
        Level relates to class
        Class determines proficient skills
    Alignment is 1 of 9 choices
    Skills is a bunch of numbers
    Feats are selected off a list
        Abilities are granted by Race or Class
    Inventory is just a bunch of strings
    Spells is probably just a list of numbers.
"""

    #Let's try to keep things basic. 
        #Stats, Races, Classes, Levels, BAB, Saves, Spellcasting, Alignment

        #Feats is a giant pile of things, as is skills, as is abilities, as is inventory

        #When we have the basics done we can revisit the rest.

def classChoose(con, cur):
    cur.execute("select * from classes")
    class_data = cur.fetchall()
    class_names = []
    for row in class_data:
        print(row)
        class_names.append(row[0])
    while True:
        print("Select character class. (Enter Class name)")
        x = input(">")
        if x in class_names:
            break
        else:
            print("Invalid Input.")
    
    cur.execute("select * from classes where cname = '%s'" % x)
    choice = cur.fetchone()
    return choice

def testing():
    con = sqlite3.connect('testing.db')
    cur = con.cursor()

    sql_file = open("database.sql")
    sql_as_string = sql_file.read()
    cur.executescript(sql_as_string)
    cur.execute("select * from classes")
    a = cur.fetchone()
    if a == None:
        sql_file2 = open("insert.sql")
        sql_as_string2 = sql_file2.read()
        cur.executescript(sql_as_string2)

    z = classChoose(con, cur)
    print("Class Chosen:")
    print(z)

#testing()