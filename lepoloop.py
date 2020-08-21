#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from listfile import *
from interdrugs import *


def lepoLoop(self, drug3, drug4):
    for i in oneDrug:
        """
        drug1 VS drug2 (interactions with clopin)
        """
        if i == "leponex" or i == "clozapine" or i == "clopin":
            if (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
                drug3 == "tégrétol" or drug4 == "carbamazépine" or \
                drug4 == "tégrétol"):
                print("+ Interactions !!!")
                importationLepoCarba(self)

            elif (drug3 == i or drug4 == i) and \
                (drug3 == "inhibiteurs de la pompe à protons" or \
                drug3 == "IPP" or \
                drug4 == "inhibiteurs de la pompe à protons" or \
                drug4 == "IPP"):
                print("+ Interactions !!!")
                importationLepoIpp(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "antidépresseurs" or \
                drug3 == "ATD" or drug4 == "antidépresseurs" or \
                drug4 == "ATD"):
                print("+ Interactions !!!")
                importationLepoAtd(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "ATB" or \
                drug3 == "antibiotiques" or drug4 == "ATB" or \
                drug4 == "antibiotiques"):
                print("+ Interactions !!!")
                importationLepoAtb(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "antihistaminiques" or \
                drug4 == "antihistaminiques"):
                print("+ Interactions !!!")
                importationLepoAntiHist(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "antiépileptiques" or \
                drug4 == "antiépileptiques" or drug3 == "MAE" or drug4 == "MAE"):
                print("+ Interactions !!!")
                importationLepoMae(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "neuroleptiques" or \
                drug4 == "neuroleptiques" or drug3 == "neuro" or drug4 == "neuro"):
                print("+ Interactions !!!")
                importationLepoNeuro(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "benzodiazépines" or \
                drug4 == "benzodiazépines" or drug3 == "BZD" or drug4 == "BZD"):
                print("+ Interactions !!!")
                importationLepoBzd(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "alcool" or \
                drug4 == "alcool" or drug3 == "oh" or drug4 == "oh"):
                print("+ Interactions !!!")
                importationLepoOh(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "méthadone" or \
                drug4 == "méthadone" or drug3 == "meoh" or drug4 == "meoh"):
                print("+ Interactions !!!")
                importationLepoMeOH(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
                drug4 == "lithium"):
                print("+ Interactions !!!")
                importationLepoLith(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "anticoagulants" or \
                drug4 == "anticoagulants"):
                print("+ Interactions !!!")
                importationLepoCoag(self)
            else:
                print("Loop to search drug3 and drug4...")
