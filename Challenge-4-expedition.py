"""Expedition Game"""
"""By M@tt M0n0"""
import games
def ask_fb():
    ans=""
    while ans.lower() not in["f","b"]:
        ans=input("\n\nYou go forward or backward? Enter f or b ... ")
    return ans.lower()



class Place(object):
    
    
    def __init__(self,location):
        #a location is a tuple containing charactristics of the location
        self.name=location[0]
        self.feature=location[1]
        self.weather=location[2]
        self.order=location[3]

    def narrate(self):
        print("\n-----------------------------------------------------------------")
        print("|\t\t- = Now you are in ",self.name," ! = - \t\t|")
        print("|\tThere is a ",self.feature," here. Very scenic !\t\t|")
        print("|\tNow it is ",self.weather," Enjoy !\t\t\t\t|")
        print("-----------------------------------------------------------------")

class Game(object):
    def __init__(self):
        self.places=[]
        self.position=0

    def go_ahead(self):
        position+=1

    def go_back(self):
        position-=1

def main():
   
    #load info to game object
    locations=[]
    locations.append(("KALAMATA","Waterfall","Rainy",0))
    locations.append(("BALLARAT","Volcano","Sunny",1))
    locations.append(("Hillsvile","Circus  ","Windy",2))
    locations.append(("Melbourne","Casino  ","Mild",3))
    game=Game()
    for location in locations:
        game.places.append(Place(location))

    for place in game.places:
            if game.position ==place.order: place.narrate()
            
    again="y"
    while again=="y":
        ans=ask_fb()
        if ans =="f":
            if game.position==3:
                print("End of the road! You can't go more forward !")
            else: game.position+=1

        if ans =="b":
            if game.position==0:
                print("Start of the road! You can't go more backward !")
            else: game.position-=1

        for place in game.places:
            if game.position ==place.order: place.narrate()
        again=games.ask_yn("\n\n\nDo you want to continue the game?")
    
            
        


#root
main()
input("press enter to exit")
        
            
        
    
    
              

