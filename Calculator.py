# Importing Tkinter module and * from Tkinter
import tkinter
from tkinter import *

#Setting up main application window
root = Tk()
root.title("First P Calculator")
root.geometry("358x500+600+200")
root.resizable(False, False)
root.configure(bg="#17161b")

label_result= Label(root, width=25, height=2, text="", font=("arial",30))
label_result.pack()

Button(root,text="C", width=2, height=3, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=10, y=100)
Button(root,text="/", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=100,y=100)
Button(root,text="%", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=200,y=100)
Button(root,text="*", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=300,y=100)


Button(root,text="7", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=10,y=200)
Button(root,text="8", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=100,y=200)
Button(root,text="9", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=200,y=200)
Button(root,text="-", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=300,y=200)


Button(root,text="4", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=10,y=300)
Button(root,text="5", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=100,y=300)
Button(root,text="6", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=200,y=300)
Button(root,text="+", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=300,y=300)

Button(root,text="1", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=10,y=400)
Button(root,text="2", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=100,y=400)
Button(root,text="3", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=200,y=400)
Button(root,text="0", width=4, height=1, font=("arial",15,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=300,y=400)





#Running the application
root.mainloop()