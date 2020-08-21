#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from listfile import *
from family import *
from onedrug import *


def familyLoop(self, drug1):
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

def oneDrugLoop(self, drug2):
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
        elif i == "tiapridal" or i == "tiapride":
            if drug2 == i:
                oneDrug8(self)
        elif i == "abilify" or i == "aripiprazol":
            if drug2 == i:
                oneDrug9(self)
        elif i == "dogmatil" or i == "sulpride":
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
        elif i == "solian" or i == "amisulpride":
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
        elif i == "mysoline" or i == "primidone":
            if drug2 == i:
                oneDrug22(self)
        elif i == "phénobarbital" or i == "aphénylbarbite":
            if drug2 == i:
                oneDrug23(self)
        elif i == "phénytoïne":
            if drug2 == i:
                oneDrug24(self)
        elif i == "briviact" or i == "brivaracétam":
            if drug2 == i:
                oneDrug25(self)
        elif i == "fycompa" or i == "pérampanel":
            if drug2 == i:
                oneDrug26(self)
        elif i == "gabitril":
            if drug2 == i:
                oneDrug27(self)
        elif i == "inovelon":
            if drug2 == i:
                oneDrug28(self)
        elif i == "keppra" or i == "lévétiracétam":
            if drug2 == i:
                oneDrug29(self)
        elif i == "lamictal" or i == "lamotrigine":
            if drug2 == i:
                oneDrug30(self)
        elif i == "lyrica" or i == "prégabaline":
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
        elif i == "vimpat" or i == "lacosamide":
            if drug2 == i:
                oneDrug38(self)
        elif i == "zonegran" or i == "zonisamide":
            if drug2 == i:
                oneDrug39(self)
        elif i == "anafranil":
            if drug2 == i:
                oneDrug40(self)
        else:
            print("+ drug2 is not in the list")
