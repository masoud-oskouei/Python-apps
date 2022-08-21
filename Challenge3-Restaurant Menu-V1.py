"Restaurant Menu App"
from tkinter import*

class Item(object):
    def __init__(self,master,dsc,unit_price=0):
        self.entry_box=Entry(master,width=3,relief="raised")
        self.v=BooleanVar()
        self.v.set(False)
        self.check_button=Checkbutton(master,text=dsc,variable=self.v,borderwidth=4,relief="raised")
        self.unit_price=unit_price
        self.unit_price_label=Label(master,text="$"+str(self.unit_price),relief="raised")




class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.label1=Label(self,text=
              "please tick what you want and enter the quantity"
              ,relief="raised")
        self.label1.grid(row=0,column=0,columnspan=2)
        self.label2=Label(self,text=
              "Quantity:",relief="raised")
        self.label2.grid(row=1,column=0,sticky=W)

        self.label3=Label(self,text=
              "Food Item:",relief="raised")
        self.label3.grid(row=1,column=1,sticky=W)
        
        
        #Feed unit prices and food names here:
        self.item_price_list=[10,15,12,8]
        self.item_food_list=["Potatoes   \t\t","Mushroomanious\t\t","Deliciousina\t\t","Oh My God Food\t\t"]
        self.item_list=[]
        for i in range(4):
            self.item_temp=Item(self,self.item_food_list[i],self.item_price_list[i])
            self.item_temp.entry_box.grid(row=i+2,column=0,stick=W)
            self.item_temp.check_button.grid(row=i+2,column=1,sticky=W)
            self.item_temp.unit_price_label.grid(row=i+2,column=3,sticky=W)
            self.item_list.append(self.item_temp)
        
        
            
        
        
        self.space_1=Label(self,text="    ")
        self.space_1.grid(row=6,column=0)
        self.space_2=Label(self,text="    ")
        self.space_2.grid(row=6,column=1)
        self.quantity_submit=Button(self,text="Submit",command=self.calc)
        self.quantity_submit.grid(row=6,column=2)

        self.space_3=Label(self,text="    ")
        self.space_3.grid(row=7,column=1)

        Label(self,text="Total:",relief="raised").grid(row=8,column=1)
        self.total_text=Text(self,width=3,height=1)
        self.total_text.grid(row=8,column=2)

    def calc(self):
        print("self.item_list[1].entry_box.get():= \n",self.item_list[1].entry_box.get())
        self.total=0
        for item in self.item_list:
            if item.v.get():
                try:
                    self.total+=int(item.entry_box.get())*item.unit_price
                except:
                    self.total+=0
                    
        self.total_text.delete(0.0,END)
        self.total_text.insert(0.0,str(self.total))

    
        













#main
root=Tk()
#root.geometry("700x300")
root.title("Menu for Restaurant")
app=Application(root)
root.mainloop()
