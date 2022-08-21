""" Guess My Number in a Window!"""
import random

from tkinter import*
class Application(Frame):
    def __init__(self , master):
        super(Application,self).__init__(master)
        self.grid()
        self.main_menu()
        self.to_main="a"
        self.valid_list=range(1,101)
        print(self.valid_list[0],len(self.valid_list))
        self.human_score=0
        
    def main_menu(self):

        self.chosen_btn=StringVar()
        self.chosen_btn.set(None)
        self.r_computer=Radiobutton(self,text="Computer Guesses",\
                    value="computer",
                    variable=self.chosen_btn)
        self.r_computer.grid(row=0,column=0)

        self.r_human=Radiobutton(self,text="Human Guesses",\
                    value="human",
                    variable=self.chosen_btn)
        self.r_human.grid(row=1,column=0,sticky=W)

        self.next_1=Button(self,text="Next",command=self.choose)
        self.next_1.grid(row=2,column=0,sticky=W)
        

        
        
    def choose(self):
        self.human_tries=0
        self.computer_tries=0
        self.humun_is_guessing=True
        if self.chosen_btn.get()=="human":
            self.chosen_btn.set(None)
            #wipe the existing gadgets
            self.r_human.grid_forget()
            self.r_computer.grid_forget()
            self.next_1.grid_forget()
            #draw new gadgets
            self.human_plays()
        if self.chosen_btn.get()=="computer":
            self.chosen_btn.set(None)
            #wipe the existing gadgets
            self.r_human.grid_forget()
            self.r_computer.grid_forget()
            self.next_1.grid_forget()
            #draw new gadgets
            self.computer_plays()
        print("before if>>>    " ,  self.to_main   )
        if self.to_main=="human to main":
            self.to_main=" "
            #wipe the existing gadgets
            self.human_l.grid_forget()
            self.human_entry.grid_forget()
            self.human_message.grid_forget()
            self.human_go_main.grid_forget()
            self.human_tries_show.grid_forget()
            self.human_tries_label.grid_forget()
            self.human_submit.grid_forget()
            #draw new gadgets
            self.main_menu() 

        
        if self.to_main=="computer to main":
            self.to_main=" "
            self.computer_l.grid_forget()
            self.computer_message.grid_forget()
            self.computer_up.grid_forget()
            self.computer_down.grid_forget()
            self.computer_correct.grid_forget()
            self.computer_go_main.grid_forget()
            #draw new gadgets
            self.main_menu() 

        

    def human_plays(self):
        self.answer=30
        #random.randint(1,100)
        self.human_l=Label(self,text="I have chosen a number from 1 to 100. Make a guess: ")
        self.human_l.grid(row=0,column=0,sticky=W)
        Label(self,text="Eneter your guess: ").grid(row=1,column=0,sticky=W)
        self.human_entry=Entry(self,width=2)
        self.human_entry.grid(row=1,column=1,sticky=W)
        self.human_submit=Button(self,text="Submit",command=self.human_guess)
        self.human_submit.grid(row=1,column=2,sticky=W)
        self.human_message=Text(self,width=20,height=5)
        self.human_message.grid(row=2,column=0,sticky=W)
        self.human_tries_label=Label(self,text="Tries: ")
        self.human_tries_label.grid(row=3,column=0,sticky=W)
        self.human_tries_show=Text(self,width=10,height=2)
        self.human_tries_show.grid(row=3,column=1,sticky=W)
        self.human_tries_show.delete(0.0,END)
        print("str(self.human_tries) ",str(self.human_tries))
        self.human_tries_show.insert(0.0,str(self.human_tries))
        #
        self.human_go_main=Button(self,text="Main Menu",
                                  command=self.human_to_main)
        self.human_go_main.grid(row=4,column=0,sticky=W)

        
        
        
        
    def human_guess(self):
        if self.humun_is_guessing:
            if int(self.human_entry.get())not in self.valid_list:
                self.human_message.delete(0.0,END)
                self.human_message.insert(0.0,"\nNot a valid entry!")
                return
                
            if int(self.human_entry.get())<self.answer:
                self.human_message.delete(0.0,END)
                self.human_message.insert(0.0,"\nGo higher!")
                self.human_tries+=1
                self.human_tries_show.delete(0.0,END)
                self.human_tries_show.insert(0.0,str(self.human_tries))
                
            elif int(self.human_entry.get())>self.answer:
                self.human_message.delete(0.0,END)
                self.human_message.insert(0.0,"\nGo lower!")
                self.human_tries+=1
                self.human_tries_show.delete(0.0,END)
                self.human_tries_show.insert(0.0,str(self.human_tries))
            else:
                self.human_message.delete(0.0,END)
                self.human_message.insert(0.0,"\nCorrect! You won! ")
                self.humun_is_guessing=False
                self.human_score+=1
                self.human_tries+=1
                self.human_tries_show.delete(0.0,END)
                self.human_tries_show.insert(0.0,str(self.human_tries))
            if self.human_tries>6:
                self.human_message.insert(0.0,"No more tries left")
                self.humun_is_guessing=False
            
            
            
        
    def human_to_main(self):
        self.to_main="human to main"
        print(self.to_main)
        self.choose()

    def computer_to_main(self):
        print("computer_go_main(self) is executed! ")
        self.to_main="computer to main"
        
        self.choose()
    
    def computer_plays(self):
        self.computer_is_guessing=True
        self.computer_span_min=1
        self.computer_span_max=100
        self.computer_l=Label(
            self,text="Choose a number from1 to 100, Iwill try to guess: ")
        self.computer_l.grid(row=0,column=0,sticky=W)
        self.computer_message=Text(self,width=20,height=5)
        self.computer_message.grid(row=1,column=0,sticky=W)
        self.computer_show_guess()
        self.computer_up=Button(self,text="go up",
                                command=self.go_up)
        self.computer_up.grid(row=2,column=0,sticky=W)
        self.computer_down=Button(self,text="go down",
                                command=self.go_down)
        self.computer_down.grid(row=2,column=1,sticky=W)
        self.computer_correct=Button(self,text="correct",
                                command=self.correct)
        self.computer_correct.grid(row=2,column=2,sticky=W)
        self.computer_tries_label=Label(self,text="Computer tries: "+str(self.computer_tries))
        self.computer_tries_label.grid(row=3,column=0,sticky=W)
        self.computer_go_main=Button(self,text="Main Menu",
                                command=self.computer_to_main)
        self.computer_go_main.grid(row=4,column=0,sticky=W)

      

    def go_up(self):
        if self.computer_is_guessing:
            self.computer_span_min=self.computer_guess_value+1
            self.computer_show_guess()
        

    def go_down(self):
        if self.computer_is_guessing:
            self.computer_span_max=self.computer_guess_value-1
            self.computer_show_guess()

    def computer_show_guess(self):
        self.computer_guess_value=(self.computer_span_min+self.computer_span_max)//2
        self.computer_message.delete(0.0,END)
        self.computer_message.insert(0.0,str(self.computer_guess_value))
        self.computer_tries+=1
        self.computer_tries_label=Label(self,text="Computer tries: "+str(self.computer_tries))
        self.computer_tries_label.grid(row=3,column=0,sticky=W)
        if self.computer_tries>6:
            self.computer_is_guessing=False
            self.computer_message.delete(0.0,END)
            self.computer_message.insert(0.0," Computer lost! ")
            

        
        

    def correct(self):
        if self.computer_is_guessing:
            self.computer_message.delete(0.0,END)
            self.computer_message.insert(0.0,"Oh! the computer wins")
            self.computer_is_guessing=False
            

       
        
    



root=Tk()
root.title("Guess The Number Game")
root.geometry("500x300")
app=Application(root)
root.mainloop()
