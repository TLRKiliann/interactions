#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_clopixol import *


def clopixoFunc(self, drug3, drug4):
    """
    drug1 VS drug2 (interactions with seroquel)
    """
    for i in oneDrug:
        if i == "clopixol" or i == "zuclopenthixol":
            if (drug3 == i or drug4 == i) and (drug3 == "neuro" or \
                drug3 == "antipsychotiques" or drug3 == "neuroleptiques" or \
                drug3 == "apsy" or drug4 == "neuro" or \
                drug4 == "antipsychotiques" or drug4 == "neuroleptiques" or \
                drug4 == "apsy"):
                print("+ Interactions carbamazépine !!!")
                importClopiNeuro(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "haldol" or \
                drug3 == "halopéridol" or drug4 == "haldol" or \
                drug4 == "halopéridol"):
                print("+ Interactions haldol !!!")
                importClopiHaldo(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "seroquel" or \
                drug3 == "quétiapine" or drug3 == "sequase" or \
                drug4 == "seroquel" or drug4 == "sequase" or \
                drug4 == "quétiapine"):
                print("+ Interactions quétiapine !!!")
                importClopiSero(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
                drug3 == "thymo" or drug3 == "stab" or \
                drug3 == "lithiofor" or drug4 == "lithium" or \
                drug4 == "thymo" or drug4 == "stab" or \
                drug4 == "lithiofor"):
                print("+ Interactions lithium !!!")
                importClopiLith(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "bzd" or \
                drug3 == "benzodiazépines" or drug4 == "bzd" or \
                drug4 == "benzodiazépines"):
                print("+ Interactions bzd !!!")
                importClopiBzd(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "apk" or \
                drug3 == "L-dopa" or drug3 == "levodopa" or \
                drug4 == "apk" or drug4 == "L-dopa" or \
                drug4 == "levodopa"):
                print("+ Interactions apk !!!")
                importClopiDopa(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "ahyperTA" or \
                drug3 == "guanéthidine" or drug4 == "ahyperTA" or \
                drug4 == "guanéthidine"):
                print("+ Interactions antihta !!!")
                importClopiHta(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "antiA" or \
                drug3 == "antiarythmiques" or drug4 == "antiA" or \
                drug4 == "antiarythmiques"):
                print("+ Interactions antiarythmiques !!!")
                importClopiAntiArytm(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "antihist" or \
                drug3 == "antihistaminiques" or drug4 == "antihist" or \
                drug4 == "antihistaminiques"):
                print("+ Interactions antihistaminiques !!!")
                importClopiAntiHist(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "atb" or \
                drug3 == "antibiotiques" or drug4 == "atb" or \
                drug4 == "antibiotiques"):
                print("+ Interactions atb !!!")
                importClopiAtb(self)



            elif (drug3 == i or drug4 == i) and (drug3 == "opio" or \
                drug3 == "opioïdes" or drug4 == "opio" or \
                drug4 == "opioïdes"):
                print("+ Interactions opioïdes !!!")
                importClopiOpio(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "oh" or \
                drug3 == "alcool" or drug4 == "oh" or \
                drug4 == "alcool"):
                print("+ Interactions alcool !!!")
                importClopiOh(self)
            else:
                print("+ End of clopixoloop ttt list !")
