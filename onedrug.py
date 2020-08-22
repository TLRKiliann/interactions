#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Per drug ...
def oneDrug2(self):
    """
    Per drug leponex
    """
    try:
        if os.path.getsize('./medifiles/perdrug/leponex.txt'):
            print("+ File 'leponex.txt' exist (read)!")
            with open('./medifiles/perdrug/leponex.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'leponex.txt' does not exist !", outnote)

def oneDrug3(self):
    """
    Per drug clopixol
    """
    try:
        if os.path.getsize('./medifiles/perdrug/clopixol.txt'):
            print("+ File 'clopixol.txt' exist (read)!")
            with open('./medifiles/perdrug/clopixol.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol.txt' does not exist !", outnote)

def oneDrug4(self):
    """
    Per drug entumine
    """
    try:
        if os.path.getsize('./medifiles/perdrug/entumine.txt'):
            print("+ File 'entumine.txt' exist (read)!")
            with open('./medifiles/perdrug/entumine.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'entumine.txt' does not exist !", outnote)

def oneDrug5(self):
    """
    Per drug fluanxol
    """
    try:
        if os.path.getsize('./medifiles/perdrug/fluanxol.txt'):
            print("+ File 'fluanxol.txt' exist (read)!")
            with open('./medifiles/perdrug/fluanxol.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'fluanxol.txt' does not exist !", outnote)

def oneDrug6(self):
    """
    Per drug haldol
    """
    try:
        if os.path.getsize('./medifiles/perdrug/haldol.txt'):
            print("+ File 'haldol.txt' exist (read)!")
            with open('./medifiles/perdrug/haldol.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'haldol.txt' does not exist !", outnote)

def oneDrug7(self):
    """
    Per drug nozinan
    """
    try:
        if os.path.getsize('./medifiles/perdrug/nozinan.txt'):
            print("+ File 'nozinan.txt' exist (read)!")
            with open('./medifiles/perdrug/nozinan.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'nozinan.txt' does not exist !", outnote)

def oneDrug8(self):
    """
    Per drug tiapridal
    """
    try:
        if os.path.getsize('./medifiles/perdrug/tiapridal.txt'):
            print("+ File 'tiapridal.txt' exist (read)!")
            with open('./medifiles/perdrug/tiapridal.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'tiapridal.txt' does not exist !", outnote)

def oneDrug9(self):
    """
    Per drug abilify
    """
    try:
        if os.path.getsize('./medifiles/perdrug/abilify.txt'):
            print("+ File 'abilify.txt' exist (read)!")
            with open('./medifiles/perdrug/abilify.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'abilify.txt' does not exist !", outnote)

def oneDrug10(self):
    """
    Per drug dogmatil
    """
    try:
        if os.path.getsize('./medifiles/perdrug/dogmatil.txt'):
            print("+ File 'dogmatil.txt' exist (read)!")
            with open('./medifiles/perdrug/dogmatil.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'dogmatil.txt' does not exist !", outnote)

def oneDrug11(self):
    """
    Per drug invega
    """
    try:
        if os.path.getsize('./medifiles/perdrug/invega.txt'):
            print("+ File 'invega.txt' exist (read)!")
            with open('./medifiles/perdrug/invega.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'invega.txt' does not exist !", outnote)

def oneDrug12(self):
    """
    Per drug olanzapine, zyprexa
    """
    try:
        if os.path.getsize('./medifiles/perdrug/olanzapine.txt'):
            print("+ File 'olanzapine.txt' exist (read)!")
            with open('./medifiles/perdrug/olanzapine.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'olanzapine.txt' does not exist !", outnote)

def oneDrug14(self):
    """
    Per drug risperdal
    """
    try:
        if os.path.getsize('./medifiles/perdrug/risperdal.txt'):
            print("+ File 'risperdal.txt' exist (read)!")
            with open('./medifiles/perdrug/risperdal.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'risperdal.txt' does not exist !", outnote)

def oneDrug16(self):
    """
    Per drug seroquel
    """
    try:
        if os.path.getsize('./medifiles/perdrug/seroquel.txt'):
            print("+ File 'seroquel.txt' exist (read)!")
            with open('./medifiles/perdrug/seroquel.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'seroquel.txt' does not exist !", outnote)

def oneDrug17(self):
    """
    Per drug solian
    """
    try:
        if os.path.getsize('./medifiles/perdrug/solian.txt'):
            print("+ File 'solian.txt' exist (read)!")
            with open('./medifiles/perdrug/solian.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'solian.txt' does not exist !", outnote)

def oneDrug19(self):
    """
    Per drug carbamazépine
    """
    try:
        if os.path.getsize('./medifiles/perdrug/carbamazepine.txt'):
            print("+ File 'carbamazepine.txt' exist (read)!")
            with open('./medifiles/perdrug/carbamazepine.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carbamazepine.txt' does not exist !", outnote)

def oneDrug20(self):
    """
    Per drug depakine et valproate
    """
    try:
        if os.path.getsize('./medifiles/perdrug/depakine.txt'):
            print("+ File 'depakine.txt' exist (read)!")
            with open('./medifiles/perdrug/depakine.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depakine.txt' does not exist !", outnote)

def oneDrug21(self):
    """
    Per drug ethosuximide
    """
    try:
        if os.path.getsize('./medifiles/perdrug/ethosuximide.txt'):
            print("+ File 'ethosuximide.txt' exist (read)!")
            with open('./medifiles/perdrug/ethosuximide.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'ethosuximide.txt' does not exist !", outnote)

# Antiepileptiques !!!
def oneDrug22(self):
    """
    Per drug mysoline
    """
    try:
        if os.path.getsize('./medifiles/perdrug/mysoline.txt'):
            print("+ File 'mysoline.txt' exist (read)!")
            with open('./medifiles/perdrug/mysoline.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'mysoline.txt' does not exist !", outnote)

def oneDrug23(self):
    """
    Per drug phénobarbital and aphénylbarbite
    """
    try:
        if os.path.getsize('./medifiles/perdrug/phenobarbit.txt'):
            print("+ File 'phenobarbit.txt' exist (read)!")
            with open('./medifiles/perdrug/phenobarbit.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'phenobarbit.txt' does not exist !", outnote)

def oneDrug24(self):
    """
    Per drug phénytoine
    """
    try:
        if os.path.getsize('./medifiles/perdrug/phenytoine.txt'):
            print("+ File 'phenytoine.txt' exist (read)!")
            with open('./medifiles/perdrug/phenytoine.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'phenytoine.txt' does not exist !", outnote)

def oneDrug25(self):
    """
    Per drug briviact
    """
    try:
        if os.path.getsize('./medifiles/perdrug/briviact.txt'):
            print("+ File 'briviact.txt' exist (read)!")
            with open('./medifiles/perdrug/briviact.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'briviact.txt' does not exist !", outnote)

def oneDrug26(self):
    """
    Per drug fycompa
    """
    try:
        if os.path.getsize('./medifiles/perdrug/fycompa.txt'):
            print("+ File 'fycompa.txt' exist (read)!")
            with open('./medifiles/perdrug/fycompa.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'fycompa.txt' does not exist !", outnote)

def oneDrug28(self):
    """
    Per drug inovelon
    """
    try:
        if os.path.getsize('./medifiles/perdrug/inovelon.txt'):
            print("+ File 'inovelon.txt' exist (read)!")
            with open('./medifiles/perdrug/inovelon.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'inovelon.txt' does not exist !", outnote)

def oneDrug29(self):
    """
    Per drug keppra
    """
    try:
        if os.path.getsize('./medifiles/perdrug/keppra.txt'):
            print("+ File 'keppra.txt' exist (read)!")
            with open('./medifiles/perdrug/keppra.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'keppra.txt' does not exist !", outnote)

def oneDrug30(self):
    """
    Per drug lamictal
    """
    try:
        if os.path.getsize('./medifiles/perdrug/lamictal.txt'):
            print("+ File 'lamictal.txt' exist (read)!")
            with open('./medifiles/perdrug/lamictal.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lamictal.txt' does not exist !", outnote)

def oneDrug31(self):
    """
    Per drug lyrica
    """
    try:
        if os.path.getsize('./medifiles/perdrug/lyrica.txt'):
            print("+ File 'lyrica.txt' exist (read)!")
            with open('./medifiles/perdrug/lyrica.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lyrica.txt' does not exist !", outnote)

def oneDrug32(self):
    """
    Per drug neurontin
    """
    try:
        if os.path.getsize('./medifiles/perdrug/neurontin.txt'):
            print("+ File 'neurontin.txt' exist (read)!")
            with open('./medifiles/perdrug/neurontin.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'neurontin.txt' does not exist !", outnote)

def oneDrug33(self):
    """
    Per drug sabril
    """
    try:
        if os.path.getsize('./medifiles/perdrug/sabril.txt'):
            print("+ File 'sabril.txt' exist (read)!")
            with open('./medifiles/perdrug/sabril.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sabril.txt' does not exist !", outnote)

def oneDrug34(self):
    """
    Per drug taloxa
    """
    try:
        if os.path.getsize('./medifiles/perdrug/taloxa.txt'):
            print("+ File 'taloxa.txt' exist (read)!")
            with open('./medifiles/perdrug/taloxa.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'taloxa.txt' does not exist !", outnote)

def oneDrug35(self):
    """
    Per drug topamax and topiramate
    """
    try:
        if os.path.getsize('./medifiles/perdrug/topamax.txt'):
            print("+ File 'topamax.txt' exist (read)!")
            with open('./medifiles/perdrug/topamax.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'topamax.txt' does not exist !", outnote)

def oneDrug38(self):
    """
    Per drug vimpat
    """
    try:
        if os.path.getsize('./medifiles/perdrug/vimpat.txt'):
            print("+ File 'vimpat.txt' exist (read)!")
            with open('./medifiles/perdrug/vimpat.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'vimpat.txt' does not exist !", outnote)

def oneDrug39(self):
    """
    Per drug zonegran
    """
    try:
        if os.path.getsize('./medifiles/perdrug/zonegran.txt'):
            print("+ File 'zonegran.txt' exist (read)!")
            with open('./medifiles/perdrug/zonegran.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'zonegran.txt' does not exist !", outnote)

def oneDrug40(self):
    """
    Per drug atarax
    """
    try:
        if os.path.getsize('./medifiles/perdrug/atarax.txt'):
            print("+ File 'atarax.txt' exist (read)!")
            with open('./medifiles/perdrug/atarax.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'atarax.txt' does not exist !", outnote)
