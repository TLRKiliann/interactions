#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles/interdrug (dépakine + anticoag)
def importDepakAnticoag(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_anticoag.txt'):
            print("+ File 'depak_anticoag.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/depak_anticoag.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_anticoag.txt' does not exist !", outnote)

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

# Display text in textbox from medifiles/interdrug (dépakine + topamax + diamox)
def importDepakTopadia(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_topadia.txt'):
            print("+ File 'depak_topadia.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/depak_topadia.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_topadia.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (dépakine + lithium)
def importDepakLith(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_lith.txt'):
            print("+ File 'depak_lith.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/depak_lith.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_lith.txt' does not exist !", outnote)

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

# Display text in textbox from medifiles/interdrug (dépakine + ATB)
def importDepakAtb(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_atb.txt'):
            print("+ File 'depak_atb.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/depak_atb.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_atb.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (dépakine + contraceptifs)
def importDepakContracep(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_contracept.txt'):
            print("+ File 'depak_contracept.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/depak_contracept.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_contracept.txt' does not exist !", outnote)
