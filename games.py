#""" Games Module """

class Player(object):
    def __init__(self,name,score=0):
        self.name=name
        self.score=score

    def __str__(self):
        strng=self.name+"\t"+str(self.score)
        return strng
def ask_yn(question):
    ans=""
    while ans.lower() not in["y","n"]:
        ans=input(question+" Enter y or n ... ")
    return ans.lower()

def ask_num(question,low,high):
    
    num=None
    # we include the high limit itself
    while num not in range(low,high+1):
        try:
            num=int(input(question+"\n Choose a number "\
                      +str(low)+" to "+str(high)+" ... "))
            if  num not in range(low,high+1):
                print("That was not in range!")
                num=None
        except:
            print("That was not a number!")
            num=None
        
            
    return str(num)

if __name__=="__main__": print("You executed this module "+\
                               "separately. It is meant to "+ \
                               "be used inside a program.") 
        
#root
#print("you answered: "+ask_yn("Are You fine?"))
#print("you answered: "+ask_num("Choose a Number from 1 to 10",1,10))
