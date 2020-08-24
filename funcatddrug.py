#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


def atdDrug1(self):
    """
    To reach file anafranil.txt
    """
    try:
        if os.path.getsize('./medifiles/perdrug/anafranil.txt'):
            print("+ File 'anafranil.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/anafranil.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'anafranil.txt' does not exist !", outnote)

def atdDrug2(self):
    """
    To reach file ludiomil.txt
    """
    try:
        if os.path.getsize('./medifiles/perdrug/ludiomil.txt'):
            print("+ File 'ludiomil.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/ludiomil.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'ludiomil.txt' does not exist !", outnote)