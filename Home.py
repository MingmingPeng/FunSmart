from tkinter import*
import os
import Methods
import PreTest
from tkmacosx import Button

def main(root, frame):
    frame.destroy()
    root.title("FunSmart Home Screen")
    frame = Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    subjects = Methods.fileSplitter("subjectSelector.txt")
    
    btn = Button(frame,font=("Arial", 14, "italic"),foreground = 'white', text = subjects[0], padx = 100, pady=50, bg='#28C275', command = lambda: PreTest.main(root, frame, subjects[0]))
    btn.pack()

    btn1 = Button(frame,font=("Arial", 14, "italic"),foreground = 'white', text = subjects[1], padx = 100, pady=50, bg="#28C275", command = lambda: PreTest.main(root, frame, subjects[1]))
    btn1.pack()

    btn2 = Button(frame,font=("Arial", 14, "italic"),foreground = 'white', text = subjects[2], padx = 100, pady=50, bg="#28C275", command = lambda: PreTest.main(root, frame, subjects[2]))
    btn2.pack()

    # btn3 = Button(frame, text = subjects[3], padx = 100, pady=50, height=20, bg="lightgreen", command = lambda: PreTest.main(root, frame, subjects[3]))
    btn3 = Button(frame,font=("Arial", 14, "italic"),foreground = 'white', text = subjects[3], padx = 100, pady=50, bg="#28C275", command = lambda: PreTest.main(root, frame, subjects[3]))
    btn3.pack()

