#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.func_pack.funcanxidrug import *


def anxioDrugLoop(self, drug2):
    for i in oneDrug:
        if i == "atarax":
            if drug2 == i:
                anxioDrug40(self)
        elif i == "demetrin" or i == "prazépam":
            if drug2 == i:
                anxioDrug42(self)
        elif i == "lexotanil" or i == "bromazépam":
            if drug2 == i:
                anxioDrug43(self)
        elif i == "rivotril" or i == "clonazépam":
            if drug2 == i:
                anxioDrug44(self)
        elif i == "rohypnol" or i == "flunitrazepamum":
            if drug2 == i:
                anxioDrug45(self)
        elif i == "seresta" or i == "oxazépam":
            if drug2 == i:
                anxioDrug46(self)
        elif i == "temesta" or i == "lorazépam":
            if drug2 == i:
                anxioDrug47(self)
        elif i == "tranxilium" or i == "clorazépate":
            if drug2 == i:
                anxioDrug48(self)
        elif i == "urbanyl" or i == "clobazam":
            if drug2 == i:
                anxioDrug49(self)
        elif i == "valium" or i == "diazépam":
            if drug2 == i:
                anxioDrug50(self)
        elif i == "xanax" or i == "alprazolam":
            if drug2 == i:
                anxioDrug51(self)
        else:
            print("End of anxio loop !")