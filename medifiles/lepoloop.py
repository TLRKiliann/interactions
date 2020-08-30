#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from medifiles.listfile import *
from medifiles.inter_pack.interact_leponex import *


def lepoFunc(self, drug3, drug4):
    for i in oneDrug:
        """
        drug1 VS drug2 (interactions with clopin)
        """
        if i == "leponex" or i == "clozapine" or i == "clopin":
            if (drug3 == i or drug4 == i) and (drug3 == "carbamazépine" or \
                drug3 == "tégrétol" or drug4 == "carbamazépine" or \
                drug4 == "tégrétol"):
                print("+ Interactions carbamazépine !!!")
                importLepoCarba(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "depakine" or \
                drug3 == "valproate" or drug4 == "depakine" or \
                drug4 == "valproate"):
                print("+ Interactions valproate !!!")
                importLepoValpro(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "phénytoïne" or \
                drug4 == "phénytoïne"):
                print("+ Interactions phénytoïne !!!")
                importLepoPheny(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "antituberculeux" or \
                drug3 == "antiTB" or drug4 == "antituberculeux" or \
                drug4 == "antiTB"):
                print("+ Interactions antiTB !!!")
                importLepoCarba(self)
            elif (drug3 == i or drug4 == i) and \
                (drug3 == "inhibiteurs de la pompe à protons" or \
                drug3 == "ipp" or \
                drug4 == "inhibiteurs de la pompe à protons" or \
                drug4 == "ipp"):
                print("+ Interactions ipp !!!")
                importLepoIpp(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "antidépresseurs" or \
                drug3 == "atd" or drug4 == "antidépresseurs" or \
                drug4 == "atd"):
                print("+ Interactions atd !!!")
                importLepoAtd(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "isrs" or \
                drug3 == "atd isrs" or drug3 == "floxyfral" or \
                drug3 == "fluvoxamine" or drug3 == "paroxétine" or \
                drug3 == "deroxat" or drug3 == "sertraline" or \
                drug3 == "citalopram" or drug4 == "floxyfral" or \
                drug4 == "fluvoxamine" or drug4 == "paroxétine" or \
                drug4 == "deroxat" or drug4 == "sertraline" or \
                drug4 == "citalopram" or drug4 == "isrs" or \
                drug4 == "atd isrs"):
                print("+ Interactions atd isrs !!!")
                importLepoIsrs(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "irsna" or \
                drug3 == "atd irsna" or drug3 == "venlafaxine" or \
                drug4 == "irsna" or drug4 == "atd irsna" or \
                drug4 == "venlafaxine"):
                print("+ Interactions atd irsna !!!")
                importLepoIrsna(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "imao" or \
                drug3 == "atd imao" or drug4 == "imao" or \
                drug4 == "atd imao"):
                print("+ Interactions atd imao !!!")
                importLepoImao(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "atb" or \
                drug3 == "antibiotiques" or drug4 == "atb" or \
                drug4 == "antibiotiques"):
                print("+ Interactions atb !!!")
                importLepoAtb(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "amyco" or \
                drug3 == "antimycotiques" or drug4 == "amyco" or \
                drug4 == "antimycotiques"):
                print("+ Interactions antimycotiques !!!")
                importLepoAmyco(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "cc" or \
                drug4 == "cc" or drug3 == "contraceptifs" or \
                drug4 == "contraceptifs"):
                print("+ Interactions contraceptifs !!!")
                importLepoContracept(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "antihistaminiques" or \
                drug3 == "antihist" or drug4 == "antihist" or \
                drug4 == "antihistaminiques"):
                print("+ Interactions antihist !!!")
                importLepoAntiHist(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "antiépileptiques" or \
                drug4 == "antiépileptiques" or drug3 == "mae" or \
                drug4 == "mae"):
                print("+ Interactions mae !!!")
                importLepoMae(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "apsy" or \
                drug4 == "apsy" or drug3 == "neuro" or drug4 == "neuro"):
                print("+ Interactions apsy !!!")
                importLepoNeuro(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "benzodiazépines" or \
                drug4 == "benzodiazépines" or drug3 == "bzd" or drug4 == "bzd"):
                print("+ Interactions bzd !!!")
                importLepoBzd(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "café" or \
                drug3 == "caféine" or drug4 == "café" or \
                drug4 == "caféine"):
                print("+ Interactions café !!!")
                importLepoCafe(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "tabac" or \
                drug4 == "tabac"):
                print("+ Interactions tabac !!!")
                importLepoTabac(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "alcool" or \
                drug4 == "alcool" or drug3 == "oh" or drug4 == "oh"):
                print("+ Interactions alcool !!!")
                importLepoOh(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "méthadone" or \
                drug4 == "méthadone" or drug3 == "meoh" or drug4 == "meoh"):
                print("+ Interactions meoh !!!")
                importLepoMeOH(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "lithium" or \
                drug3 == "lithiofor" or drug4 == "lithium" or \
                drug4 == "lithiofor"):
                print("+ Interactions lithium !!!")
                importLepoLith(self)
            elif (drug3 == i or drug4 == i) and (drug3 == "anticoagulants" or \
                drug3 == "ac" or drug4 == "anticoagulants" or drug4 == "ac"):
                print("+ Interactions ac !!!")
                importLepoCoag(self)
            else:
                print("+ End of lepoloop ttt list !")
                