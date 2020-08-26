#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles/interdrug (seroquel + carabamazepine)
def importSeroCarba(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_sero.txt'):
            print("+ File 'carba_sero.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_sero.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_sero.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (seroquel + depakine)
def importSeroDepak(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_depak.txt'):
            print("+ File 'sero_depak.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/sero_depak.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_depak.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (seroquel + érythromicine)
def importSeroEry(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_erythro.txt'):
            print("+ File 'sero_erythro.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/sero_erythro.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_erythro.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (seroquel + kétoconazol)
def importSeroKeto(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_keto.txt'):
            print("+ File 'sero_keto.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/sero_keto.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_keto.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (seroquel + lithium)
def importSeroLith(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_lith.txt'):
            print("+ File 'sero_lith.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/sero_lith.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_lith.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (seroquel + MeOH)
def importSeroMeoh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_metha.txt'):
            print("+ File 'sero_metha.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/sero_metha.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_metha.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (seroquel + OH)
def importSeroOh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_oh.txt'):
            print("+ File 'sero_oh.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/sero_oh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_oh.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (seroquel + phénytoïne)
def importSeroPheny(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_pheny.txt'):
            print("+ File 'sero_pheny.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/sero_pheny.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_pheny.txt' does not exist !", outnote)

def importNoDrugs(self):
    self.textBox.insert(INSERT, "There is no information about this interaction !")
