#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interdrugs import *


def carbaFunc(self, drug3, drug4):
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
                importCarbaAnticoa(self)
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
                importCarbaAtb(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "mae" or \
                drug4 == "mae"):
                importCarbaMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "atd" or \
                drug3 == "antidépresseurs" or drug4 == "atd" or \
                drug4 == "antidépresseurs"):
                print("+ Interactions !!!")
                importCarbaAntidep(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "antidiurétique" or \
                drug4 == "antidiurétique"):
                print("+ Interactions !!!")
                importCarbaAntidiu(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "isoniazide" or \
                drug3 == "antituberculeux" or drug3 == "rifampicine" or \
                drug4 == "isoniazide" or drug4 == "antituberculeux" or \
                drug4 == "rifampicine"):
                print("+ Interactions !!!")
                importCarbaAntitub(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "keppra" or \
                drug3 == "levetiracetam" or drug4 == "keppra" or \
                drug4 == "levetiracetam"):
                print("+ Interactions !!!")
                importCarbaKeppra(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
                drug4 == "lithium"):
                print("+ Interactions !!!")
                importCarbaLith(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "myorelaxant" or \
                drug4 == "myorelaxant"):
                print("+ Interactions !!!")
                importCarbaMyo(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "oh" or \
                drug3 == "alcool" or drug4 == "oh" or \
                drug4 == "alcool"):
                print("+ Interactions !!!")
                importCarbaOh(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "perphénazine" or \
                drug4 == "perphénazine"):
                print("+ Interactions !!!")
                importCarbaPerphe(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "seroquel" or \
                drug3 == "sequase" or drug3 == "quétiapine" or \
                drug4 == "seroquel" or drug4 == "sequase" or \
                drug4 == "quétiapine"):
                print("+ Interactions !!!")
                importCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "clopin" or \
                drug3 == "leponex" or drug3 == "clozapine" or \
                drug4 == "clopin" or drug4 == "leponex" or \
                drug4 == "clozapine"):
                print("+ Interactions !!!")
                importCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "dépakine" or \
                drug3 == "valproate" or drug4 == "dépakine" or \
                drug4 == "valproate"):
                print("+ Interactions !!!")
                importCarbaDepak(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "olanzapine" or \
                drug3 == "zyprexa" or drug4 == "olanzapine" or \
                drug4 == "zyprexa"):
                print("+ Interactions !!!")
                importCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "haldol" or \
                drug3 == "halopéridol" or drug4 == "haldol" or \
                drug4 == "halopéridol"):
                print("+ Interactions !!!")
                importCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "phénobarbital" or \
                drug3 == "aphénylbarbite" or drug4 == "phénobarbital" or \
                drug4 == "aphénylbarbite"):
                print("+ Interactions !!!")
                importCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "primidone" or \
                drug3 == "mysoline" or drug4 == "primidone" or \
                drug4 == "mysoline"):
                print("+ Interactions !!!")
                importCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "risperdal" or \
                drug3 == "risperdone" or drug4 == "risperdal" or \
                drug4 == "risperdone"):
                print("+ Interactions !!!")
                importCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "abilify" or \
                drug3 == "aripiprazol" or drug4 == "abilify" or \
                drug4 == "aripiprazol"):
                print("+ Interactions !!!")
                importCarbaAntipsy(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "invega" or \
                drug3 == "palipéridone" or drug4 == "invega" or \
                drug4 == "palipéridone"):
                print("+ Interactions !!!")
                importCarbaAntipsy(self)
            else:
                print("Loop to search drug3 and drug4...")
