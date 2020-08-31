#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_tranxilium import *


def tranxiFunc(self, drug3, drug4):
    for i in oneDrug:
        """
        drug1 VS drug2 (interactions with tranxilium)
        """
        if i == "tranxilium" or i == "clorazépate":
            if (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
                drug3 == "tégrétol" or drug4 == "carbamazépine" or \
                drug4 == "tégrétol"):
                print("+ Interactions carbamazépine !!!")
                importTranxi...(self)