#import module from tkinter for UI
from tkinter import *

import os

#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("600x600")
def function():
    os.startfile(os.getcwd() + "/developers/diet1frame1first.html")

def function1():
    
    os.system("Project-synopsis.pdf")

def function4():

    root.destroy()
    os.system("py firstpage.py")




#stting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")



#creating a text label
Label(root, text="Project Reports",font=("times new roman",40),fg="white",bg="green", height=2).grid(row=0,rowspan=2,columnspan=8,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Developers",font=('times new roman',30),bg="#0D47A1",fg="white",command=function).grid(row=3,columnspan=8,sticky=N+E+W+S,padx=5,pady=5)
#creating a button
Button(root,text="Synopsis",font=("times new roman",30),bg="#0D47A1",fg='white',command=function1).grid(row=4,columnspan=8,sticky=W+E+N+S,padx=5,pady=5)

#creating third button
# Button(root,text="Report 2",font=('times new roman',30),bg="#3F51B5",fg="white",command=function3).grid(row=6,columnspan=8,sticky=N+E+W+S,padx=5,pady=5)

#creating five button
Button(root,text="Back",font=('times new roman',40),bg="red",fg="white",command=function4).grid(row=8,columnspan=8,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
