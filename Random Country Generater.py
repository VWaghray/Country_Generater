from tkinter import *
import random 

root = Tk()

root.title("Country Capitals")
root.geometry('400x400')

Text = Entry(root)
Text1 = Entry(root)
label = Label(root)
label1 = Label(root)
label2 = Label(root)
label3 = Label(root)


list1 = []
list2 = []

def add():
    Name = Text.get()
    list1.append(Name)
    label["text"] = "Country Name: " + str(list1)
    Name1 = Text1.get()
    list1.append(Name1)
    label1["text"] = "City Name: " + str(list2)
    
    
def random_friend():
    lenght = len(list1)
    lenght1 = len(list2)
    random_no = random.randint(0, lenght-1)
    random_no1 = random.randint(0, lenght1-1)
    Friend = list1[random_no]
    label2["text"]="Random Country" + str(Friend)
    Friend1 = list1[random_no1]
    label3["text"] = "Random City: " + str(Friend1)
    
Text.place(relx=0.5, rely=0.2, anchor=CENTER)
Text1.place(root, relx=0.5, rely=0.3, anchor=CENTER)
btn = Button(root, text = 'Display Country and City Name', command=add)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
label.place(relx=0.5, rely=0.5, anchor=CENTER)
label1.place(relx=0.5, rely=0.6, anchor=CENTER)
btn1 = Button(root, text = 'Display Country and City Name Randomly', command=random_friend)
btn1.place(relx=0.5, rely=0.7, anchor=CENTER)
label2.place(relx=0.5, rely=0.8, anchor=CENTER)
label3.place(relx=0.5, rely=0.9, anchor=CENTER)
    

root.mainloop()
