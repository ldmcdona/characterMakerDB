import random

def main():
    attributes = [0, 0, 0, 0, 0, 0]
    random.seed()
    print("Welcome to the D&D Character Creator.")
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
    else:
        print("Your alignment is", order, moral)

main()