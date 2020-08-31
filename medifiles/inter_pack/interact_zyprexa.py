#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles/interdrug (zyprexa + neuro)
def importZyprexMae(self):
    try:
        if os.path.getsize('./medifiles/interdrug/zyprexa_mae.txt'):
            print("+ File 'zyprexa_mae.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/zyprexa_mae.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'zyprexa_mae.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (zyprexa + atd)
def importZyprexAtd(self):
    try:
        if os.path.getsize('./medifiles/interdrug/zyprexa_atd.txt'):
            print("+ File 'zyprexa_atd.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/zyprexa_atd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'zyprexa_atd.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (zyprexa + tabac)
def importZyprexTabac(self):
    try:
        if os.path.getsize('./medifiles/interdrug/zyprexa_tabac.txt'):
            print("+ File 'zyprexa_tabac.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/zyprexa_tabac.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'zyprexa_tabac.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (zyprexa + oh)
def importZyprexOh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/zyprexa_oh.txt'):
            print("+ File 'zyprexa_oh.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/zyprexa_oh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'zyprexa_oh.txt' does not exist !", outnote)
