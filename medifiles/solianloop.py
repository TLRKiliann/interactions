#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_solian import *


def solianFunc(self, drug3, drug4):
    """
    drug1 VS drug2 (interactions with solian)
    """
    for i in oneDrug:
        if i == "solian" or i == "amisulpride":
            if (drug3 == i or drug4 == i):
                print("+ Interactions bcp trop d'interactions !!!")
                importSolianBordel(self)
            else:
                print("+ End of solianloop ttt list !")