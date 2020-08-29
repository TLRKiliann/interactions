#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.familyloop import *
from medifiles.apsydrug import *
from medifiles.aepidrug import *
from medifiles.anxidrug import *
from medifiles.atddrug import *
from medifiles.stabdrug import *

from medifiles.aripiloop import *
from medifiles.carbaloop import *
from medifiles.depaloop import *
from medifiles.lepoloop import *
from medifiles.seroloop import *


class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='DodgerBlue4', padx=20, pady=20, relief=GROOVE)
        self.master.title('Interact - Developed by ko@l@tr33 - 2020')

        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = Canvas(self, width=1250, height=800, bg='aquamarine')
        self.frame = Frame(self.can)

        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW, tags="self.frame")
        # Insertion of picture
        self.photo = PhotoImage(file='./picgif/bg.png')
        self.item = self.can.create_image(625, 400, image=self.photo)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)

        self.top = Frame(self.can, bg='turquoise3')
        self.top2 = Frame(self.can, bg='turquoise3')
        self.top3 = Frame(self.can, bg='aquamarine')
        self.top4 = Frame(self.can, bg='turquoise3')
        self.bottom = Frame(self.can)
        self.top.pack(side=TOP, pady=2)
        self.top2.pack(side=TOP, pady=2)
        self.top3.pack(side=TOP, pady=2)
        self.top4.pack(side=TOP, pady=2)
        self.bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

        def searchExpress():
            """
            Algorithm to compare
            """
            drug1 = self.familyDrug1_var.get()
            drug2 = self.oneperdrug2_var.get()

            drug3 = self.compDrug1_var.get()
            drug4 = self.comparedrug2_var.get()

            familyLoop(self, drug1)

            antipsyDrugLoop(self, drug2)
            antiepiDrugLoop(self, drug2)
            anxioDrugLoop(self, drug2)
            atdDrugLoop(self, drug2)
            stabDrugLoop(self, drug2)

            seroFunc(self, drug3, drug4)
            carbaFunc(self, drug3, drug4)
            lepoFunc(self, drug3, drug4)
            depaFunc(self, drug3, drug4)
            ariFunc(self, drug3, drug4)

        # Label title
        self.label=Label(self.can, text="Interact", font='Times 22 bold', 
            fg='navy', bg='turquoise3')
        self.label.pack(in_=self.top, side=LEFT, padx=5, pady=10)

        # Text entry 1
        self.familyDrug1_var = StringVar()
        self.reachFamily = Entry(self.can, textvariable=self.familyDrug1_var, width=30)
        self.familyDrug1_var.set("Enter a class of drug")
        self.reachFamily.pack(in_=self.top2, side=LEFT, padx=40, pady=20)

        # Text entry 2
        self.oneperdrug2_var = StringVar()
        self.reachDate = Entry(self.can, textvariable=self.oneperdrug2_var, width=30)
        self.oneperdrug2_var.set("Enter a name of drug")
        self.reachDate.pack(in_=self.top2, side=LEFT, padx=40, pady=20)

        # Text entry 3
        self.compDrug1_var = StringVar()
        self.reachDate = Entry(self.can, textvariable=self.compDrug1_var, width=30)
        self.compDrug1_var.set("Enter a drug 1")
        self.reachDate.pack(in_=self.top3, side=LEFT, padx=20, pady=10)

        # Label VS
        self.labelbot=Label(self.can, text="VS", font='Times 18 bold', 
            fg='red', bg='aquamarine')
        self.labelbot.pack(in_=self.top3, side=LEFT, pady=10)

        # Text entry 4
        self.comparedrug2_var = StringVar()
        self.reachDate = Entry(self.can, textvariable=self.comparedrug2_var, width=30)
        self.comparedrug2_var.set("Enter drug 2")
        self.reachDate.pack(in_=self.top3, side=LEFT, padx=20, pady=10)

        # Button to search text entry
        self.buttonSearch = Button(self.can, text='Search', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=searchExpress)
        self.buttonSearch.pack(in_=self.top4, side=LEFT, padx=10, pady=10)

        def renewTextBox():
            """
            To renew textBox with intro page !
            """
            try:
                if os.path.getsize('textualbox.txt'):
                    print("+ File 'textualbox.txt' exist (read)!")
                    self.textBox.delete('0.0', 'end')
                    self.textBox.update()
                    with open('textualbox.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'textualbox.txt' does not exist !", outnote)

        def showListtt():
            """
            To display list of ttt to use app !
            """
            try:
                if os.path.getsize('listbox.txt'):
                    print("+ File 'listbox.txt' exist (read)!")
                    self.textBox.delete('0.0', 'end')
                    self.textBox.update()
                    with open('listbox.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'listbox.txt' does not exist !", outnote)

        def upDateAll():
            """
            To update all !
            """
            self.master.destroy()
            subprocess.call('./interact.py')

        # Button to display list of ttt
        self.buttonListtt = Button(self.can, text='Liste ttt', width=8, bd=3,
            fg='navy', bg='turquoise2', highlightbackground='darkblue',
            activeforeground='yellow',
            activebackground='light blue', command=showListtt)
        self.buttonListtt.pack(in_=self.top4, side=LEFT, padx=10, pady=10)

        # Button to earase textBox
        self.buttonRefresh = Button(self.can, text='Intro', width=8, bd=3,
            fg='navy', bg='turquoise2', highlightbackground='darkblue',
            activeforeground='yellow',
            activebackground='light blue', command=renewTextBox)
        self.buttonRefresh.pack(in_=self.top4, side=LEFT, padx=10, pady=10)

        # Button to update
        self.buttonUpdate = Button(self.can, text='Refresh', width=8, bd=3,
            fg='navy', bg='turquoise2', highlightbackground='darkblue',
            activeforeground='yellow',
            activebackground='light blue', command=upDateAll)
        self.buttonUpdate.pack(in_=self.top4, side=LEFT, padx=10, pady=10)

        # Button to quit
        self.buttonQuit = Button(self.can, text='Quit', width=8, bd=3,
            fg='white', bg='DodgerBlue2', highlightbackground='darkblue',
            activeforeground='red',
            activebackground='light blue', command=quit)
        self.buttonQuit.pack(in_=self.top4, side=LEFT, padx=10, pady=10)

        # TextBox
        self.textBox=Text(self.can, height=20, width=80, font=18, relief=SUNKEN)
        try:
            if os.path.getsize('textualbox.txt'):
                print("+ File 'textualbox.txt' exist (read)!")
                self.textBox.delete('0.0', 'end')
                self.textBox.update()
                with open('textualbox.txt', 'r') as textfile:
                    lines = textfile.readlines()
                    for li in lines:
                        self.textBox.insert(END, li)
        except FileNotFoundError as outnote:
            print("+ Sorry, file 'textualbox.txt' does not exist !", outnote)
            
        self.textBox.pack(padx=20, pady=20)
        self.pack()

if __name__=='__main__':
    app = Application()
    app.mainloop()
