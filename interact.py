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
                    if drug1 == i or drug1 == "antipsy":
                        familyPsycho()
                elif i == "antiépileptiques":
                    if drug1 == i or drug1 == "mae":
                        familyMae()
                elif i == "antidépresseurs":
                    if drug1 == i or drug1 == "atd":
                        familyAtd()
                elif i == "anxiolytiques":
                    if drug1 == i or drug1 == "anxio":
                        familyAnxio()
                elif i == "thymorégulateurs":
                    if drug1 == i or drug1 == "stabilisateurs":
                        familyThymo()
                elif i == "somnifères":
                    if drug1 == i or drug1 == "somni" or drug1 == "inducteurs de sommeil":
                        familySomni()
                elif i == "benzodiazépines":
                    if drug1 == i or drug1 == "bzd":
                        familyBzd()
                elif i == "inhibiteurs de la cholinestérase":
                    if drug1 == i or drug1 == "idlc":
                        familyIcho()
                elif i == "antiparkinsoniens":
                    if drug1 == i or drug1 == "ap":
                        familyPark()
                else:
                    print("+ This drug is not in familylist")

            # Don't forget kemadrin akineton
            oneDrug=["chlorpromazine", "clopin", "leponex", "clopixol", 
            "enthumine", "fluanxol", "haldol", "nozinan", "tiapridal", 
            "abilify", "dogmatil", "invega", "olanzapine", "zyprexa", 
            "orap", "risperdal", "risperdone", "semap", "seroquel", "sequase", 
            "quétiapine", "solian", "bromides", "carbamazépine", "tégrétol", 
            "dépakine", "valproate", "ethosuximide", "mysoline", "phénobarbital", 
            "aphénylbarbite", "phénytoïne", "briviact", "fycompa", "gabitril", 
            "inovelon", "keppra", "lamictal", "lyrica", "neurontin", "sabril", 
            "taloxa", "tiapridal", "topamax", "topiramate", "trileptal", "trobalt", 
            "vimpat", "zonegran"]

            for i in oneDrug:
                if i == "chlorpromazine":
                    if drug2 == i:
                        oneDrug1()
                elif i == "clopin" or i == "leponex":
                    if drug2 == i:
                        oneDrug2()
                elif i == "clopixol":
                    if drug2 == i:
                        oneDrug3()
                elif i == "enthumine":
                    if drug2 == i:
                        oneDrug4()
                elif i == "fluanxol":
                    if drug2 == i:
                        oneDrug5()
                elif i == "haldol":
                    if drug2 == i:
                        oneDrug6()
                elif i == "nozinan":
                    if drug2 == i:
                        oneDrug7()
                elif i == "tiapridal":
                    if drug2 == i:
                        oneDrug8()
                elif i == "abilify":
                    if drug2 == i:
                        oneDrug9()
                elif i == "dogmatil":
                    if drug2 == i:
                        oneDrug10()
                elif i == "invega":
                    if drug2 == i:
                        oneDrug11()
                elif i == "olanzapine" or i == "zyprexa":
                    if drug2 == i:
                        oneDrug12()
                elif i == "orap":
                    if drug2 == i:
                        oneDrug13()
                elif i == "risperdal" or i == "risperdone":
                    if drug2 == i:
                        oneDrug14()
                elif i == "semap":
                    if drug2 == i:
                        oneDrug15()
                elif i == "sequase" or i == "seroquel" or i == "quétiapine":
                    if drug2 == i:
                        oneDrug16()
                elif i == "solian":
                    if drug2 == i:
                        oneDrug17()
                elif i == "bromides":
                    if drug2 == i:
                        oneDrug18()
                elif i == "carbamazépine" or i == "tégrétol":
                    if drug2 == i:
                        oneDrug19()
                elif i == "dépakine" or i == "valproate":
                    if drug2 == i:
                        oneDrug20()
                elif i == "ethosuximide":
                    if drug2 == i:
                        oneDrug21()
                elif i == "mysoline":
                    if drug2 == i:
                        oneDrug22()
                elif i == "phénobarbital" or i == "aphénylbarbite":
                    if drug2 == i:
                        oneDrug23()
                elif i == "phénytoïne":
                    if drug2 == i:
                        oneDrug24()
                elif i == "briviact":
                    if drug2 == i:
                        oneDrug25()
                elif i == "fycompa":
                    if drug2 == i:
                        oneDrug26()
                elif i == "gabitril":
                    if drug2 == i:
                        oneDrug27()
                elif i == "inovelon":
                    if drug2 == i:
                        oneDrug28()
                elif i == "keppra":
                    if drug2 == i:
                        oneDrug29()
                elif i == "lamictal":
                    if drug2 == i:
                        oneDrug30()
                elif i == "lyrica":
                    if drug2 == i:
                        oneDrug31()
                elif i == "neurontin":
                    if drug2 == i:
                        oneDrug32()
                elif i == "sabril":
                    if drug2 == i:
                        oneDrug33()
                elif i == "taloxa":
                    if drug2 == i:
                        oneDrug34()
                elif i == "topamax" or i == "topiramate":
                    if drug2 == i:
                        oneDrug35()
                elif i == "trileptal":
                    if drug2 == i:
                        oneDrug36()
                elif i == "trobalt":
                    if drug2 == i:
                        oneDrug37()
                elif i == "vimpat":
                    if drug2 == i:
                        oneDrug38()
                elif i == "zonegran":
                    if drug2 == i:
                        oneDrug39()
                elif i == "anafranil":
                    if drug2 == i:
                        oneDrug40()
                else:
                    print("+ This drug is not in the list")

            # drug1 VS drug2 (interact)        
            for i in oneDrug:
                if i == "seroquel" or i == "sequase" or i == "quétiapine":
                    if (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
                        drug4 == "carbamazépine"):
                        print("+ Interactions ultraviolente !!!")
                        importationViolente()
                
                if i == "seroquel" or i == "sequase" or i == "quétiapine":
                    if (drug3 == i or drug4 == i) and (drug3 == "dépakine" or \
                        drug4 == "dépakine"):
                        print("+ Interactions !!!")
                        importationSeroDepak()

                if i == "seroquel" or i == "sequase" or i == "quétiapine":
                    if (drug3 == i or drug4 == i) and (drug3 == "érythromycine" or \
                        drug4 == "érythromycine"):
                        print("+ Interactions !!!")
                        importationSeroEry()

                if i == "seroquel" or i == "sequase" or i == "quétiapine":
                    if (drug3 == i or drug4 == i) and (drug3 == "kétoconazol" or \
                        drug4 == "kétoconazol"):
                        print("+ Interactions !!!")
                        importationSeroKeto()

                if i == "seroquel" or i == "sequase" or i == "quétiapine":
                    if (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
                        drug4 == "lithium"):
                        print("+ Interactions !!!")
                        importationSeroLith()

                if i == "seroquel" or i == "sequase" or i == "quétiapine":
                    if (drug3 == i or drug4 == i) and (drug3 == "méthadone" or \
                        drug4 == "méthadone"):
                        print("+ Interactions !!!")
                        importationSeroMeoh()

                if i == "seroquel" or i == "sequase" or i == "quétiapine":
                    if (drug3 == i or drug4 == i) and (drug3 == "alcool" or \
                        drug4 == "alcool"):
                        print("+ Interactions !!!")
                        importationSeroOh()

                if i == "seroquel" or i == "sequase" or i == "quétiapine":
                    if (drug3 == i or drug4 == i) and (drug3 == "phénytoïne" or \
                        drug4 == "phénytoïne"):
                        print("+ Interactions !!!")
                        importationSeroPheny()

                if i == "seroquel" or i == "sequase" or i == "quétiapine":
                    if (drug3 == i or drug4 == i) and (drug3 == "risperdal" or \
                        drug4 == "risperdal"):
                        print("+ Interactions !!!")
                        importationSeroRisp()

                if i == "carbamazépine" or i == "tégrétol":
                    if (drug3 == i or drug4 == i) and (drug3 == "sintrom" or \
                        drug3 == "xarelto" or drug3 == "Rivaroxaban" or \
                        drug3 == "héparine" or drug3 == "pradaxa" or \
                        drug4 == "eliquis" or \
                        drug4 == "sintrom" or drug4 == "xarelto" or \
                        drug4 == "Rivaroxaban" or drug4 == "héparine" or \
                        drug4 == "pradaxa" or drug4 == "eliquis"):
                        print("+ Interactions !!!")
                        importationCarbaAnticoa()

                """
                elif i == "clopin" or i == "leponex":
                
                elif i == "dépakine" or i == "valproate":

                elif i == "olanzapine" or i == "zyprexa":

                elif i == "clopixol":

                elif i == "haldol":

                elif i == "risperdal" or i == "risperdone":

                elif i == "fluanxol":

                elif i == "nozinan":

                elif i == "solian":

                """

        def familyPsycho():
            """
            Per family !
            """
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

        # Per drug ...
        def oneDrug3():
            """
            Per drug clopixol
            """
            try:
                if os.path.getsize('./medifiles/perdrug/clopixol.txt'):
                    print("+ File 'clopixol.txt' exist (read)!")
                    with open('./medifiles/perdrug/clopixol.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'clopixol.txt' does not exist !", outnote)

        def oneDrug6():
            """
            Per drug haldol
            """
            try:
                if os.path.getsize('./medifiles/perdrug/haldol.txt'):
                    print("+ File 'haldol.txt' exist (read)!")
                    with open('./medifiles/perdrug/haldol.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'haldol.txt' does not exist !", outnote)

        def oneDrug9():
            """
            Per drug abilify
            """
            try:
                if os.path.getsize('./medifiles/perdrug/abilify.txt'):
                    print("+ File 'abilify.txt' exist (read)!")
                    with open('./medifiles/perdrug/abilify.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'abilify.txt' does not exist !", outnote)

        def oneDrug12():
            """
            Per drug olanzapine, zyprexa
            """
            try:
                if os.path.getsize('./medifiles/perdrug/olanzapine.txt'):
                    print("+ File 'olanzapine.txt' exist (read)!")
                    with open('./medifiles/perdrug/olanzapine.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'olanzapine.txt' does not exist !", outnote)

        def oneDrug16():
            """
            Per drug seroquel
            """
            try:
                if os.path.getsize('./medifiles/perdrug/seroquel.txt'):
                    print("+ File 'seroquel.txt' exist (read)!")
                    with open('./medifiles/perdrug/seroquel.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'seroquel.txt' does not exist !", outnote)

        def oneDrug17():
            """
            Per drug solian
            """
            try:
                if os.path.getsize('./medifiles/perdrug/solian.txt'):
                    print("+ File 'solian.txt' exist (read)!")
                    with open('./medifiles/perdrug/solian.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'solian.txt' does not exist !", outnote)

        def oneDrug19():
            """
            Per drug carbamazépine
            """
            try:
                if os.path.getsize('./medifiles/perdrug/carbamazepine.txt'):
                    print("+ File 'carbamazepine.txt' exist (read)!")
                    with open('./medifiles/perdrug/carbamazepine.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'carbamazepine.txt' does not exist !", outnote)

        def oneDrug20():
            """
            Per drug depakine et valproate
            """
            try:
                if os.path.getsize('./medifiles/perdrug/depakine.txt'):
                    print("+ File 'depakine.txt' exist (read)!")
                    with open('./medifiles/perdrug/depakine.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'depakine.txt' does not exist !", outnote)

        def oneDrug23():
            """
            Per drug phénobarbital and aphénylbarbite
            """
            try:
                if os.path.getsize('./medifiles/perdrug/phenobarbit.txt'):
                    print("+ File 'phenobarbit.txt' exist (read)!")
                    with open('./medifiles/perdrug/phenobarbit.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'phenobarbit.txt' does not exist !", outnote)

        def oneDrug32():
            """
            Per drug neurontin
            """
            try:
                if os.path.getsize('./medifiles/perdrug/neurontin.txt'):
                    print("+ File 'neurontin.txt' exist (read)!")
                    with open('./medifiles/perdrug/neurontin.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'neurontin.txt' does not exist !", outnote)

        def oneDrug35():
            """
            Per drug topamax and topiramate
            """
            try:
                if os.path.getsize('./medifiles/perdrug/topamax.txt'):
                    print("+ File 'topamax.txt' exist (read)!")
                    with open('./medifiles/perdrug/topamax.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'topamax.txt' does not exist !", outnote)


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
        self.textBox.pack(padx=20, pady=20)

        self.pack()

if __name__=='__main__':
    app = Application()
    app.mainloop()
