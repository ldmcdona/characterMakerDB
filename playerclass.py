class playerclass:
    def __init__(self, name, bab, saves, spells):
        self.name = name
        self.level = 1
        self.bab = bab
        self.full_bab = ""
        self.saves = saves
        self.full_saves = [0, 0, 0]
        self.spells = spells

    def levelUp(self):
        if self.level % 4 == 0:
            pass
        else:
            pass

    def saveline(self):
        for i in range(3):
            if self.saves[i] == 1:
                self.full_saves[i] = (self.level / 2) + 2
            else:
                self.full_saves[i] = (self.level / 3)
    
    def babline(self):
        if self.bab == "good":
            temp = self.level
        elif self.bab == "average":
            temp = (self.level * 0.75)
        elif self.bab == "poor":
            temp = (self.level / 2)
        
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

def classChoose(con, cur):
    cur.execute("select * from classes")
    class_data = cur.fetchall()

    #Gonna stop you right there. 
    #Classes are probably gonna need individual tables. Just like the PHB.
    #Probably have a table for brief class info for selection/short hand.
    #Need to do some foriegn key stuff there. 
    #This will also solve the ability problem. Just a column of the table.

    #Races are gonna have a lot of ability text since it'll included darkvision and saves and stuff.
    #Also gonna have to properly plan out how to organize data for later use. line.split("_") sort of thing.