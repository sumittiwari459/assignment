from tkinter import *
from tkinter import messagebox

def login():
    username=entry1.get()
    password=entry2.get()

    if (username=="",password==""):
        messagebox.showinfo("","Blank not Allowed")

    if(username=="sumit",password=="123"):
        messagebox.showinfo("","Login success")
        
    else: messagebox.showinfo("Incorrect username and password")

window=Tk()

window.title("login")
window.geometry("300x200")

global entry1
global entry2
l1=Label(window,text="USERNAME")
l1.place(x=40,y=25)
l1=Label(window,text="PASSWORD")
l1.place(x=40,y=70)

entry1=Entry(window,bd=5)
entry1.place(x=140,y=20)

entry2=Entry(window,bd=5)
entry2.place(x=140,y=70)

Button(window,text="login",height=3,width=12,bd=6,bg='blue',command=login).place(x=100,y=120)

window.mainloop()