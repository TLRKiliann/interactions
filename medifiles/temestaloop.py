#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_temesta import *


def temestaFunc(self, drug3, drug4):
    """
    drug1 VS drug2 (interactions with temesta)
    """
    for i in oneDrug:
        if i == "temesta" or i == "lorazépam":
            if (drug3 == i or drug4 == i) and (drug3 == "neuro" or \
                drug3 == "apsy" or drug4 == "neuro" or \
                drug4 == "apsy"):
                print("+ Interactions !!!")
                importTemestaNeuro(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "oh" or \
                drug3 == "alcool" or drug4 == "alcool" or \
                drug4 == "oh"):
                print("+ Interactions oh !!!")
                importTemestaOh(self)

            else:
                print("+ End of seroloop ttt list !")