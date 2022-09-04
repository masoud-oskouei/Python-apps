"""Full Critter Program"""


class Critter(object):
    import random

    def __init__(self, name):
        self.name = name
        self.hunger = random.randrange(0, 8)
        self.boredom = random.randrange(0, 8)

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
        # print("pass time executed")

    @property
    def mood(self):
        unhappiness = self.boredom + self.hunger
        # print("unhappiness  =  ",unhappiness)
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print(
            self.name,
            "says: '  I'm ",
            self.name,
            "and I feel ",
            self.mood,
            "now.  '",
        )
        self.__pass_time()

    def eat(self, food=4):
        print(self.name, "says: '  Oh! It hit the spot !   Thanx !  '")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print(self.name, "says:' Wheeeee ! '")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def __str__(self):
        desc = ""
        desc += "Name : "
        desc += self.name
        desc += "\nHunger Level : "
        desc += str(self.hunger)
        desc += "\n Bordom Level : "
        desc += str(self.boredom)
        desc += "\n Mood Status : "
        desc += self.mood
        return desc


def main():
    crits = []
    screen_clear()
    print("         -= Welcome to PET CARETAKER program =-  ")
    crit_name = input("\n Please enter your much loved pet name and press Enter: ")
    crits.append(Critter(crit_name))
    choice = None

    while choice != "0":

        print(
            """
            
             --= Menu =--
             
             0 - Quit
             1 - Listen to your pets
             2 - Feed your pets
             3 - Play with your pets
             4 - Creat another pet

             """
        )
        choice = input(
            "Please enter the number beside your choice from above menu and press enter:   "
        )
        screen_clear()
        if choice == "0":
            print("Bye Bye")
        elif choice == "1":
            for crit in crits:
                crit.talk()
        elif choice == "2":
            food = 0
            while not (4 <= food <= 14):
                food = int(input("How much food are you giving (4-14)?"))
            for crit in crits:
                crit.eat(food)

        elif choice == "3":
            fun = 0
            while not (4 <= fun <= 14):
                fun = int(input("How long  are you playing with it? (4-14)?"))
            for crit in crits:
                crit.play(fun)

        elif choice == "4":
            screen_clear()
            crit_name = input("Please type your new pet's name and press Enter: ")
            crits.append(Critter(crit_name))

        elif choice == "100":
            for crit in crits:
                print(crit)

        else:
            print("Please enter a valid choice ")


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")


# root
import random
import os

main()
input("\n\n Press the enter key to exit.")
