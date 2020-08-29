#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_abilify import *


def ariFunc(self, drug3, drug4):
    for i in oneDrug:
        """
        drug1 VS drug2 (interactions with abilify)
        """
        if i == "abilify" or i == "aripiprazol":
            if (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
                drug4 == "carbamazépine" or drug3 == "tégrétol" or \
                drug4 == "tégrétol"):
                print("+ Interactions !!!")
                importAriCarba(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "mae" or \
                drug4 == "mae" or drug3 == "antiépileptiques" or \
                drug4 == "antiépileptiques"):
                print("+ Interactions !!!")
                importAriCarba(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "primidone" or \
                drug4 == "primidone" or drug3 == "mysoline" or \
                drug4 == "mysoline"):
                print("+ Interactions !!!")
                importAriCarba(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "phénobarbital" or \
                drug4 == "phénobarbital" or drug3 == "aphénylbarbite" or \
                drug4 == "aphénylbarbite"):
                print("+ Interactions !!!")
                importAriCarba(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "phénytoïne" or \
                drug4 == "phénytoïne"):
                print("+ Interactions !!!")
                importAriCarba(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "depakine" or \
                drug4 == "depakine" or drug3 == "valproate" or \
                drug4 == "valproate"):
                print("+ Interactions !!!")
                importAriVal(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "lithiofor" or \
                drug4 == "lithiofor" or drug3 == "lithium" or \
                drug4 == "lithium"):
                print("+ Interactions !!!")
                importAriVal(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "isrs" or \
                drug3 == "irsn" or drug4 == "isrs" or \
                drug4 == "irsn"):
                print("+ Interactions !!!")
                importAriSrs(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "fluoxétine" or \
                drug4 == "fluoxétine"):
                print("+ Interactions !!!")
                importAriFluo(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "paroxétine" or \
                drug4 == "paroxétine" or drug3 == "deroxat" or \
                drug4 == "deroxat"):
                print("+ Interactions !!!")
                importAriFluo(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "apalu" or \
                drug4 == "apalu" or drug3 == "quinidine" or \
                drug4 == "quinidine"):
                print("+ Interactions !!!")
                importAriFluo(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "kétoconazole" or \
                drug3 == "keto" or drug4 == "kétoconazole" or drug4 == "keto"):
                print("+ Interactions !!!")
            elif (drug3 == i or drug4 == i) and (drug3 == "ahyperTA" or \
                drug4 == "ahyperTA"):
                print("+ Interactions !!!")
                importAriTa(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "ac" or \
                drug4 == "ac" or drug3 == "warfarine" or \
                drug4 == "warfarine" or \
                drug3 == "bexine" or drug4 == "bexine" or \
                drug3 == "dextrométhorphane" or \
                drug4 == "dextrométhorphane"):
                print("+ Interactions !!!")
                importAriMiscel(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "oméoprazole" or \
                drug4 == "oméoprazole" or drug3 == "ipp" or \
                drug4 == "ipp"):
                print("+ Interactions !!!")
                importAriFluo(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "oh" or \
                drug3 == "alcool" or drug4 == "oh" or drug4 == "alcool"):
                print("+ Interactions !!!")
                importAriOh(self)
            else:
                print("+ End of aripiloop ttt list !")
