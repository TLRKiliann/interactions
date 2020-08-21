#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from loopfile import *
from seroloop import *
from carbaloop import *
from lepoloop import *
from depaloop import *
#import os
#import subprocess


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
            oneDrugLoop(self, drug2)
            seroLoop(self, drug3, drug4)
            carbaLoop(self, drug3, drug4)
            lepoLoop(self, drug3, drug4)
            depaLoop(self, drug3, drug4)

        # Label title
        self.label=Label(self.can, text="Interact", font='Times 22 bold', 
            fg='navy', bg='turquoise3')
        self.label.pack(in_=self.top, side=LEFT, padx=5, pady=10)

        # Text entry 1
        self.familyDrug1_var = StringVar()
        self.reachFamily = Entry(self.can, textvariable=self.familyDrug1_var, width=30)
        self.familyDrug1_var.set("Enter a class of drug")
        self.reachFamily.pack(in_=self.top2, side=LEFT, padx=10, pady=20)

        # Text entry 2
        self.oneperdrug2_var = StringVar()
        self.reachDate = Entry(self.can, textvariable=self.oneperdrug2_var, width=30)
        self.oneperdrug2_var.set("Enter a name of drug")
        self.reachDate.pack(in_=self.top2, side=LEFT, padx=10, pady=20)

        # Text entry 3
        self.compDrug1_var = StringVar()
        self.reachDate = Entry(self.can, textvariable=self.compDrug1_var, width=30)
        self.compDrug1_var.set("Enter a drug 1")
        self.reachDate.pack(in_=self.top3, side=LEFT, padx=80, pady=10)

        # Label VS
        self.labelbot=Label(self.can, text="VS", font='Times 18 bold', 
            fg='navy', bg='aquamarine')
        self.labelbot.pack(in_=self.top3, side=LEFT, padx=5, pady=10)

        # Text entry 4
        self.comparedrug2_var = StringVar()
        self.reachDate = Entry(self.can, textvariable=self.comparedrug2_var, width=30)
        self.comparedrug2_var.set("Enter drug 2")
        self.reachDate.pack(in_=self.top3, side=LEFT, padx=80, pady=10)

        # Button to search text entry
        self.buttonSearch = Button(self.can, text='Search', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=searchExpress)
        self.buttonSearch.pack(in_=self.top4, side=LEFT, padx=10, pady=10)

        def refresh():
            """
            To refresh textBox !
            """
            self.textBox.delete('0.0', END)
            self.textBox.update()

        def upDateAll():
            """
            To update all !
            """
            self.master.destroy()
            subprocess.call('./interact.py')

        # Button to earase textBox
        self.buttonRefresh = Button(self.can, text='Erase', width=8, bd=3,
            fg='navy', bg='turquoise2', highlightbackground='darkblue',
            activeforeground='yellow',
            activebackground='light blue', command=refresh)
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
        self.textBox.insert(INSERT, "You can choose from the following families or medications :\n\n"
            "Available class of drugs : \n"
            "antipsychotiques, antiépileptiques, antidépresseurs, anxiolytiques, thymorégulateurs,\n" 
            "somnifères, benzodiazépines, inhibiteurs de la cholinestérase, antiparkinsoniens\n\n"
            "Available drugs : \n\n"
            "Antipsychotiques : \n"
            "------------------------\n\n"
            "abilify, aripiprazol\n"
            "clopin = clozapine = leponex\n"
            "clopixol = zuclopenthixol\n"
            "dépakine = valproate\n"
            "dogmatil = sulpride\n"
            "entumine = clotiapine\n"
            "fluanxol = flupentixol\n"
            "haldol = halopéridol\n"
            "invega = palipéridone\n"
            "nozinan = levomepromazine\n"
            "olanzapine = zyprexa\n"
            "risperdal = risperdone\n"
            "seroquel = sequase = quétiapine\n"
            "solian = amisulpride\n"
            "tiapridal = tiapride\n\n"

            "Antiépileptiques :\n"
            "-----------------------\n\n"
            "briviact = brivaracétam =\n"
            "carbamazépine = tégrétol\n"
            "ethosuximide = pétinimid\n"
            "fycompa = pérampanel\n"
            "gabitril\n"
            "inovelon = rufinamide\n"
            "keppra = levetiracetam\n"
            "lamictal = lamotrigine\n"
            "lyrica = prégabaline\n"
            "mysoline = primidone\n"
            "neurontin = gabapentine\n"
            "phénobarbital = aphénylbarbite\n"
            "phénytoïne\n"
            "sabril = vigabatrin\n"
            "taloxa = felbamate\n"
            "topamax = topiramate\n"
            "trileptal = oxcarbazépine\n" 
            "vimpat = lacosamide\n"
            "zonegran = zonisamide\n\n")
        self.textBox.pack(padx=20, pady=20)

        self.pack()

if __name__=='__main__':
    app = Application()
    app.mainloop()
