#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_tranxilium import *


def tranxiFunc(self, drug3, drug4):
    for i in oneDrug:
        """
        drug1 VS drug2 (interactions with tranxilium)
        """
        if i == "tranxilium" or i == "clorazépate":
            if (drug3 == i or drug4 == i) and (drug3 == "clozapine" or \
                drug3 == "neuro" or drug3 == "apsy" or \
                drug3 == "antipsychotiques" or drug4 == "apsy" or \
                drug4 == "antipsychotiques" or drug4 == "clozapine" or \
                drug4 == "neuro"):
                print("+ Interactions clozapine et neuro !!!")
                importTranxiNeuro(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "bzd" or \
                drug3 == "benzodiazépines" or drug3 == "anxio" or \
                drug3 == "anxiolytiques" or drug4 == "anxiolytiques" or \
                drug4 == "anxio" or drug4 == "bzd" or \
                drug4 == "benzodiazépines"):
                print("+ Interactions bzd + anxio !!!")
                importTranxiBzd(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "bzd" or \
                drug3 == "benzodiazépines" or \
                drug4 == "bzd" or drug4 == "benzodiazépines"):
                print("+ Interactions bzd + anxio !!!")
                importTranxiHypno(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "myo" or \
                drug3 == "myorelaxants" or drug4 == "myorelaxants" or \
                drug4 == "myo"):
                print("+ Interactions bzd + anxio !!!")
                importTranxiMyo(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "atd" or \
                drug3 == "anxiolytiques" or drug3 == "anxio" or \
                drug3 == "atuss" or drug3 == "antihist" or drug3 == "clonidine" or\
                drug3 == "buprénorphine" or drug3 == "barbituriques" or \
                drug3 == "antidépresseurs" or drug4 == "antidépresseurs" or \
                drug4 == "buprénorphine" or drug4 == "barbituriques" or \
                drug4 == "atuss" or drug4 == "antihist" or \
                drug4 == "anxio" or drug4 == "atd" or drug4 == "clonidine" or \
                drug4 == "anxiolytiques"):
                print("+ Interactions bzd + anxio !!!")
                importTranxiGroup(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "ipp" or \
                drug3 == "cimétidine" or drug3 == "oméoprazole" or \
                drug4 == "oméoprazole" or drug4 == "ipp" or \
                drug4 == "cimétidine"):
                print("+ Interactions ipp !!!")
                importTranxiIpp(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "opio" or \
                drug3 == "opioïdes" or drug3 == "meoh" or \
                drug3 == "méthadone" or drug4 == "meoh" or \
                drug4 == "opio" or drug4 == "méthadone" or \
                drug4 == "opioïdes"):
                print("+ Interactions opio !!!")
                importTranxiOpio(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "oh" or \
                drug3 == "alcool" or drug4 == "alcool" or \
                drug4 == "oh"):
                print("+ Interactions oh !!!")
                importTranxiOh(self)