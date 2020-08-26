#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles files (leponex + carbamazépine)
def importLepoCarba(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_carba.txt'):
            print("+ File 'lepo_carba.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_carba.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_carba.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (carbamazépine + ipp)
def importLepoIpp(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_ipp.txt'):
            print("+ File 'lepo_ipp.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_ipp.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_ipp.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (leponex + atd)
def importLepoAtd(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_atd.txt'):
            print("+ File 'lepo_atd.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_atd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_atd.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (leponex + atb)
def importLepoAtb(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_atb.txt'):
            print("+ File 'lepo_atb.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_atb.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_atb.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (leponex + antihistaminique)
def importLepoAntiHist(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_antihist.txt'):
            print("+ File 'lepo_antihist.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_antihist.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_antihist.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (leponex + mae)
def importLepoMae(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_mae.txt'):
            print("+ File 'lepo_mae.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_mae.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_mae.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (leponex + neuro)
def importLepoNeuro(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_neuro.txt'):
            print("+ File 'lepo_neuro.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_neuro.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_neuro.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (leponex + bzd)
def importLepoBzd(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_bzd.txt'):
            print("+ File 'lepo_bzd.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_bzd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_bzd.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (leponex + OH)
def importLepoOh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_oh.txt'):
            print("+ File 'lepo_oh.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_oh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_oh.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (leponex + méthadone)
def importLepoMeOH(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_meoh.txt'):
            print("+ File 'lepo_meoh.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_meoh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_meoh.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (leponex + lithium)
def importLepoLith(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_lith.txt'):
            print("+ File 'lepo_lith.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_lith.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_lith.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (leponex + coagulant)
def importLepoCoag(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_coagul.txt'):
            print("+ File 'lepo_coagul.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_coagul.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_coagul.txt' does not exist !", outnote)

def importNoDrugs(self):
    self.textBox.insert(INSERT, "There is no information about this interaction !")

