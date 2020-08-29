#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.func_pack.funcstabdrug import *


def stabDrugLoop(self, drug2):
    for i in oneDrug:
        if i == "lithiofor" or i == "lithium":
            if drug2 == i:
                stabDrug1(self)
        else:
            print("End of stab loop !")