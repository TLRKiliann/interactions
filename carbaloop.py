#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from listfile import *
from interdrugs import *


def carbaLoop(self, drug3, drug4):
    for i in oneDrug:
        """
        drug1 VS drug2 (interactions with carbamazépine)
        """
        if i == "carbamazépine" or i == "tégrétol":
            if (drug3 == i or drug4 == i) and (drug3 == "sintrom" or \
                drug3 == "xarelto" or drug3 == "Rivaroxaban" or \
                drug3 == "héparine" or drug3 == "pradaxa" or \
                drug4 == "eliquis" or \
                drug4 == "sintrom" or drug4 == "xarelto" or \
                drug4 == "Rivaroxaban" or drug4 == "héparine" or \
                drug4 == "pradaxa" or drug4 == "eliquis"):
                print("+ Interactions !!!")
                importationCarbaAnticoa(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "atb" or \
                drug3 == "ciprofloxacine" or drug3 == "érythromycine" or \
                drug3 == "clarithromycine" or drug3 == "rifabutine" or \
                drug3 == "doxycycline" or drug3 == "troléandomycine" or \
                drug3 == "josamycine" or drug4 == "atb" or \
                drug4 == "ciprofloxacine" or drug4 == "érythromycine" or \
                drug4 == "clarithromycine" or drug4 == "rifabutine" or \
                drug4 == "doxycycline" or drug4 == "troléandomycine" or \
                drug4 == "josamycine"):
                print("+ Interactions !!!")
                importationCarbaAtb(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "mae" or \
                drug4 == "mae"):
                importationCarbaMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "atd" or \
                drug3 == "antidépresseurs" or drug4 == "atd" or \
                drug4 == "antidépresseurs"):
                print("+ Interactions !!!")
                importationCarbaAntidep(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "antidiurétique" or \
                drug4 == "antidiurétique"):
                print("+ Interactions !!!")
                importationCarbaAntidiu(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "isoniazide" or \
                drug3 == "antituberculeux" or drug3 == "rifampicine" or \
                drug4 == "isoniazide" or drug4 == "antituberculeux" or \
                drug4 == "rifampicine"):
                print("+ Interactions !!!")
                importationCarbaAntitub(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "keppra" or \
                drug3 == "levetiracetam" or drug4 == "keppra" or \
                drug4 == "levetiracetam"):
                print("+ Interactions !!!")
                importationCarbaKeppra(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
                drug4 == "lithium"):
                print("+ Interactions !!!")
                importationCarbaLith(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "myorelaxant" or \
                drug4 == "myorelaxant"):
                print("+ Interactions !!!")
                importationCarbaMyo(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "oh" or \
                drug3 == "alcool" or drug4 == "oh" or \
                drug4 == "alcool"):
                print("+ Interactions !!!")
                importationCarbaOh(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "perphénazine" or \
                drug4 == "perphénazine"):
                print("+ Interactions !!!")
                importationCarbaPerphe(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "seroquel" or \
                drug3 == "sequase" or drug3 == "quétiapine" or \
                drug4 == "seroquel" or drug4 == "sequase" or \
                drug4 == "quétiapine"):
                print("+ Interactions !!!")
                importationCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "clopin" or \
                drug3 == "leponex" or drug3 == "clozapine" or \
                drug4 == "clopin" or drug4 == "leponex" or \
                drug4 == "clozapine"):
                print("+ Interactions !!!")
                importationCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "dépakine" or \
                drug3 == "valproate" or drug4 == "dépakine" or \
                drug4 == "valproate"):
                print("+ Interactions !!!")
                importationCarbaDepak(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "olanzapine" or \
                drug3 == "zyprexa" or drug4 == "olanzapine" or \
                drug4 == "zyprexa"):
                print("+ Interactions !!!")
                importationCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "haldol" or \
                drug3 == "halopéridol" or drug4 == "haldol" or \
                drug4 == "halopéridol"):
                print("+ Interactions !!!")
                importationCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "phénobarbital" or \
                drug3 == "aphénylbarbite" or drug4 == "phénobarbital" or \
                drug4 == "aphénylbarbite"):
                print("+ Interactions !!!")
                importationCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "primidone" or \
                drug3 == "mysoline" or drug4 == "primidone" or \
                drug4 == "mysoline"):
                print("+ Interactions !!!")
                importationCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "risperdal" or \
                drug3 == "risperdone" or drug4 == "risperdal" or \
                drug4 == "risperdone"):
                print("+ Interactions !!!")
                importationCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "abilify" or \
                drug3 == "aripiprazol" or drug4 == "abilify" or \
                drug4 == "aripiprazol"):
                print("+ Interactions !!!")
                importationCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "invega" or \
                drug3 == "palipéridone" or drug4 == "invega" or \
                drug4 == "palipéridone"):
                print("+ Interactions !!!")
                importationCarbaAntipsy(self)
            else:
                print("Loop to search drug3 and drug4...")
