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
            if (drug3 == i or drug4 == i) and (drug3 == "" or \
                drug4 == "" or drug3 == "" or \
                drug4 == ""):
                print("+ Interactions ... !!!")
                importZyprexNeuro(self)

            else:
                print("+ End of zyprexaloop ttt list !")
