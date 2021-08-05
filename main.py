import random
from playerclass import *
from character import *

def statline():
    attributes = [0, 0, 0, 0, 0, 0]
    random.seed()
    print("Rolling Stats:")
    while True:
        print("How many dice do you want to roll for each attribute?")
        try:
            dice = int(input(">"))
            if dice < 1 or dice > 5:
                10 / 0
        except:
            print("Please enter a number between 1 and 5")
        else:
            break

    while True:
        print("What is the minimum value for each die?")
        try:
            low = int(input(">"))
            if low < 1 or low > 6:
                10 / 0
        except:
            print("Please enter a number between 1 and 6")
        else:
            break
    
    for i in range(6):
        rolls = []
        final = 0
        for _ in range(dice):
            rolls.append(random.randint(low, 6))
        rolls.sort(reverse=True)
        print(rolls)
        final = rolls[0] + rolls[1] + rolls[2]
        attributes[i] = final

    print("Your attribute rolls are:", attributes)

    attributeList = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    x = attributes.copy()
    y = 0
    while y < 6:
        print("Which roll would you like for " + attributeList[y] + "?")
        print(x)
        try:
            z = int(input(">"))
            if z < 0 or z > len(x):
                10 / 0
        except:
            print("Choose the index of the roll you wish to choose, with the first number being index 0.")
        else:
            #print("Flag", len(attributes), y, len(x), z)
            attributes[y] = x[z]
            x.pop(z)
            y += 1
        
    print("Your attributes are now:", attributes)
    return attributes

def alignment():
    print("Choosing Alignment:")
    while True:
        print("Is your character Lawful, Neutral, or Chaotic?")
        order = input(">")
        if order == "Lawful" or order == "Neutral" or order == "Chaotic":
            break
        else:
            print("Invalid input.")

    while True:
        print("Is your character Good, Neutral, or Evil?")
        moral = input(">")
        if moral == "Good" or moral == "Neutral" or moral == "Evil":
            break
        else:
            print("Invalid input.")

    if order == moral:
        print("Your alignment is True Neutral")
        x = "True Neutral"
    else:
        print("Your alignment is", order, moral)
        x = order + " " + moral
    
    return x

def main():
    print("Welcome to the D&D Character Creator.")
    newchar = Character()
    newchar.set_stats(statline())
    newchar.set_align(alignment())

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
    
    testing = classChoose(con, cur)
    #print(testing, type(testing))

    newclass = Playerclass(testing[0], testing[1], testing[2], testing[3], testing[4], testing[5], testing[6])
    print("Testing -----------------")
    print("What level is your character?")
    lev = int(input(">"))
    newclass.levelSet(lev)
    print(newclass.full_bab, newclass.full_saves)

    #This project is a bit of a confused mess, but I'm working on it.
    #Character is the top level. It hold the stat line, the class (or classes), the race, the alignment, the feats, the inventory, and the total level
    #Class is mid level. It holds the bab, the saves, their own hit dice and skills, signature abilitys and spells, and specific level
    #Race is just kind of a modifyer that messes with everything. Might make mid-level?
    #Rest is to be determined.

main()