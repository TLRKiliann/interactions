#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from listfile import *
from funcatddrug import *


def atdDrugLoop(self, drug2):
    for i in oneDrug:
        if i == "anafranil" or i == "...":
            if drug2 == i:
                atdDrug1(self)
        elif i == "ludiomil" or i == "...":
            if drug2 == i:
                atdDrug2(self)
        elif i == "saroten" or i == "...":
            if drug2 == i:
                atdDrug3(self)
        elif i == "surmontil" or i == "...":
            if drug2 == i:
                atdDrug4(self)
        elif i == "tofranil" or i == "...":
            if drug2 == i:
                atdDrug5(self)
        elif i == "trittico" or i == "...":
            if drug2 == i:
                atdDrug6(self)
        else:
            print("This atd is not in the list")
