#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from loopfile import *
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

            luckyLoop(self, drug1)
            
            luckyLoop2(drug2, drug3, drug4)

        # Per drug ...
        def oneDrug2():
            """
            Per drug leponex
            """
            try:
                if os.path.getsize('./medifiles/perdrug/leponex.txt'):
                    print("+ File 'leponex.txt' exist (read)!")
                    with open('./medifiles/perdrug/leponex.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'leponex.txt' does not exist !", outnote)

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

        def oneDrug4():
            """
            Per drug entumine
            """
            try:
                if os.path.getsize('./medifiles/perdrug/entumine.txt'):
                    print("+ File 'entumine.txt' exist (read)!")
                    with open('./medifiles/perdrug/entumine.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'entumine.txt' does not exist !", outnote)

        def oneDrug5():
            """
            Per drug fluanxol
            """
            try:
                if os.path.getsize('./medifiles/perdrug/fluanxol.txt'):
                    print("+ File 'fluanxol.txt' exist (read)!")
                    with open('./medifiles/perdrug/fluanxol.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'fluanxol.txt' does not exist !", outnote)

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

        def oneDrug7():
            """
            Per drug nozinan
            """
            try:
                if os.path.getsize('./medifiles/perdrug/nozinan.txt'):
                    print("+ File 'nozinan.txt' exist (read)!")
                    with open('./medifiles/perdrug/nozinan.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'nozinan.txt' does not exist !", outnote)

        def oneDrug8():
            """
            Per drug tiapridal
            """
            try:
                if os.path.getsize('./medifiles/perdrug/tiapridal.txt'):
                    print("+ File 'tiapridal.txt' exist (read)!")
                    with open('./medifiles/perdrug/tiapridal.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'tiapridal.txt' does not exist !", outnote)

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

        def oneDrug10():
            """
            Per drug dogmatil
            """
            try:
                if os.path.getsize('./medifiles/perdrug/dogmatil.txt'):
                    print("+ File 'dogmatil.txt' exist (read)!")
                    with open('./medifiles/perdrug/dogmatil.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'dogmatil.txt' does not exist !", outnote)

        def oneDrug11():
            """
            Per drug invega
            """
            try:
                if os.path.getsize('./medifiles/perdrug/invega.txt'):
                    print("+ File 'invega.txt' exist (read)!")
                    with open('./medifiles/perdrug/invega.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'invega.txt' does not exist !", outnote)

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

        def oneDrug14():
            """
            Per drug risperdal
            """
            try:
                if os.path.getsize('./medifiles/perdrug/risperdal.txt'):
                    print("+ File 'risperdal.txt' exist (read)!")
                    with open('./medifiles/perdrug/risperdal.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'risperdal.txt' does not exist !", outnote)

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

        def oneDrug21():
            """
            Per drug ethosuximide
            """
            try:
                if os.path.getsize('./medifiles/perdrug/ethosuximide.txt'):
                    print("+ File 'ethosuximide.txt' exist (read)!")
                    with open('./medifiles/perdrug/ethosuximide.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'ethosuximide.txt' does not exist !", outnote)

        def oneDrug22():
            """
            Per drug mysoline
            """
            try:
                if os.path.getsize('./medifiles/perdrug/mysoline.txt'):
                    print("+ File 'mysoline.txt' exist (read)!")
                    with open('./medifiles/perdrug/mysoline.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'mysoline.txt' does not exist !", outnote)

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

        def oneDrug28():
            """
            Per drug inovelon
            """
            try:
                if os.path.getsize('./medifiles/perdrug/inovelon.txt'):
                    print("+ File 'inovelon.txt' exist (read)!")
                    with open('./medifiles/perdrug/inovelon.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'inovelon.txt' does not exist !", outnote)

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

        def oneDrug33():
            """
            Per drug sabril
            """
            try:
                if os.path.getsize('./medifiles/perdrug/sabril.txt'):
                    print("+ File 'sabril.txt' exist (read)!")
                    with open('./medifiles/perdrug/sabril.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'sabril.txt' does not exist !", outnote)

        def oneDrug34():
            """
            Per drug taloxa
            """
            try:
                if os.path.getsize('./medifiles/perdrug/taloxa.txt'):
                    print("+ File 'taloxa.txt' exist (read)!")
                    with open('./medifiles/perdrug/taloxa.txt', 'r') as textfile:
                        lines = textfile.readlines()
                        for li in lines:
                            self.textBox.insert(END, li)
            except FileNotFoundError as outnote:
                print("+ Sorry, file 'taloxa.txt' does not exist !", outnote)

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
