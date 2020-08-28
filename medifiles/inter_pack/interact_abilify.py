#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles/interdrug (abilify + carba)
def importAriCarba(self):
    try:
        if os.path.getsize('./medifiles/interdrug/ari_carba.txt'):
            print("+ File 'ari_carba.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/ari_carba.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'ari_carba.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (abilify + valproate)
def importAriVal(self):
    try:
        if os.path.getsize('./medifiles/interdrug/ari_valith.txt'):
            print("+ File 'ari_valith.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/ari_valith.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'ari_valith.txt' does not exist !", outnote)