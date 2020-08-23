#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


def antipsyDrug2(self):
    """
    Per drug leponex
    """
    try:
        if os.path.getsize('./medifiles/perdrug/leponex.txt'):
            print("+ File 'leponex.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/leponex.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'leponex.txt' does not exist !", outnote)

def antipsyDrug3(self):
    """
    Per drug clopixol
    """
    try:
        if os.path.getsize('./medifiles/perdrug/clopixol.txt'):
            print("+ File 'clopixol.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/clopixol.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol.txt' does not exist !", outnote)

def antipsyDrug4(self):
    """
    Per drug entumine
    """
    try:
        if os.path.getsize('./medifiles/perdrug/entumine.txt'):
            print("+ File 'entumine.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/entumine.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'entumine.txt' does not exist !", outnote)

def antipsyDrug5(self):
    """
    Per drug fluanxol
    """
    try:
        if os.path.getsize('./medifiles/perdrug/fluanxol.txt'):
            print("+ File 'fluanxol.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/fluanxol.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'fluanxol.txt' does not exist !", outnote)

def antipsyDrug6(self):
    """
    Per drug haldol
    """
    try:
        if os.path.getsize('./medifiles/perdrug/haldol.txt'):
            print("+ File 'haldol.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/haldol.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'haldol.txt' does not exist !", outnote)

def antipsyDrug7(self):
    """
    Per drug nozinan
    """
    try:
        if os.path.getsize('./medifiles/perdrug/nozinan.txt'):
            print("+ File 'nozinan.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/nozinan.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'nozinan.txt' does not exist !", outnote)

def antipsyDrug8(self):
    """
    Per drug tiapridal
    """
    try:
        if os.path.getsize('./medifiles/perdrug/tiapridal.txt'):
            print("+ File 'tiapridal.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/tiapridal.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'tiapridal.txt' does not exist !", outnote)

def antipsyDrug9(self):
    """
    Per drug abilify
    """
    try:
        if os.path.getsize('./medifiles/perdrug/abilify.txt'):
            print("+ File 'abilify.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/abilify.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'abilify.txt' does not exist !", outnote)

def antipsyDrug10(self):
    """
    Per drug dogmatil
    """
    try:
        if os.path.getsize('./medifiles/perdrug/dogmatil.txt'):
            print("+ File 'dogmatil.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/dogmatil.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'dogmatil.txt' does not exist !", outnote)

def antipsyDrug11(self):
    """
    Per drug invega
    """
    try:
        if os.path.getsize('./medifiles/perdrug/invega.txt'):
            print("+ File 'invega.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/invega.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'invega.txt' does not exist !", outnote)

def antipsyDrug12(self):
    """
    Per drug olanzapine, zyprexa
    """
    try:
        if os.path.getsize('./medifiles/perdrug/olanzapine.txt'):
            print("+ File 'olanzapine.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/olanzapine.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'olanzapine.txt' does not exist !", outnote)

def antipsyDrug14(self):
    """
    Per drug risperdal
    """
    try:
        if os.path.getsize('./medifiles/perdrug/risperdal.txt'):
            print("+ File 'risperdal.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/risperdal.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'risperdal.txt' does not exist !", outnote)

def antipsyDrug16(self):
    """
    Per drug seroquel
    """
    try:
        if os.path.getsize('./medifiles/perdrug/seroquel.txt'):
            print("+ File 'seroquel.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/seroquel.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'seroquel.txt' does not exist !", outnote)

def antipsyDrug17(self):
    """
    Per drug solian
    """
    try:
        if os.path.getsize('./medifiles/perdrug/solian.txt'):
            print("+ File 'solian.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/solian.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'solian.txt' does not exist !", outnote)
