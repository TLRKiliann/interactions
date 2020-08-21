#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from listfile import *
from interdrugs import *


def seroLoop(self, drug3, drug4):
    """
    drug1 VS drug2 (interactions with seroquel)
    """
    for i in oneDrug:
        if i == "seroquel" or i == "sequase" or i == "quétiapine":
            if (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
                drug4 == "carbamazépine" or drug3 == "tégrétol" or \
                drug4 == "tégrétol"):
                print("+ Interactions ultraviolente !!!")
                importationViolente(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "dépakine" or \
                drug3 == "valproate" or drug4 == "dépakine" or \
                drug4 == "valproate"):
                print("+ Interactions !!!")
                importationSeroDepak(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "érythromycine" or \
                drug4 == "érythromycine"):
                print("+ Interactions !!!")
                importationSeroEry(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "kétoconazol" or \
                drug4 == "kétoconazol"):
                print("+ Interactions !!!")
                importationSeroKeto(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
                drug4 == "lithium"):
                print("+ Interactions !!!")
                importationSeroLith(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "methadone" or \
                drug3 == "meoh" or drug4 == "methadone" or \
                drug4 == "meoh"):
                print("+ Interactions !!!")
                importationSeroMeoh(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "oh" or \
                drug3 == "alcool" or drug4 == "oh" or \
                drug4 == "alcool"):
                print("+ Interactions !!!")
                importationSeroOh(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "phénitoïne" or \
                drug3 == "aphénylbarbite" or drug4 == "phénitoïne" or \
                drug4 == "aphénylbarbite"):
                print("+ Interactions !!!")
                importationSeroPheny(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "risperdal" or \
                drug3 == "risperdone" or drug4 == "risperdal" or \
                drug4 == "risperdone"):
                print("+ Interactions !!!")
                importationSeroRisp(self)
            else:
                print("Loop to search drug3 and drug4...")
