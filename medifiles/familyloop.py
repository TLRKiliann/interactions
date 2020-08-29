#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.func_pack.funcfamily import *


def familyLoop(self, drug1):
    for i in familiyttt:
        if i == "antipsychotiques":
            if drug1 == i or drug1 == "apsy":
                familyPsycho(self)
        elif i == "antiépileptiques":
            if drug1 == i or drug1 == "mae":
                familyMae(self)
        elif i == "antidépresseurs":
            if drug1 == i or drug1 == "atd":
                familyAtd(self)
        elif i == "anxiolytiques":
            if drug1 == i or drug1 == "anxio":
                familyAnxio(self)
        elif i == "thymorégulateurs":
            if drug1 == i or drug1 == "stabilisateurs":
                familyThymo(self)
        elif i == "somnifères":
            if drug1 == i or drug1 == "somni" or drug1 == "inducteurs de sommeil":
                familySomni(self)
        elif i == "benzodiazépines":
            if drug1 == i or drug1 == "bzd":
                familyBzd(self)
        elif i == "inhibiteurs de la cholinestérase":
            if drug1 == i or drug1 == "idlc":
                familyIcho(self)
        elif i == "antiparkinsoniens":
            if drug1 == i or drug1 == "apk":
                familyPark(self)
        else:
            print("+ End of familyloop list !")
