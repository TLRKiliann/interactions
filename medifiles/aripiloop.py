#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_abilify import *


def ariFunc(self, drug3, drug4):
    for i in oneDrug:
        """
        drug1 VS drug2 (interactions with depakine)
        """
        if i == "abilify" or i == "aripiprazol":
            if (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
                drug4 == "carbamazépine" or drug3 == "tégrétol" or \
                drug4 == "tégrétol"):
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
            else:
                print("abilify n'a pas d'interactions avec ce médic !")