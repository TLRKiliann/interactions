#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_leponex import *


def lepoFunc(self, drug3, drug4):
    for i in oneDrug:
        """
        drug1 VS drug2 (interactions with clopin)
        """
        if i == "leponex" or i == "clozapine" or i == "clopin":
            if (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
                drug3 == "tégrétol" or drug4 == "carbamazépine" or \
                drug4 == "tégrétol"):
                print("+ Interactions !!!")
                importLepoCarba(self)
            elif (drug3 == i or drug4 == i) and \
                (drug3 == "inhibiteurs de la pompe à protons" or \
                drug3 == "ipp" or \
                drug4 == "inhibiteurs de la pompe à protons" or \
                drug4 == "ipp"):
                print("+ Interactions !!!")
                importLepoIpp(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "antidépresseurs" or \
                drug3 == "atd" or drug4 == "antidépresseurs" or \
                drug4 == "atd"):
                print("+ Interactions !!!")
                importLepoAtd(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "atb" or \
                drug3 == "antibiotiques" or drug4 == "atb" or \
                drug4 == "antibiotiques"):
                print("+ Interactions !!!")
                importLepoAtb(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "antihistaminiques" or \
                drug3 == "antihist" or drug4 == "antihist" or drug4 == "antihistaminiques"):
                print("+ Interactions !!!")
                importLepoAntiHist(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "antiépileptiques" or \
                drug4 == "antiépileptiques" or drug3 == "mae" or drug4 == "mae"):
                print("+ Interactions !!!")
                importLepoMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "neuroleptiques" or \
                drug4 == "neuroleptiques" or drug3 == "neuro" or drug4 == "neuro"):
                print("+ Interactions !!!")
                importLepoNeuro(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "benzodiazépines" or \
                drug4 == "benzodiazépines" or drug3 == "bzd" or drug4 == "bzd"):
                print("+ Interactions !!!")
                importLepoBzd(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "alcool" or \
                drug4 == "alcool" or drug3 == "oh" or drug4 == "oh"):
                print("+ Interactions !!!")
                importLepoOh(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "méthadone" or \
                drug4 == "méthadone" or drug3 == "meoh" or drug4 == "meoh"):
                print("+ Interactions !!!")
                importLepoMeOH(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
                drug3 == "lithiofor" or drug4 == "lithium" or drug4 == "lithiofor"):
                print("+ Interactions !!!")
                importLepoLith(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "anticoagulants" or \
                drug3 == "ac" or drug4 == "anticoagulants" or drug4 == "ac"):
                print("+ Interactions !!!")
                importLepoCoag(self)
            else:
                print("+ End of lepoloop ttt list !")
                