#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_seroquel import *


def seroFunc(self, drug3, drug4):
    """
    drug1 VS drug2 (interactions with seroquel)
    """
    for i in oneDrug:
        if i == "seroquel" or i == "sequase" or i == "quétiapine":
            if (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
                drug4 == "carbamazépine" or drug3 == "tégrétol" or \
                drug4 == "tégrétol"):
                print("+ Interactions ultraviolente !!!")
                importSeroCarba(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "depakine" or \
                drug3 == "valproate" or drug4 == "depakine" or \
                drug4 == "valproate"):
                print("+ Interactions !!!")
                importSeroDepak(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "érythromycine" or \
                drug4 == "érythromycine"):
                print("+ Interactions !!!")
                importSeroEry(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "kétoconazol" or \
                drug3 == "keto" or drug4 == "kétoconazol" or drug4 == keto):
                print("+ Interactions !!!")
                importSeroKeto(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
                drug4 == "lithium"):
                print("+ Interactions !!!")
                importSeroLith(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "methadone" or \
                drug3 == "meoh" or drug4 == "methadone" or \
                drug4 == "meoh"):
                print("+ Interactions !!!")
                importSeroMeoh(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "oh" or \
                drug3 == "alcool" or drug4 == "oh" or \
                drug4 == "alcool"):
                print("+ Interactions !!!")
                importSeroOh(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "phénitoïne" or \
                drug3 == "aphénylbarbite" or drug4 == "phénitoïne" or \
                drug4 == "aphénylbarbite"):
                print("+ Interactions !!!")
                importSeroPheny(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "risperdal" or \
                drug3 == "risperdone" or drug4 == "risperdal" or \
                drug4 == "risperdone"):
                print("+ Interactions !!!")
                importSeroRisp(self)
            else:
                print("+ End of seroloop ttt list !")
