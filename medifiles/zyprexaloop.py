#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_zyprexa import *


def zyprexFunc(self, drug3, drug4):
    for i in oneDrug:
        """
        drug1 VS drug2 (interactions with abilify)
        """
        if i == "abilify" or i == "aripiprazol":
            if (drug3 == i or drug4 == i) and (drug3 == "phénytoïne" or \
                drug3 == "phénobarbital" or drug3 == "aphénylbarbite" or \
                drug3 == "anti-épileptiques" or drug3 == "mae" or \
                drug4 == "phénytoïne" or drug4 == "mae" or \
                drug4 == "aphénylbarbite" or drug4 == "anti-épileptiques" or \
                drug4 == "phénobarbital"):
                print("+ Interactions mae !!!")
                importZyprexMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "atd" or \
                drug3 == "fluvoxamine" or drug3 == "antidépresseurs" or \
                drug3 == "prozac" or drug3 == "floxyfral" or
                drug3 == "fluanxol" or drug4 == "atd" or \
                drug4 == "fluvoxamine" or drug4 == "antidépresseurs" or \
                drug4 == "prozac" or drug4 == "fluanxol" or \
                drug4 == "floxyfral"):
                print("+ Interactions atd !!!")
                importZyprexAtd(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "tabac" or \
                drug4 == "tabac"):
                print("+ Interactions tabac !!!")
                importZyprexTabac(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "oh" or \
                drug3 == "alcool" or drug4 == "oh" or \
                drug4 == "alcool"):
                print("+ Interactions oh !!!")
                importZyprexOh(self)
            else:
                print("+ End of zyprexaloop ttt list !")
