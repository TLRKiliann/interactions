#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from loopfile import *
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

            luckyLoop(self, drug1)
            luckyLoop2(self, drug2)
            luckyLoop3(self, drug3, drug4)

        # Display text in textbox from medifiles files (seroquel + carabamazepine)
        def importationViolente():
            try:
                if os.path.getsize('./medifiles/interdrug/carba_sero.txt'):
                    print("+ File 'carba_sero.txt' exist (read)!")
                    with open('./medifiles/interdrug/carba_sero.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'carba_sero.txt' does not exist !", outnote)

        # Display text in textbox from medifiles files (seroquel + depakine)
        def importationSeroDepak():
            try:
                if os.path.getsize('./medifiles/interdrug/sero_depak.txt'):
                    print("+ File 'sero_depak.txt' exist (read)!")
                    with open('./medifiles/interdrug/sero_depak.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'sero_depak.txt' does not exist !", outnote)

        # Display text in textbox from medifiles files (seroquel + érythromicine)
        def importationSeroEry():
            try:
                if os.path.getsize('./medifiles/interdrug/sero_erythro.txt'):
                    print("+ File 'sero_erythro.txt' exist (read)!")
                    with open('./medifiles/interdrug/sero_erythro.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'sero_erythro.txt' does not exist !", outnote)

        # Display text in textbox from medifiles files (seroquel + kétoconazol)
        def importationSeroKeto():
            try:
                if os.path.getsize('./medifiles/interdrug/sero_keto.txt'):
                    print("+ File 'sero_keto.txt' exist (read)!")
                    with open('./medifiles/interdrug/sero_keto.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'sero_keto.txt' does not exist !", outnote)

        # Display text in textbox from medifiles files (seroquel + lithium)
        def importationSeroLith():
            try:
                if os.path.getsize('./medifiles/interdrug/sero_lith.txt'):
                    print("+ File 'sero_lith.txt' exist (read)!")
                    with open('./medifiles/interdrug/sero_lith.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'sero_lith.txt' does not exist !", outnote)

        # Display text in textbox from medifiles files (seroquel + MeOH)
        def importationSeroMeoh():
            try:
                if os.path.getsize('./medifiles/interdrug/sero_metha.txt'):
                    print("+ File 'sero_metha.txt' exist (read)!")
                    with open('./medifiles/interdrug/sero_metha.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'sero_metha.txt' does not exist !", outnote)

        # Display text in textbox from medifiles files (seroquel + kétoconazol)
        def importationSeroPheny():
            try:
                if os.path.getsize('./medifiles/interdrug/sero_pheny.txt'):
                    print("+ File 'sero_pheny.txt' exist (read)!")
                    with open('./medifiles/interdrug/sero_pheny.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'sero_pheny.txt' does not exist !", outnote)
            
        # Display text in textbox from medifiles files (seroquel + kétoconazol)
        def importationCarbaAnticoa():
            try:
                if os.path.getsize('./medifiles/interdrug/carba_anticoa.txt'):
                    print("+ File 'carba_anticoa.txt' exist (read)!")
                    with open('./medifiles/interdrug/carba_anticoa.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'carba_anticoa.txt' does not exist !", outnote)

        def importationCarbaAntipsy():
            try:
                if os.path.getsize('./medifiles/interdrug/carba_neuro.txt'):
                    print("+ File 'carba_neuro.txt' exist (read)!")
                    with open('./medifiles/interdrug/carba_neuro.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'carba_neuro.txt' does not exist !", outnote)


        def importationLepoCarba():
            try:
                if os.path.getsize('./medifiles/interdrug/lepo_carba.txt'):
                    print("+ File 'lepo_carba.txt' exist (read)!")
                    with open('./medifiles/interdrug/lepo_carba.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'lepo_carba.txt' does not exist !", outnote)

        def importationLepoIpp():
            try:
                if os.path.getsize('./medifiles/interdrug/lepo_ipp.txt'):
                    print("+ File 'lepo_ipp.txt' exist (read)!")
                    with open('./medifiles/interdrug/lepo_ipp.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'lepo_ipp.txt' does not exist !", outnote)

        def importationLepoAtd():
            try:
                if os.path.getsize('./medifiles/interdrug/lepo_atd.txt'):
                    print("+ File 'lepo_atd.txt' exist (read)!")
                    with open('./medifiles/interdrug/lepo_atd.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'lepo_atd.txt' does not exist !", outnote)

        def importationLepoAtb():
            try:
                if os.path.getsize('./medifiles/interdrug/lepo_atb.txt'):
                    print("+ File 'lepo_atb.txt' exist (read)!")
                    with open('./medifiles/interdrug/lepo_atb.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'lepo_atb.txt' does not exist !", outnote)

        def importationLepoAntiHist():
            try:
                if os.path.getsize('./medifiles/interdrug/lepo_antihist.txt'):
                    print("+ File 'lepo_antihist.txt' exist (read)!")
                    with open('./medifiles/interdrug/lepo_antihist.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'lepo_antihist.txt' does not exist !", outnote)

        def importationLepoMae():
            try:
                if os.path.getsize('./medifiles/interdrug/lepo_mae.txt'):
                    print("+ File 'lepo_mae.txt' exist (read)!")
                    with open('./medifiles/interdrug/lepo_mae.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'lepo_mae.txt' does not exist !", outnote)

        def importationLepoNeuro():
            try:
                if os.path.getsize('./medifiles/interdrug/lepo_neuro.txt'):
                    print("+ File 'lepo_neuro.txt' exist (read)!")
                    with open('./medifiles/interdrug/lepo_neuro.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'lepo_neuro.txt' does not exist !", outnote)

        def importationLepoBzd():
            try:
                if os.path.getsize('./medifiles/interdrug/lepo_bzd.txt'):
                    print("+ File 'lepo_bzd.txt' exist (read)!")
                    with open('./medifiles/interdrug/lepo_bzd.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'lepo_bzd.txt' does not exist !", outnote)

        def importationLepoOh():
            try:
                if os.path.getsize('./medifiles/interdrug/lepo_oh.txt'):
                    print("+ File 'lepo_oh.txt' exist (read)!")
                    with open('./medifiles/interdrug/lepo_oh.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'lepo_oh.txt' does not exist !", outnote)

        def importationLepoMeOH():
            try:
                if os.path.getsize('./medifiles/interdrug/lepo_meoh.txt'):
                    print("+ File 'lepo_meoh.txt' exist (read)!")
                    with open('./medifiles/interdrug/lepo_meoh.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'lepo_meoh.txt' does not exist !", outnote)

        def importationLepoLith():
            try:
                if os.path.getsize('./medifiles/interdrug/lepo_lith.txt'):
                    print("+ File 'lepo_lith.txt' exist (read)!")
                    with open('./medifiles/interdrug/lepo_lith.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'lepo_lith.txt' does not exist !", outnote)

        def importationLepoCoag():
            try:
                if os.path.getsize('./medifiles/interdrug/lepo_coagul.txt'):
                    print("+ File 'lepo_coagul.txt' exist (read)!")
                    with open('./medifiles/interdrug/lepo_coagul.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'lepo_coagul.txt' does not exist !", outnote)

        """
        # Display text in textbox from medifiles files
        def importationpsycho():
            try:
                if os.path.getsize('./medifile/neuro_syndrom.txt'):
                    print("+ File 'neuro_syndrom.txt' exist (read)!")
                    with open('./medifile/neuro_syndrom.txt', 'r') as textfile1:
                        lines = textfile1.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'neuro_syndrom.txt' does not exist !", outnote)
        """

        # Label title
        self.label=Label(self.can, text="Interact", font='Arial 22 bold', 
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
        self.labelbot=Label(self.can, text="VS", font='Arial 18 bold', 
            fg='white', bg='aquamarine')
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
            "Available drugs : \n"
            "aripiprazol, clopin, clozapine, leponex, clopixol, entumine, fluanxol, haldol, halopéridol, nozinan,\n"
            "tiapridal, abilify, dogmatil, invega, olanzapine, zyprexa, risperdal, risperdone,\n"
            "seroquel, sequase, quétiapine, solian, carbamazépine, tégrétol, dépakine, valproate,\n" 
            "ethosuximide, pétinimid, mysoline, inovelon, aphénylbarbite, phénytoïne, briviact,\n"
            "fycompa, gabitril, inovelon, keppra, lamictal, lyrica, neurontin, sabril, taloxa,\n" 
            "tiapridal, topamax, topiramate, trileptal, vimpat, zonegran, palipéridone")
        self.textBox.pack(padx=20, pady=20)

        self.pack()

if __name__=='__main__':
    app = Application()
    app.mainloop()
