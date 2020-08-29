#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.func_pack.funcatddrug import *


def atdDrugLoop(self, drug2):
    for i in oneDrug:
        if i == "anafranil" or i == "clomipramine":
            if drug2 == i:
                atdDrug1(self)
        elif i == "saroten" or i == "amitriptyline":
            if drug2 == i:
                atdDrug2(self)
        elif i == "surmontil" or i == "trimipramine":
            if drug2 == i:
                atdDrug3(self)
        elif i == "trittico" or i == "trazodone":
            if drug2 == i:
                atdDrug4(self)
        else:
            print("End of atd loop !")
