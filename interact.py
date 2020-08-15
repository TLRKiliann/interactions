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

            familiyttt=["antipsychotiques", "antiépileptiques", "antidépresseurs", 
            "anxiolytiques", "thymorégulateurs", "somnifères", "benzodiazépines", 
            "inhibiteurs de la cholinestérase", "antiparkinsoniens"]

            for i in familiyttt:
                if i == "antipsychotiques":
                    if drug1 == i:
                        familyPsycho()
                elif i == "antiépileptiques":
                    if drug1 == i:
                        familyMae()
                elif i == "antidépresseurs":
                    if drug1 == i:
                        familyAtd()
                elif i == "anxiolytiques":
                    if drug1 == i:
                        familyAnxio()
                elif i == "thymorégulateurs":
                    if drug1 == i:
                        familyThymo()
                elif i == "somnifères":
                    if drug1 == i:
                        familySomni()
                elif i == "benzodiazépines":
                    if drug1 == i:
                        familyBzd()
                elif i == "inhibiteurs de la cholinestérase":
                    if drug1 == i:
                        familyIcho()
                elif i == "antiparkinsoniens":
                    if drug1 == i:
                        familyPark()
                else:
                    print("+ Choose a ttt")

            oneDrug=["chlorpromazine", "clopin", "leponex", "clopixol", 
            "enthumine", "fluanxol", "haldol", "nozinan", "tiapridal", 
            "abilify", "dogmatil", "invega", "olanzapine", "zyprexa", 
            "orap", "risperdal", "risperdone", "semap", "seroquel", 
            "sequase", "quétiapine", "solian", "bromides", "carbamazépines", 
            "dépakine", "ethosuximide", "mysoline", "phénobarbital", 
            "phénytoïne", "briviact", "fycompa", "gabitril", "inovelon", 
            "keppra", "lamictal", "lyrica", "neurontin", "sabril", 
            "taloxa", "tiapridal", "topamax", "trileptal", "trobalt", 
            "vimpat", "zonegran"]

            for i in oneDrug:
                if i == "chlorpromazine":
                    if drug2 == i:
                        oneDrug()
                elif i == "clopin" or i == "leponex":
                    if drug2 == i:
                        oneDrug()
                elif i == "clopixol":
                    if drug2 == i:
                        oneDrug()
                elif i == "enthumine":
                    if drug2 == i:
                        oneDrug()
                elif i == "fluanxol":
                    if drug2 == i:
                        oneDrug()
                elif i == "haldol":
                    if drug2 == i:
                        oneDrug()
                elif i == "nozinan":
                    if drug2 == i:
                        oneDrug()
                elif i == "tiapridal":
                    if drug2 == i:
                        oneDrug()
                elif i == "abilify":
                    if drug2 == i:
                        oneDrug()
                elif i == "dogmatil":
                    if drug2 == i:
                        oneDrug()
                elif i == "invega":
                    if drug2 == i:
                        oneDrug()
                elif i == "olanzapine" or i == "zyprexa":
                    if drug2 == i:
                        oneDrug()
                elif i == "orap":
                    if drug2 == i:
                        oneDrug()
                elif i == "risperdal" or i == "risperdone":
                    if drug2 == i:
                        oneDrug()
                elif i == "semap":
                    if drug2 == i:
                        oneDrug()
                elif i == "sequase" or i == "seroquel" or i == "quétiapine":
                    if drug2 == i:
                        oneDrug()
                elif i == "solian":
                    if drug2 == i:
                        oneDrug()
                elif i == "bromides":
                    if drug2 == i:
                        oneDrug()
                elif i == "carbamazépine" or i == "tégrétol":
                    if drug2 == i:
                        oneDrug()
                elif i == "dépakine" or i == "valproate":
                    if drug2 == i:
                        oneDrug()
                elif i == "ethosuximide":
                    if drug2 == i:
                        oneDrug()
                elif i == "mysoline":
                    if drug2 == i:
                        oneDrug()
                elif i == "phénobarbital":
                    if drug2 == i:
                        oneDrug()
                elif i == "phénytoïne":
                    if drug2 == i:
                        oneDrug()
                elif i == "briviact":
                    if drug2 == i:
                        oneDrug()
                elif i == "fycompa":
                    if drug2 == i:
                        oneDrug()
                elif i == "gabitril":
                    if drug2 == i:
                        oneDrug()
                elif i == "inovelon":
                    if drug2 == i:
                        oneDrug()
                elif i == "keppra":
                    if drug2 == i:
                        oneDrug()
                elif i == "lamictal":
                    if drug2 == i:
                        oneDrug()
                elif i == "lyrica":
                    if drug2 == i:
                        oneDrug()
                elif i == "neurontin":
                    if drug2 == i:
                        oneDrug()
                elif i == "sabril":
                    if drug2 == i:
                        oneDrug()
                elif i == "taloxa":
                    if drug2 == i:
                        oneDrug()
                elif i == "topamax":
                    if drug2 == i:
                        oneDrug()
                elif i == "trileptal":
                    if drug2 == i:
                        oneDrug()
                elif i == "trobalt":
                    if drug2 == i:
                        oneDrug()
                elif i == "vimpat":
                    if drug2 == i:
                        oneDrug()
                elif i == "zonegran":
                    if drug2 == i:
                        oneDrug()
                elif i == "anafranil":
                    if drug2 == i:
                        oneDrug()
                else:
                    print("+ Choose a ttt")

            neurolist=["chlorpromazine", "clopin", "leponex", "clopixol", 
            "enthumine", "fluanxol", "haldol", "nozinan", "tiapridal", 
            "abilify", "dogmatil", "invega", "olanzapine", "zyprexa", 
            "orap", "risperdal", "risperdone", "semap", "seroquel", 
            "sequase", "quétiapine", "solian"]

            for i in neurolist:
                if i == "seroquel":
                    if (drug1 == i or drug2 == i) and (drug1 == "carbamazépine" or \
                        drug2 == "carbamazépine"):
                        print("+ Interactions ultraviolente !!!")
                        importationViolente()
                    """
                    elif () and ():
                    elif () and ():
                    elif () and ():
                    elif () and ():
                    elif () and ():

                    else:
                        print("+ Nothing !")
                    """

        def familyPsycho():
            try:
                if os.path.getsize('./medifiles/family/antipsycho.txt'):
                    print("+ File 'antipsycho.txt' exist (read)!")
                    with open('./medifiles/family/antipsycho.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'antipsycho.txt' does not exist !", outnote)


        def familyMae():
            try:
                if os.path.getsize('./medifiles/family/mae.txt'):
                    print("+ File 'mae.txt' exist (read)!")
                    with open('./medifiles/family/mae.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'mae.txt' does not exist !", outnote)

        def familyAtd():
            try:
                if os.path.getsize('./medifiles/family/atd.txt'):
                    print("+ File 'atd.txt' exist (read)!")
                    with open('./medifiles/family/atd.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'atd.txt' does not exist !", outnote)

        def familyAnxio():
            try:
                if os.path.getsize('./medifiles/family/anxio.txt'):
                    print("+ File 'anxio.txt' exist (read)!")
                    with open('./medifiles/family/anxio.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'anxio.txt' does not exist !", outnote)

        def familyThymo():
            try:
                if os.path.getsize('./medifiles/family/thymo.txt'):
                    print("+ File 'thymo.txt' exist (read)!")
                    with open('./medifiles/family/thymo.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'thymo.txt' does not exist !", outnote)

        def familySomni():
            try:
                if os.path.getsize('./medifiles/family/somni.txt'):
                    print("+ File 'somni.txt' exist (read)!")
                    with open('./medifiles/family/somni.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'somni.txt' does not exist !", outnote)

        def familyBzd():
            try:
                if os.path.getsize('./medifiles/family/bzd.txt'):
                    print("+ File 'bzd.txt' exist (read)!")
                    with open('./medifiles/family/bzd.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'bzd.txt' does not exist !", outnote)


        def familyIcho():
            try:
                if os.path.getsize('./medifiles/family/icho.txt'):
                    print("+ File 'icho.txt' exist (read)!")
                    with open('./medifiles/family/icho.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'icho.txt' does not exist !", outnote)


        def familyPark():
            try:
                if os.path.getsize('./medifiles/family/park.txt'):
                    print("+ File 'park.txt' exist (read)!")
                    with open('./medifiles/family/park.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'park.txt' does not exist !", outnote)



        # Display text in textbox from medifiles files (seroquel + carabamazepine)
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

        # Label
        self.label=Label(self.can, text="Interact", font='Arial 18 bold', 
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

        self.labelbot=Label(self.can, text="VS", font='Arial 18 bold', 
            fg='white', bg='aquamarine')
        self.labelbot.pack(in_=self.top3, side=LEFT, padx=5, pady=0)

        # Text entry 4
        self.comparedrug2_var = StringVar()
        self.reachDate = Entry(self.can, textvariable=self.comparedrug2_var, width=30)
        self.comparedrug2_var.set("Enter drug 2")
        self.reachDate.pack(in_=self.top3, side=LEFT, padx=80, pady=10)

        # Button to search text entry
        self.buttonSearch = Button(self.can, text='Search', width=8, bd=3,
            fg='navy', bg='cyan', highlightbackground='darkblue',
            activebackground='light blue', command=searchExpress)
        self.buttonSearch.pack(in_=self.top4, side=LEFT, padx=10, pady=5)

        def upDateAll():
            self.master.destroy()
            subprocess.call('./neuro_psy.py')

        # Button to update
        self.buttonSearch = Button(self.can, text='Refresh', width=8, bd=3,
            fg='navy', bg='cyan', highlightbackground='darkblue',
            activeforeground='yellow',
            activebackground='light blue', command=upDateAll)
        self.buttonSearch.pack(in_=self.top4, side=LEFT, padx=10, pady=5)

        # Button to quit
        self.buttonSearch = Button(self.can, text='Quit', width=8, bd=3,
            fg='white', bg='DodgerBlue2', highlightbackground='darkblue',
            activeforeground='red',
            activebackground='light blue', command=quit)
        self.buttonSearch.pack(in_=self.top4, side=LEFT, padx=10, pady=5)

        # TextBox
        self.textBox=Text(self.can, height=20, width=80, font=18, relief=SUNKEN)
        self.textBox.pack(padx=20, pady=20)

        self.pack()

if __name__=='__main__':
    app = Application()
    app.mainloop()
