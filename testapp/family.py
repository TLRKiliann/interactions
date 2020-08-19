#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


def familyPsycho(self):
    """
    Choose per family of medication !
    """
    try:
        if os.path.getsize('../medifiles/family/antipsycho.txt'):
            print("+ File 'antipsycho.txt' exist (read)!")
            with open('../medifiles/family/antipsycho.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'antipsycho.txt' does not exist !", outnote)

def familyMae(self):
    try:
        if os.path.getsize('../medifiles/family/mae.txt'):
            print("+ File 'mae.txt' exist (read)!")
            with open('../medifiles/family/mae.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'mae.txt' does not exist !", outnote)  