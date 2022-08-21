"""  Black Jack Game """
#m
import cards,games

class Bj_card(cards.Positionable_card):
    ACE_VALUE=1
    @property
    def value(self):
        if self.face_is_up==True:
            v=cards.Card.RANKS.index(self.rank)+1
            if v>10:
                v=10
        else:
            v=None
        return v




class Bj_deck(cards.Deck):
    def populate(self):
        for suit in Bj_card.SUITS:
            for rank in Bj_card.RANKS:
                self.cards.append(Bj_card(rank, suit))

    def deal(self,players,per_hand=1): #accepts a LIST for players
        for rounds in range(per_hand):
            for player in players:
                if not self.cards:
                    print("Cards finished, New deck is opened")
                    self.populate()
                top_card=self.cards[0]
                self.give(top_card,player)
               
                    


class Bj_hand(cards.Hand):
    
    def __str__(self):
        txt=super(Bj_hand,self).__str__()
        if self.total:
            txt+="("+str(self.total)+")"
        return txt

    @property
    def total(self):
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value: return None

        #sum of the values
        t=0
        for card in self.cards:
            t+=card.value
        # determine if the hand contains an Ace.
        # The player would want to add 10 once even if he has more Ace's.
        #Because if he add more he looses.
        contains_ace=False
        for card in self.cards:
            if card.value==Bj_card.ACE_VALUE : contains_ace=True

        if contains_ace and t<=11:
            t+=10
            
        return t

    
    @property
    def is_busted(self):
        return self.total>21
        
        

class Bj_player(Bj_hand):
    def __init__(self,person):
        super(Bj_player,self).__init__(person[0])
        self.money=person[1]
        self.bet=0
    
    def is_hitting(self):
        response=games.ask_yn(self.name+" do you want a hit?")
        return response=="y"

    def bust(self):
        print(self.name," busts!")
        self.lose()

    def lose(self):
        #print(self.name," loses!")
        print(self.name," lost ", self.bet," dollors ! ")
        self.money-=self.bet
        print("Now ",self.name," has ", self.money," dollors ! ")
        if self.money==0: print(self.name," has no money now ! ")

    def win(self):
        #print(self.name," wins!")
        print(self.name," Won ", self.bet," dollors ! ")
        self.money+=self.bet
        print("Now ",self.name," has ", self.money," dollors ! ")
        
        
        
    def push(self): print(self.name, "pushes.")


class Bj_dealer(Bj_hand):
    
    def is_hitting(self): return self.total < 17
    
    def bust(self): print(self.name, "busts.")
    
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class Bj_game(object):
    def __init__(self,persons):
        self.players=[]
        for person in persons:
            self.players.append(Bj_player(person))
        self.dealer=Bj_dealer("Dealer")
        self.deck=Bj_deck("Deck")
        self.deck.populate()
        self.deck.shuffle()
        

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted:
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted and player.is_hitting():
            self.deck.deal([player])
            print(player)
        if player.is_busted:
            player.bust()
    def play(self):
        # deal initial 2 cards to everyone
        for player in self.players:
            self.ask_bet(player)
        self.deck.deal(self.players+[self.dealer],per_hand=2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card() # reveal dealer's first

        if not self.still_playing: # since all players have busted, 
            print(self.dealer)     #just show the dealer's hand
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted: # everyone still playing wins
                for player in self.still_playing:
                    player.win()
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else: player.push()
        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()

    def ask_bet(self,player):
        player.bet=int(games.ask_num(str(player)+ "  How much dollors are"+\
                            "you going to bet?(from 0 upto your money)",0,player.money))
        
    

        
#main function
def main():
    print("\t\tWelcome to Blackjack!\n")
    persons = []
    number = int(games.ask_num("How many players? : ", low = 1, high = 7))
    for i in range(number):
        name = input("Enter player name: ")
        money=int(games.ask_num("Enter player money: ",0,1000000))
        persons.append((name,money)) #a tuple is created and appended to names list
    print()
    game = Bj_game(persons)
    again = None
    while again != "n":
        game.play()
        again = games.ask_yn("\nDo you want to play again?: ")


#root        
main()
input("\n\nPress the enter key to exit.")
    
        
    














