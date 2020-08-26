#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles/interdrug (dépakine + mae)
def importDepakMae(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_mae.txt'):
            print("+ File 'depak_mae.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/depak_mae.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_mae.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (dépakine + neuro)
def importDepakNeuro(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_neuro.txt'):
            print("+ File 'depak_neuro.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/depak_neuro.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_neuro.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (dépakine + atd)
def importDepakAtd(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_atd.txt'):
            print("+ File 'depak_atd.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/depak_atd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_atd.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (dépakine + bzd)
def importDepakBzd(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_bzd.txt'):
            print("+ File 'depak_bzd.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/depak_bzd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_bzd.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (dépakine + OH)
def importDepakOh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_oh.txt'):
            print("+ File 'depak_oh.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/depak_oh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_oh.txt' does not exist !", outnote)

def importNoDrugs(self):
    self.textBox.insert(INSERT, "There is no information about this interaction !")
