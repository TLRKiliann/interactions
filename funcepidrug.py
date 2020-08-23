#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


def antiepiDrug19(self):
    """
    Per drug carbamazépine
    """
    try:
        if os.path.getsize('./medifiles/perdrug/carbamazepine.txt'):
            print("+ File 'carbamazepine.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/carbamazepine.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carbamazepine.txt' does not exist !", outnote)

def antiepiDrug20(self):
    """
    Per drug depakine et valproate
    """
    try:
        if os.path.getsize('./medifiles/perdrug/depakine.txt'):
            print("+ File 'depakine.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/depakine.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depakine.txt' does not exist !", outnote)

def antiepiDrug21(self):
    """
    Per drug ethosuximide
    """
    try:
        if os.path.getsize('./medifiles/perdrug/ethosuximide.txt'):
            print("+ File 'ethosuximide.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/ethosuximide.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'ethosuximide.txt' does not exist !", outnote)

# Antiepileptiques !!!
def antiepiDrug22(self):
    """
    Per drug mysoline
    """
    try:
        if os.path.getsize('./medifiles/perdrug/mysoline.txt'):
            print("+ File 'mysoline.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/mysoline.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'mysoline.txt' does not exist !", outnote)

def antiepiDrug23(self):
    """
    Per drug phénobarbital and aphénylbarbite
    """
    try:
        if os.path.getsize('./medifiles/perdrug/phenobarbit.txt'):
            print("+ File 'phenobarbit.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/phenobarbit.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'phenobarbit.txt' does not exist !", outnote)

def antiepiDrug24(self):
    """
    Per drug phénytoine
    """
    try:
        if os.path.getsize('./medifiles/perdrug/phenytoine.txt'):
            print("+ File 'phenytoine.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/phenytoine.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'phenytoine.txt' does not exist !", outnote)

def antiepiDrug25(self):
    """
    Per drug briviact
    """
    try:
        if os.path.getsize('./medifiles/perdrug/briviact.txt'):
            print("+ File 'briviact.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/briviact.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'briviact.txt' does not exist !", outnote)

def antiepiDrug26(self):
    """
    Per drug fycompa
    """
    try:
        if os.path.getsize('./medifiles/perdrug/fycompa.txt'):
            print("+ File 'fycompa.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/fycompa.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'fycompa.txt' does not exist !", outnote)

def antiepiDrug28(self):
    """
    Per drug inovelon
    """
    try:
        if os.path.getsize('./medifiles/perdrug/inovelon.txt'):
            print("+ File 'inovelon.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/inovelon.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'inovelon.txt' does not exist !", outnote)

def antiepiDrug29(self):
    """
    Per drug keppra
    """
    try:
        if os.path.getsize('./medifiles/perdrug/keppra.txt'):
            print("+ File 'keppra.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/keppra.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'keppra.txt' does not exist !", outnote)

def antiepiDrug30(self):
    """
    Per drug lamictal
    """
    try:
        if os.path.getsize('./medifiles/perdrug/lamictal.txt'):
            print("+ File 'lamictal.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/lamictal.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lamictal.txt' does not exist !", outnote)

def antiepiDrug31(self):
    """
    Per drug lyrica
    """
    try:
        if os.path.getsize('./medifiles/perdrug/lyrica.txt'):
            print("+ File 'lyrica.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/lyrica.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lyrica.txt' does not exist !", outnote)

def antiepiDrug32(self):
    """
    Per drug neurontin
    """
    try:
        if os.path.getsize('./medifiles/perdrug/neurontin.txt'):
            print("+ File 'neurontin.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/neurontin.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'neurontin.txt' does not exist !", outnote)

def antiepiDrug33(self):
    """
    Per drug sabril
    """
    try:
        if os.path.getsize('./medifiles/perdrug/sabril.txt'):
            print("+ File 'sabril.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/sabril.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sabril.txt' does not exist !", outnote)

def antiepiDrug34(self):
    """
    Per drug taloxa
    """
    try:
        if os.path.getsize('./medifiles/perdrug/taloxa.txt'):
            print("+ File 'taloxa.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/taloxa.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'taloxa.txt' does not exist !", outnote)

def antiepiDrug35(self):
    """
    Per drug topamax and topiramate
    """
    try:
        if os.path.getsize('./medifiles/perdrug/topamax.txt'):
            print("+ File 'topamax.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/topamax.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'topamax.txt' does not exist !", outnote)

def antiepiDrug38(self):
    """
    Per drug vimpat
    """
    try:
        if os.path.getsize('./medifiles/perdrug/vimpat.txt'):
            print("+ File 'vimpat.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/vimpat.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'vimpat.txt' does not exist !", outnote)

def antiepiDrug39(self):
    """
    Per drug zonegran
    """
    try:
        if os.path.getsize('./medifiles/perdrug/zonegran.txt'):
            print("+ File 'zonegran.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/zonegran.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'zonegran.txt' does not exist !", outnote)
