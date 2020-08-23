#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from listfile import *
from funcepidrug import *


def antiepiDrugLoop(self, drug2):
    for i in oneDrug:
        if i == "carbamazépine" or i == "tégrétol":
            if drug2 == i:
                antiepiDrug19(self)
        elif i == "dépakine" or i == "valproate":
            if drug2 == i:
                antiepiDrug20(self)
        elif i == "ethosuximide" or i == "pétinimid":
            if drug2 == i:
                antiepiDrug21(self)
        elif i == "mysoline" or i == "primidone":
            if drug2 == i:
                antiepiDrug22(self)
        elif i == "phénobarbital" or i == "aphénylbarbite":
            if drug2 == i:
                antiepiDrug23(self)
        elif i == "phénytoïne":
            if drug2 == i:
                antiepiDrug24(self)
        elif i == "briviact" or i == "brivaracétam":
            if drug2 == i:
                antiepiDrug25(self)
        elif i == "fycompa" or i == "pérampanel":
            if drug2 == i:
                antiepiDrug26(self)
        elif i == "inovelon" or i == "rufinamide":
            if drug2 == i:
                antiepiDrug28(self)
        elif i == "keppra" or i == "lévétiracétam":
            if drug2 == i:
                antiepiDrug29(self)
        elif i == "lamictal" or i == "lamotrigine":
            if drug2 == i:
                antiepiDrug30(self)
        elif i == "lyrica" or i == "prégabaline":
            if drug2 == i:
                antiepiDrug31(self)
        elif i == "neurontin" or i == "gabapentine":
            if drug2 == i:
                antiepiDrug32(self)
        elif i == "sabril" or i == "vigabatrine":
            if drug2 == i:
                antiepiDrug33(self)
        elif i == "taloxa" or i == "felbamate":
            if drug2 == i:
                antiepiDrug34(self)
        elif i == "topamax" or i == "topiramate":
            if drug2 == i:
                antiepiDrug35(self)
        elif i == "trileptal" or i == "oxcarbazépine":
            if drug2 == i:
                antiepiDrug36(self)
        elif i == "vimpat" or i == "lacosamide":
            if drug2 == i:
                antiepiDrug38(self)
        elif i == "zonegran" or i == "zonisamide":
            if drug2 == i:
                antiepiDrug39(self)
        else:
            print("This antiepi is not in the list")