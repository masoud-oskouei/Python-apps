"""Full Critter Program"""
class Critter(object):
    import random
    def __init__(self,name):
        self.name=name
        self.hunger=random.randrange(0,8)
        self.boredom=random.randrange(0,8)

    def __pass_time(self):
        self.hunger+=1
        self.boredom+=1
        #print("pass time executed")

    @property
    def mood(self):
        unhappiness=self.boredom+self.hunger
        #print("unhappiness  =  ",unhappiness)
        if unhappiness<5:
            m="happy"
        elif 5<=unhappiness<=10:
            m="okay"
        elif 11<=unhappiness<=15:
            m="frustrated"
        else:
            m="mad"
        return m

    def talk(self):
        print("I'm ",self.name,"and I feel ", self.mood,"now.\n")
        self.__pass_time()

    def eat(self,food=4):
        print("Oh! It hit the spot !   Thanx ! ")
        self.hunger-=food
        if self.hunger<0:
            self.hunger=0
        self.__pass_time()

    def play(self,fun=4):
        print("Wheeeee ! ")
        self.boredom-=fun
        if self.boredom<0:
            self.boredom=0
        self.__pass_time()

    def __str__(self):
        desc=""
        desc+="Name : "
        desc+=self.name
        desc+="\nHunger Level : "
        desc+=str(self.hunger)
        desc+="\n Bordom Level : "
        desc+=str(self.boredom)
        desc+="\n Mood Status : "
        desc+=self.mood
        return desc


def main():
    crits=[]
    crit_name=input("What is your critter's name?: ")
    crits.append(Critter(crit_name))
    choice=None
    while choice!="0":
        
        print("""
             --= Critter Caretaker =--
             0 - Quit
             1 - Listen to your critter
             2 - Feed your critter
             3 - Play with your critter
             4 - Creat another critter

             """)
        choice=input("PLEASE ENTER YOUR CHOICE")
        if choice=="0":
            print("Bye Bye")
        elif choice=="1":
            for crit in crits:
                crit.talk()
        elif choice=="2":
            food=0
            while not (4<= food <=14):
                food=int(input("How much food are you giving (4-14)?"))
            for crit in crits:
                crit.eat(food)
            
        elif choice=="3":
            fun=0
            while not (4<= fun <=14):
                fun=int(input("How long  are you playing with it? (4-14)?"))
            for crit in crits:
                crit.play(fun)

        elif choice=="4":
            crit_name=input("What is your new critter's name?: ")
            crits.append(Critter(crit_name))
            
        elif choice=="100":
            for crit in crits:
                print(crit)
            
        else:
            print("Please enter a valid choice ")
            


#root
import random
main()
input("\n\n Press the enter key to exit.")
        
        

        
    
        

        













