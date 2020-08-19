#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from listfile import *
from family import *
import os
import subprocess


def luckyLoop(self, drug1):
    for i in familiyttt:
        if i == "antipsychotiques":
            if drug1 == i or drug1 == "antipsy":
                familyPsycho(self)
        elif i == "antiépileptiques":
            if drug1 == i or drug1 == "mae":
                familyMae(self)
        elif i == "antidépresseurs":
            if drug1 == i or drug1 == "atd":
                familyAtd()
        elif i == "anxiolytiques":
            if drug1 == i or drug1 == "anxio":
                familyAnxio()
        elif i == "thymorégulateurs":
            if drug1 == i or drug1 == "stabilisateurs":
                familyThymo()
        elif i == "somnifères":
            if drug1 == i or drug1 == "somni" or drug1 == "inducteurs de sommeil":
                familySomni()
        elif i == "benzodiazépines":
            if drug1 == i or drug1 == "bzd":
                familyBzd()
        elif i == "inhibiteurs de la cholinestérase":
            if drug1 == i or drug1 == "idlc":
                familyIcho()
        elif i == "antiparkinsoniens":
            if drug1 == i or drug1 == "ap":
                familyPark()
        else:
            print("+ This drug is not in familylist")


def luckyLoop2(drug2, drug3, drug4):
    # Don't forget kemadrin akineton
    for i in oneDrug:
        if i == "clopin" or i == "leponex" or i == "clozapine":
            if drug2 == i:
                oneDrug2()
        elif i == "clopixol":
            if drug2 == i:
                oneDrug3()
        elif i == "entumine":
            if drug2 == i:
                oneDrug4()
        elif i == "fluanxol":
            if drug2 == i:
                oneDrug5()
        elif i == "haldol":
            if drug2 == i:
                oneDrug6()
        elif i == "nozinan":
            if drug2 == i:
                oneDrug7()
        elif i == "tiapridal":
            if drug2 == i:
                oneDrug8()
        elif i == "abilify":
            if drug2 == i:
                oneDrug9()
        elif i == "dogmatil":
            if drug2 == i:
                oneDrug10()
        elif i == "invega" or i == "palipéridone":
            if drug2 == i:
                oneDrug11()
        elif i == "olanzapine" or i == "zyprexa":
            if drug2 == i:
                oneDrug12()
        elif i == "risperdal" or i == "risperdone":
            if drug2 == i:
                oneDrug14()
        elif i == "sequase" or i == "seroquel" or i == "quétiapine":
            if drug2 == i:
                sendToFunct16()
        elif i == "solian":
            if drug2 == i:
                oneDrug17()
        elif i == "carbamazépine" or i == "tégrétol":
            if drug2 == i:
                oneDrug19()
        elif i == "dépakine" or i == "valproate":
            if drug2 == i:
                oneDrug20()
        elif i == "ethosuximide" or i == "pétinimid":
            if drug2 == i:
                oneDrug21()
        elif i == "mysoline":
            if drug2 == i:
                oneDrug22()
        elif i == "phénobarbital" or i == "aphénylbarbite":
            if drug2 == i:
                oneDrug23()
        elif i == "phénytoïne":
            if drug2 == i:
                oneDrug24()
        elif i == "briviact":
            if drug2 == i:
                oneDrug25()
        elif i == "fycompa":
            if drug2 == i:
                oneDrug26()
        elif i == "gabitril":
            if drug2 == i:
                oneDrug27()
        elif i == "inovelon":
            if drug2 == i:
                oneDrug28()
        elif i == "keppra":
            if drug2 == i:
                oneDrug29()
        elif i == "lamictal":
            if drug2 == i:
                oneDrug30()
        elif i == "lyrica":
            if drug2 == i:
                oneDrug31()
        elif i == "neurontin":
            if drug2 == i:
                oneDrug32()
        elif i == "sabril":
            if drug2 == i:
                oneDrug33()
        elif i == "taloxa":
            if drug2 == i:
                oneDrug34()
        elif i == "topamax" or i == "topiramate":
            if drug2 == i:
                oneDrug35()
        elif i == "trileptal":
            if drug2 == i:
                oneDrug36()
        elif i == "vimpat":
            if drug2 == i:
                oneDrug38()
        elif i == "zonegran":
            if drug2 == i:
                oneDrug39()
        elif i == "anafranil":
            if drug2 == i:
                oneDrug40()
        else:
            print("+ This drug is not in the list")

    # drug1 VS drug2 (interactions with seroquel)
    for i in oneDrug:
        if i == "seroquel" or i == "sequase" or i == "quétiapine":
            if (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
                drug4 == "carbamazépine"):
                print("+ Interactions ultraviolente !!!")
                importationViolente()
            elif (drug3 == i or drug4 == i) and (drug3 == "dépakine" or \
                drug4 == "dépakine"):
                print("+ Interactions !!!")
                importationSeroDepak()
            elif (drug3 == i or drug4 == i) and (drug3 == "érythromycine" or \
                drug4 == "érythromycine"):
                print("+ Interactions !!!")
                importationSeroEry()
            elif (drug3 == i or drug4 == i) and (drug3 == "kétoconazol" or \
                drug4 == "kétoconazol"):
                print("+ Interactions !!!")
                importationSeroKeto()
            elif (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
                drug4 == "lithium"):
                print("+ Interactions !!!")
                importationSeroLith()
            elif (drug3 == i or drug4 == i) and (drug3 == "méthadone" or \
                drug4 == "méthadone"):
                print("+ Interactions !!!")
                importationSeroMeoh()
            elif (drug3 == i or drug4 == i) and (drug3 == "alcool" or \
                drug4 == "alcool"):
                print("+ Interactions !!!")
                importationSeroOh()
            elif (drug3 == i or drug4 == i) and (drug3 == "phénytoïne" or \
                drug4 == "phénytoïne"):
                print("+ Interactions !!!")
                importationSeroPheny()
            elif (drug3 == i or drug4 == i) and (drug3 == "risperdal" or \
                drug4 == "risperdal"):
                print("+ Interactions !!!")
                importationSeroRisp()
            else:
                print("One of your choice doesn't exist in the list")

    # drug1 VS drug2 (interactions with carbamazépine)
    if i == "carbamazépine" or i == "tégrétol":
        if (drug3 == i or drug4 == i) and (drug3 == "sintrom" or \
            drug3 == "xarelto" or drug3 == "Rivaroxaban" or \
            drug3 == "héparine" or drug3 == "pradaxa" or \
            drug4 == "eliquis" or \
            drug4 == "sintrom" or drug4 == "xarelto" or \
            drug4 == "Rivaroxaban" or drug4 == "héparine" or \
            drug4 == "pradaxa" or drug4 == "eliquis"):
            print("+ Interactions !!!")
            importationCarbaAnticoa()
        elif (drug3 == i or drug4 == i) and (drug3 == "seroquel" or \
            drug3 == "sequase" or drug3 == "quétiapine" or \
            drug4 == "seroquel" or drug4 == "sequase" or \
            drug4 == "quétiapine"):
            print("+ Interactions !!!")
            importationCarbaAntipsy()
        elif (drug3 == i or drug4 == i) and (drug3 == "clopin" or \
            drug3 == "leponex" or drug3 == "clozapine" or \
            drug4 == "clopin" or drug4 == "leponex" or \
            drug4 == "clozapine"):
            print("+ Interactions !!!")
            importationCarbaAntipsy()
        elif (drug3 == i or drug4 == i) and (drug3 == "dépakine" or \
            drug3 == "valproate" or drug4 == "dépakine" or \
            drug4 == "valproate"):
            print("+ Interactions !!!")
            importationCarbaAntipsy()
        elif (drug3 == i or drug4 == i) and (drug3 == "olanzapine" or \
            drug3 == "zyprexa" or drug4 == "olanzapine" or \
            drug4 == "zyprexa"):
            print("+ Interactions !!!")
            importationCarbaAntipsy()
        elif (drug3 == i or drug4 == i) and (drug3 == "haldol" or \
            drug3 == "halopéridol" or drug4 == "haldol" or \
            drug4 == "halopéridol"):
            print("+ Interactions !!!")
            importationCarbaAntipsy()
        elif (drug3 == i or drug4 == i) and (drug3 == "phénobarbital" or \
            drug3 == "aphénylbarbite" or drug4 == "phénobarbital" or \
            drug4 == "aphénylbarbite"):
            print("+ Interactions !!!")
            importationCarbaAntipsy()
        elif (drug3 == i or drug4 == i) and (drug3 == "primidone" or \
            drug3 == "mysoline" or drug4 == "primidone" or \
            drug4 == "mysoline"):
            print("+ Interactions !!!")
            importationCarbaAntipsy()
        elif (drug3 == i or drug4 == i) and (drug3 == "risperdal" or \
            drug3 == "risperdone" or drug4 == "risperdal" or \
            drug4 == "risperdone"):
            print("+ Interactions !!!")
            importationCarbaAntipsy()
        elif (drug3 == i or drug4 == i) and (drug3 == "abilify" or \
            drug3 == "aripiprazol" or drug4 == "abilify" or \
            drug4 == "aripiprazol"):
            print("+ Interactions !!!")
            importationCarbaAntipsy()
        elif (drug3 == i or drug4 == i) and (drug3 == "invega" or \
            drug3 == "palipéridone" or drug4 == "invega" or \
            drug4 == "palipéridone"):
            print("+ Interactions !!!")
            importationCarbaAntipsy()
        else:
            print("One of your choice doesn't exist in the list (VS)")

    # drug1 VS drug2 (interactions with carbamazépine)
    if i == "léponex" or i == "clozapine" or i == "clopin":
        if (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
            drug3 == "tégrétol" or drug4 == "carbamazépine" or \
            drug4 == "tégrétol"):
            print("+ Interactions !!!")
            importationLepoCarba()

        elif (drug3 == i or drug4 == i) and \
            (drug3 == "inhibiteurs de la pompe à protons" or \
            drug3 == "IPP" or \
            drug4 == "inhibiteurs de la pompe à protons" or \
            drug4 == "IPP"):
            print("+ Interactions !!!")
            importationLepoIpp()

        elif (drug3 == i or drug4 == i) and (drug3 == "antidépresseurs" or \
            drug3 == "ATD" or drug4 == "antidépresseurs" or \
            drug4 == "ATD"):
            print("+ Interactions !!!")
            importationLepoAtd()

        elif (drug3 == i or drug4 == i) and (drug3 == "ATB" or \
            drug3 == "antibiotiques" or drug4 == "ATB" or \
            drug4 == "antibiotiques"):
            print("+ Interactions !!!")
            importationLepoAtb()

        elif (drug3 == i or drug4 == i) and (drug3 == "antihistaminiques" or \
            drug4 == "antihistaminiques"):
            print("+ Interactions !!!")
            importationLepoAntiHist()

        elif (drug3 == i or drug4 == i) and (drug3 == "antiépileptiques" or \
            drug4 == "antiépileptiques" or drug3 == "MAE" or drug4 == "MAE"):
            print("+ Interactions !!!")
            importationLepoMae()

        elif (drug3 == i or drug4 == i) and (drug3 == "neuroleptiques" or \
            drug4 == "neuroleptiques" or drug3 == "neuro" or drug4 == "neuro"):
            print("+ Interactions !!!")
            importationLepoNeuro()

        elif (drug3 == i or drug4 == i) and (drug3 == "benzodiazépines" or \
            drug4 == "benzodiazépines" or drug3 == "BZD" or drug4 == "BZD"):
            print("+ Interactions !!!")
            importationLepoBzd()

        elif (drug3 == i or drug4 == i) and (drug3 == "alcool" or \
            drug4 == "alcool" or drug3 == "OH" or drug4 == "OH"):
            print("+ Interactions !!!")
            importationLepoOh()

        elif (drug3 == i or drug4 == i) and (drug3 == "méthadone" or \
            drug4 == "méthadone" or drug3 == "MeOH" or drug4 == "MeOH"):
            print("+ Interactions !!!")
            importationLepoMeOH()

        elif (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
            drug4 == "lithium"):
            print("+ Interactions !!!")
            importationLepoLith()

        elif (drug3 == i or drug4 == i) and (drug3 == "anticoagulants" or \
            drug4 == "anticoagulants"):
            print("+ Interactions !!!")
            importationLepoCoag()

        else:
            print("One of your choice doesn't exist in the list (vs carba)")
