#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_depakine import *


def depaFunc(self, drug3, drug4):
    for i in oneDrug:
        """
        drug1 VS drug2 (interactions with carbamazépine)
        """
        if i == "dépakine" or i == "valproate":
            if (drug3 == i or drug4 == i) and (drug3 == "anticoagulants" or \
                drug4 == "anticoagulants" or drug3 == "anticoag" or \
                drug4 == "anticoag"):
                print("+ Interactions !!!")
                importDepakAnticoag(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "antidépresseurs" or \
                drug4 == "antidépresseurs" or drug3 == "atd" or \
                drug4 == "atd"):
                print("+ Interactions !!!")
                importDepakAtd(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "antiépileptiques" or \
                drug4 == "antiépileptiques" or drug3 == "mae" or \
                drug4 == "mae"):
                print("+ Interactions !!!")
                importDepakMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "taloxa" or \
                drug4 == "taloxa" or drug3 == "felbamate" or \
                drug4 == "felbamate"):
                print("+ Interactions !!!")
                importDepakMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "rufinamide" or \
                drug4 == "rufinamide" or drug3 == "inovelon" or \
                drug4 == "inovelon"):
                print("+ Interactions !!!")
                importDepakMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "lamotrigine" or \
                drug4 == "lamotrigine" or drug3 == "lamictal" or \
                drug4 == "lamictal"):
                print("+ Interactions !!!")
                importDepakMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
                drug4 == "carbamazépine" or drug3 == "tégrétol" or \
                drug4 == "tégrétol"):
                print("+ Interactions !!!")
                importDepakMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "phénytoïne" or \
                drug4 == "phénytoïne"):
                print("+ Interactions !!!")
                importDepakMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "mysoline" or \
                drug4 == "mysoline" or drug3 == "primidone" or \
                drug4 == "primidone"):
                print("+ Interactions !!!")
                importDepakMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "phénobarbital" or \
                drug4 == "phénobarbital" or drug3 == "aphénylbarbite" or \
                drug4 == "aphénylbarbite"):
                print("+ Interactions !!!")
                importDepakMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "topamax" or \
                drug4 == "topamax" or drug3 == "topiramate" or \
                drug4 == "topiramate"):
                print("+ Interactions !!!")
                importDepakMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "diamox" or \
                drug4 == "diamox" or drug3 == "acétazolamide" or \
                drug4 == "acétazolamide"):
                print("+ Interactions !!!")
                importDepakMae(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "neuroleptiques" or \
                drug4 == "neuroleptiques" or drug3 == "neuro" or \
                drug4 == "neuro"):
                print("+ Interactions !!!")
                importDepakNeuro(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "benzodiazépines" or \
                drug4 == "benzodiazépines" or drug3 == "bzd" or \
                drug4 == "bzd"):
                print("+ Interactions !!!")
                importDepakBzd(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "alcool" or \
                drug4 == "alcool" or drug3 == "oh" or \
                drug4 == "oh"):
                print("+ Interactions !!!")
                importDepakOh(self)
            else:
                print("Loop to search depakine and interactions...")
