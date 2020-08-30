#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_temesta import *


def temestaFunc(self, drug3, drug4):
    """
    drug1 VS drug2 (interactions with temesta)
    """
    for i in oneDrug:
        if i == "temesta" or i == "lorazépam":
            if (drug3 == i or drug4 == i) and (drug3 == "neuro" or \
                drug3 == "apsy" or drug3 == "antipsychotiques" or \
                drug4 == "neuro" or drug4 == "antipsychotiques" or \
                drug4 == "apsy"):
                print("+ Interactions apsy !!!")
                importTemestaNeuro(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "leponex" or \
                drug3 == "clopin" or drug3 == "clozapine" or \
                drug4 == "clozapine" or drug4 == "leponex" or \
                drug4 == "clopin"):
                print("+ Interactions clozapine !!!")
                importTemestaNeuro(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "mae" or \
                drug3 == "depakine" or drug3 == "valproate" or \
                drug4 == "valproate" or drug4 == "mae" or \
                drug4 == "depakine"):
                print("+ Interactions valproate (mae) !!!")
                importTemestaMae(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "hypno" or \
                drug3 == "somni" or drug3 == "hypnotiques" or \
                drug4 == "somni" or drug4 == "hypno" or \
                drug4 == "hypnotiques"):
                print("+ Interactions hypno !!!")
                importTemestaNeuro(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "bzd" or \
                drug3 == "anxio" or drug3 == "anxiolytiques" or \
                drug3 == "benzodiazépines" or drug4 == "anxio" or \
                drug4 == "anxiolytiques" or drug4 == "bzd" or \
                drug4 == "benzodiazépines"):
                print("+ Interactions bzd !!!")
                importTemestaNeuro(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "atd" or \
                drug3 == "antidépresseurs" or \
                drug4 == "antidépresseurs" or drug4 == "atd"):
                print("+ Interactions atd !!!")
                importTemestaNeuro(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "anest" or \
                drug3 == "anesthésiques" or \
                drug4 == "anesthésiques" or drug4 == "anest"):
                print("+ Interactions atd !!!")
                importTemestaNeuro(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "myo" or \
                drug3 == "myorelaxants" or \
                drug4 == "myorelaxants" or drug4 == "myo"):
                print("+ Interactions atd !!!")
                importTemestaNeuro(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "antihist" or \
                drug3 == "antihistaminiques" or \
                drug4 == "antihistaminiques" or drug4 == "antihist"):
                print("+ Interactions atd !!!")
                importTemestaNeuro(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "opio" or \
                drug3 == "opioïdes" or drug3 == "meoh" or \
                drug3 == "méthadone" or drug4 == "opioïdes" or \
                drug4 == "opio" or drug4 == "meoh" or \
                drug4 == "méthadone"):
                print("+ Interactions atd !!!")
                importTemestaOpio(self)


            elif (drug3 == i or drug4 == i) and (drug3 == "oh" or \
                drug3 == "alcool" or drug4 == "alcool" or \
                drug4 == "oh"):
                print("+ Interactions oh !!!")
                importTemestaOh(self)

            else:
                print("+ End of temestaloop ttt list !")