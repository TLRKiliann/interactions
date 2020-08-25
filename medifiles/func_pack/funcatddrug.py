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
    To reach file saroten.txt
    """
    try:
        if os.path.getsize('./medifiles/perdrug/saroten.txt'):
            print("+ File 'saroten.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/saroten.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'saroten.txt' does not exist !", outnote)

def atdDrug3(self):
    """
    To reach file surmontil.txt
    """
    try:
        if os.path.getsize('./medifiles/perdrug/surmontil.txt'):
            print("+ File 'surmontil.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/surmontil.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'surmontil.txt' does not exist !", outnote)

def atdDrug4(self):
    """
    To reach file trittico.txt
    """
    try:
        if os.path.getsize('./medifiles/perdrug/trittico.txt'):
            print("+ File 'trittico.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/trittico.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'trittico.txt' does not exist !", outnote)
