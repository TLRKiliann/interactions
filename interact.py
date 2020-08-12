#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


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
        # Insertion of text
        self.can.create_text(280, 100, anchor=CENTER, 
            text="Text below to read interactions", font=('Times New Roman', 18, 'bold'), fill='navy')
        self.can.create_text(980, 540, anchor=NE, text="ko@l@tr33",
            font=('Times', 12), fill='navy')
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)

        self.top = Frame(self.can, bg='aquamarine')
        self.bottom = Frame(self.can)
        self.top.pack(side=TOP, pady=2)
        self.bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

        def searchExpress():
            """
            Algorithm to compare
            """
            drug1 = self.compDrug1_var.get()
            drug2 = self.comparedrug2_var.get()

            maelist = ["bromides", "carbamazépine", "dépakine", "ethosuximide", 
            "mysoline", "phénobarbital", "phénytoïne", "briviact", "fycompa", "gabitril",
            "inovelon", "keppra", "lamictal", "lyrica", "neurontin", "sabril", "taloxa",
            "tiapridal", "topamax", "trileptal", "trobalt", "vimpat", "zonegran"]
            for i in maelist:
            	if i == drug2 or i ==drug1:
            		print("Le médic y est !!!")
"""

            if (drug1 == str("seroquel")) or (drug1 == str("sequase")) \
                or (drug1 == str("quetiapine")) and (drug2 == str("carbamazépine")) \
                or (drug2 == str("tégrétol")):
                print("+ Interactions ultraviolente !!!")
                importationViolente()
            elif (drug2 == str("seroquel")) or (drug2 == str("sequase")) \
                or (drug2 == str("quetiapine")) and (drug1 == str("carbamazépine")) \
                or (drug1 == str("tégrétol")):
                print("+ Interactions ultraviolente !!!")
                importationViolente()
            elif 

            else:
                print("+ Il n'y a pas d'interaction(s) !!!")
"""
        # Display text in textbox from medifiles files
        def importationViolente():
            try:
                if os.path.getsize('./medifiles/seroquel/Carbamazepine.txt'):
                    print("+ File 'Carbamazepine.txt' exist (read)!")
                    with open('./medifiles/seroquel/Carbamazepine.txt', 'r') as textfile2:
                        lines = textfile2.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote2:
                print("+ Sorry, file 'Carbamazepine.txt' does not exist !", outnote2)

        # Display text in textbox from medifiles files
        def importationNeuro():
            try:
                if os.path.getsize('./medifile/neuro_syndrom.txt'):
                    print("+ File 'neuro_syndrom.txt' exist (read)!")
                    with open('./medifile/neuro_syndrom.txt', 'r') as textfile1:
                        lines = textfile1.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'neuro_syndrom.txt' does not exist !", outnote)


        # Text entry 1
        self.compDrug1_var = StringVar()
        self.reachDate = Entry(self.can, textvariable=self.compDrug1_var, width=40)
        self.compDrug1_var.set("Enter a drug here")
        self.reachDate.pack(in_=self.top, side=LEFT, padx=10, pady=20)

        # Text entry 2
        self.comparedrug2_var = StringVar()
        self.reachDate = Entry(self.can, textvariable=self.comparedrug2_var, width=40)
        self.comparedrug2_var.set("Enter a second drug here")
        self.reachDate.pack(in_=self.top, side=LEFT, padx=10, pady=20)

        # Button to search text entry
        self.buttonSearch = Button(self.can, text='Search', width=8, bd=3,
            fg='navy', bg='cyan', highlightbackground='darkblue',
            activebackground='light blue', command=searchExpress)
        self.buttonSearch.pack(in_=self.top, side=LEFT, padx=10, pady=20)

        def upDateAll():
            self.master.destroy()
            subprocess.call('./neuro_psy.py')

        # Button to update
        self.buttonSearch = Button(self.can, text='Refresh', width=8, bd=3,
            fg='navy', bg='cyan', highlightbackground='darkblue',
            activeforeground='yellow',
            activebackground='light blue', command=upDateAll)
        self.buttonSearch.pack(in_=self.top, side=LEFT, padx=10, pady=20)

        # Button to quit
        self.buttonSearch = Button(self.can, text='Quit', width=8, bd=3,
            fg='white', bg='DodgerBlue2', highlightbackground='darkblue',
            activeforeground='red',
            activebackground='light blue', command=quit)
        self.buttonSearch.pack(in_=self.top, side=LEFT, padx=10, pady=20)

        # TextBox
        self.textBox=Text(self.can, height=20, width=80, font=18, relief=SUNKEN)
        self.textBox.pack(padx=100, pady=50)

        self.pack()

if __name__=='__main__':
    app = Application()
    app.mainloop()
