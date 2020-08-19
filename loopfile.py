#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from listfile import *
from family import *
from onedrug import *
from interdrugs import *


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
                familyAtd(self)
        elif i == "anxiolytiques":
            if drug1 == i or drug1 == "anxio":
                familyAnxio(self)
        elif i == "thymorégulateurs":
            if drug1 == i or drug1 == "stabilisateurs":
                familyThymo(self)
        elif i == "somnifères":
            if drug1 == i or drug1 == "somni" or drug1 == "inducteurs de sommeil":
                familySomni(self)
        elif i == "benzodiazépines":
            if drug1 == i or drug1 == "bzd":
                familyBzd(self)
        elif i == "inhibiteurs de la cholinestérase":
            if drug1 == i or drug1 == "idlc":
                familyIcho(self)
        elif i == "antiparkinsoniens":
            if drug1 == i or drug1 == "ap":
                familyPark(self)
        else:
            print("+ This drug is not in familylist")

def luckyLoop2(self, drug2):
    # Don't forget kemadrin akineton
    for i in oneDrug:
        if i == "clopin" or i == "leponex" or i == "clozapine":
            if drug2 == i:
                oneDrug2(self)
        elif i == "clopixol":
            if drug2 == i:
                oneDrug3(self)
        elif i == "entumine":
            if drug2 == i:
                oneDrug4(self)
        elif i == "fluanxol":
            if drug2 == i:
                oneDrug5(self)
        elif i == "haldol":
            if drug2 == i:
                oneDrug6(self)
        elif i == "nozinan":
            if drug2 == i:
                oneDrug7(self)
        elif i == "tiapridal":
            if drug2 == i:
                oneDrug8(self)
        elif i == "abilify":
            if drug2 == i:
                oneDrug9(self)
        elif i == "dogmatil":
            if drug2 == i:
                oneDrug10(self)
        elif i == "invega" or i == "palipéridone":
            if drug2 == i:
                oneDrug11(self)
        elif i == "olanzapine" or i == "zyprexa":
            if drug2 == i:
                oneDrug12(self)
        elif i == "risperdal" or i == "risperdone":
            if drug2 == i:
                oneDrug14(self)
        elif i == "sequase" or i == "seroquel" or i == "quétiapine":
            if drug2 == i:
                oneDrug16(self)
        elif i == "solian":
            if drug2 == i:
                oneDrug17(self)
        elif i == "carbamazépine" or i == "tégrétol":
            if drug2 == i:
                oneDrug19(self)
        elif i == "dépakine" or i == "valproate":
            if drug2 == i:
                oneDrug20(self)
        elif i == "ethosuximide" or i == "pétinimid":
            if drug2 == i:
                oneDrug21(self)
        elif i == "mysoline":
            if drug2 == i:
                oneDrug22(self)
        elif i == "phénobarbital" or i == "aphénylbarbite":
            if drug2 == i:
                oneDrug23(self)
        elif i == "phénytoïne":
            if drug2 == i:
                oneDrug24(self)
        elif i == "briviact":
            if drug2 == i:
                oneDrug25(self)
        elif i == "fycompa":
            if drug2 == i:
                oneDrug26(self)
        elif i == "gabitril":
            if drug2 == i:
                oneDrug27(self)
        elif i == "inovelon":
            if drug2 == i:
                oneDrug28(self)
        elif i == "keppra":
            if drug2 == i:
                oneDrug29(self)
        elif i == "lamictal":
            if drug2 == i:
                oneDrug30(self)
        elif i == "lyrica":
            if drug2 == i:
                oneDrug31(self)
        elif i == "neurontin":
            if drug2 == i:
                oneDrug32(self)
        elif i == "sabril":
            if drug2 == i:
                oneDrug33(self)
        elif i == "taloxa":
            if drug2 == i:
                oneDrug34(self)
        elif i == "topamax" or i == "topiramate":
            if drug2 == i:
                oneDrug35(self)
        elif i == "trileptal":
            if drug2 == i:
                oneDrug36(self)
        elif i == "vimpat":
            if drug2 == i:
                oneDrug38(self)
        elif i == "zonegran":
            if drug2 == i:
                oneDrug39(self)
        elif i == "anafranil":
            if drug2 == i:
                oneDrug40(self)
        else:
            print("+ drug2 is not in the list")

def luckyLoop3(self, drug3, drug4):
    # drug1 VS drug2 (interactions with seroquel)
    for i in oneDrug:
        if i == "seroquel" or i == "sequase" or i == "quétiapine":
            if (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
                drug4 == "carbamazépine" or drug3 == "tégrétol" or \
                drug4 == "tégrétol"):
                print("+ Interactions ultraviolente !!!")
                importationViolente(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "dépakine" or \
                drug4 == "dépakine"):
                print("+ Interactions !!!")
                importationSeroDepak(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "érythromycine" or \
                drug4 == "érythromycine"):
                print("+ Interactions !!!")
                importationSeroEry(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "kétoconazol" or \
                drug4 == "kétoconazol"):
                print("+ Interactions !!!")
                importationSeroKeto(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
                drug4 == "lithium"):
                print("+ Interactions !!!")
                importationSeroLith(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "méthadone" or \
                drug4 == "méthadone"):
                print("+ Interactions !!!")
                importationSeroMeoh(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "alcool" or \
                drug4 == "alcool"):
                print("+ Interactions !!!")
                importationSeroOh(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "phénytoïne" or \
                drug4 == "phénytoïne"):
                print("+ Interactions !!!")
                importationSeroPheny(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "risperdal" or \
                drug4 == "risperdal"):
                print("+ Interactions !!!")
                importationSeroRisp(self)
            else:
                print("Loop to search drug3 and drug4...")

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

        # drug1 VS drug2 (interactions with carbamazépine)
        if i == "léponex" or i == "clozapine" or i == "clopin":
            if (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
                drug3 == "tégrétol" or drug4 == "carbamazépine" or \
                drug4 == "tégrétol"):
                print("+ Interactions !!!")
                importationLepoCarba(self)

            elif (drug3 == i or drug4 == i) and \
                (drug3 == "inhibiteurs de la pompe à protons" or \
                drug3 == "IPP" or \
                drug4 == "inhibiteurs de la pompe à protons" or \
                drug4 == "IPP"):
                print("+ Interactions !!!")
                importationLepoIpp(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "antidépresseurs" or \
                drug3 == "ATD" or drug4 == "antidépresseurs" or \
                drug4 == "ATD"):
                print("+ Interactions !!!")
                importationLepoAtd(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "ATB" or \
                drug3 == "antibiotiques" or drug4 == "ATB" or \
                drug4 == "antibiotiques"):
                print("+ Interactions !!!")
                importationLepoAtb(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "antihistaminiques" or \
                drug4 == "antihistaminiques"):
                print("+ Interactions !!!")
                importationLepoAntiHist(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "antiépileptiques" or \
                drug4 == "antiépileptiques" or drug3 == "MAE" or drug4 == "MAE"):
                print("+ Interactions !!!")
                importationLepoMae(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "neuroleptiques" or \
                drug4 == "neuroleptiques" or drug3 == "neuro" or drug4 == "neuro"):
                print("+ Interactions !!!")
                importationLepoNeuro(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "benzodiazépines" or \
                drug4 == "benzodiazépines" or drug3 == "BZD" or drug4 == "BZD"):
                print("+ Interactions !!!")
                importationLepoBzd(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "alcool" or \
                drug4 == "alcool" or drug3 == "OH" or drug4 == "OH"):
                print("+ Interactions !!!")
                importationLepoOh(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "méthadone" or \
                drug4 == "méthadone" or drug3 == "MeOH" or drug4 == "MeOH"):
                print("+ Interactions !!!")
                importationLepoMeOH(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
                drug4 == "lithium"):
                print("+ Interactions !!!")
                importationLepoLith(self)

            elif (drug3 == i or drug4 == i) and (drug3 == "anticoagulants" or \
                drug4 == "anticoagulants"):
                print("+ Interactions !!!")
                importationLepoCoag(self)
            else:
                print("Loop to search drug3 and drug4...")
