#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interdrugs import *


def depaFunc(self, drug3, drug4):
    for i in oneDrug:
        """
        drug1 VS drug2 (interactions with carbamazépine)
        """
        if i == "dépakine" or i == "valproate":
            if (drug3 == i or drug4 == i) and (drug3 == "antidépresseurs" or \
                drug4 == "antidépresseurs" or drug3 == "atd" or drug4 == "atd"):
                print("+ Interactions !!!")
                importDepakAtd(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "antiépileptiques" or \
                drug4 == "antiépileptiques" or drug3 == "mae" or drug4 == "mae"):
                print("+ Interactions !!!")
                importDepakMae(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "neuroleptiques" or \
                drug4 == "neuroleptiques" or drug3 == "neuro" or drug4 == "neuro"):
                print("+ Interactions !!!")
                importDepakNeuro(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "benzodiazépines" or \
                drug4 == "benzodiazépines" or drug3 == "bzd" or drug4 == "bzd"):
                print("+ Interactions !!!")
                importDepakBzd(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "alcool" or \
                drug4 == "alcool" or drug3 == "oh" or drug4 == "oh"):
                print("+ Interactions !!!")
                importDepakOh(self)
            else:
                print("Loop to search drug3 and drug4...")
