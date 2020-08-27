#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.func_pack.funcapdrug import *


def antipsyDrugLoop(self, drug2):
    # Don't forget kemadrin akineton
    for i in oneDrug:
        if i == "clopin" or i == "leponex" or i == "clozapine":
            if drug2 == i:
                antipsyDrug1(self)
        elif i == "prazine" or i == "chlorpromazine":
            if drug2 == i:
                antipsyDrug2(self)
        elif i == "clopixol" or i == "zuclopenthixol":
            if drug2 == i:
                antipsyDrug3(self)
        elif i == "entumine" or i == "clotiapine":
            if drug2 == i:
                antipsyDrug4(self)
        elif i == "fluanxol" or i == "flupentixol":
            if drug2 == i:
                antipsyDrug5(self)
        elif i == "haldol" or i == "halopéridol":
            if drug2 == i:
                antipsyDrug6(self)
        elif i == "nozinan" or i == "levomepromazine":
            if drug2 == i:
                antipsyDrug7(self)
        elif i == "tiapridal" or i == "tiapride":
            if drug2 == i:
                antipsyDrug8(self)
        elif i == "abilify" or i == "aripiprazol":
            if drug2 == i:
                antipsyDrug9(self)
        elif i == "dogmatil" or i == "sulpride":
            if drug2 == i:
                antipsyDrug10(self)
        elif i == "invega" or i == "palipéridone":
            if drug2 == i:
                antipsyDrug11(self)
        elif i == "olanzapine" or i == "zyprexa":
            if drug2 == i:
                antipsyDrug12(self)
        elif i == "risperdal" or i == "risperdone":
            if drug2 == i:
                antipsyDrug14(self)
        elif i == "sequase" or i == "seroquel" or i == "quétiapine":
            if drug2 == i:
                antipsyDrug16(self)
        elif i == "solian" or i == "amisulpride":
            if drug2 == i:
                antipsyDrug17(self)
        else:
            print("This antipsy is not in the list")
