#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_depakine import *


def depaFunc(self, drug3, drug4):
    for i in oneDrug:
        """
        drug1 VS drug2 (interactions with depakine)
        """
        if i == "depakine" or i == "valproate":
            if (drug3 == i or drug4 == i) and (drug3 == "anticoagulants" or \
                drug4 == "anticoagulants" or drug3 == "ac" or \
                drug4 == "ac"):
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
                importDepakTopadia(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "diamox" or \
                drug4 == "diamox" or drug3 == "acétazolamide" or \
                drug4 == "acétazolamide"):
                print("+ Interactions !!!")
                importDepakTopadia(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "neuroleptiques" or \
                drug4 == "neuroleptiques" or drug3 == "neuro" or \
                drug3 == "antipsy" or drug4 == "neuro" or drug4 == "antipsy"):
                print("+ Interactions !!!")
                importDepakNeuro(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "olanzapine" or \
                drug4 == "olanzapine" or drug3 == "zyprexa" or \
                drug4 == "zyprexa"):
                print("+ Interactions !!!")
                importDepakNeuro(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "seroquel" or \
                drug4 == "seroquel" or drug3 == "sequase" or \
                drug3 == "quétiapine" or drug4 == "sequase" or \
                drug4 == "quétiapine"):
                print("+ Interactions !!!")
                importDepakNeuro(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
                drug4 == "lithium"):
                print("+ Interactions !!!")
                importDepakLith(self)
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
            elif (drug3 == i or drug4 == i) and (drug3 == "antibiotiques" or \
                drug4 == "antibiotiques" or drug3 == "atb" or \
                drug4 == "atb"):
                print("+ Interactions !!!")
                importDepakAtb(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "contraceptifs" or \
                drug4 == "contraceptifs" or drug3 == "cc" or \
                drug4 == "cc"):
                print("+ Interactions !!!")
                importDepakContracep(self)
            else:
                print("Loop to search depakine and interactions...")
