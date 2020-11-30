from tkinter import*
import os
import Methods
import PreTest
from tkmacosx import Button

def main(root, frame):
    frame.destroy()
    root.title("FunSmart Home Screen")
    frame = Frame(root,)
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    photo3 = PhotoImage(file = "funsmart.png")
    w = Label(frame, image=photo3)
    w.pack()




    subjects = Methods.fileSplitter("subjectSelector.txt")

    
    btn = Button(frame,font=("Arial", 14, "italic"),foreground = 'white',  text = subjects[0], height=80,padx = 100, pady=50, bg='#82E0AA', command = lambda: PreTest.main(root, frame, subjects[0]))
    # btn = Button(frame,font=("Arial", 14, "italic"),foreground = 'white',  text = subjects[0], height=60,pady=20, bg='#28C275', command = lambda: PreTest.main(root, frame, subjects[0]))
    btn.pack()

    btn1 = Button(frame,font=("Arial", 14, "italic"),foreground = 'white', text = subjects[1], height=80,padx = 100, pady=50, bg="#82E0AA", command = lambda: PreTest.main(root, frame, subjects[1]))
    btn1.pack()

    btn2 = Button(frame,font=("Arial", 14, "italic"),foreground = 'white', text = subjects[2], height=80,padx = 100, pady=50, bg="#82E0AA", command = lambda: PreTest.main(root, frame, subjects[2]))
    btn2.pack()

    # btn3 = Button(frame, text = subjects[3], padx = 100, pady=50, height=20, bg="lightgreen", command = lambda: PreTest.main(root, frame, subjects[3]))
    btn3 = Button(frame,font=("Arial", 14, "italic"),foreground = 'white',text = subjects[3], height=80, padx = 100, pady=50, bg="#82E0AA", command = lambda: PreTest.main(root, frame, subjects[3]))
    btn3.pack()

