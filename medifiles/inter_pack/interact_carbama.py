#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles files (carbamazépine + anticoagul)
def importCarbaAnticoa(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_anticoa.txt'):
            print("+ File 'carba_anticoa.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_anticoa.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_anticoa.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (carbamazépine + atb)
def importCarbaAtb(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_atb.txt'):
            print("+ File 'carba_atb.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_atb.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_atb.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (carbamazépine + atd)
def importCarbaAntidep(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_atdtc.txt'):
            print("+ File 'carba_atdtc.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_atdtc.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_atdtc.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (carbamazépine + dépakine)
def importCarbaDepak(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_depak.txt'):
            print("+ File 'carba_depak.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_depak.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_depak.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (carbamazépine + diurétiques)
def importCarbaAntidiu(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_diuret.txt'):
            print("+ File 'carba_diuret.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_diuret.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_diuret.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (carbamazépine + isonia)
def importCarbaAntitub(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_isonia.txt'):
            print("+ File 'carba_isonia.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_isonia.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_isonia.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (carbamazépine + mae)
def importCarbaMae(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_mae.txt'):
            print("+ File 'carba_mae.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_mae.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_mae.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (carbamazépine + keppra)
def importCarbaKeppra(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_levetira.txt'):
            print("+ File 'carba_levetira.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_levetira.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_levetira.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (carbamazépine + lithium)
def importCarbaLith(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_lith.txt'):
            print("+ File 'carba_lith.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_lith.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_lith.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (carbamazépine + myorelaxant)
def importCarbaMyo(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_myorelax.txt'):
            print("+ File 'carba_myorelax.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_myorelax.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_myorelax.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (carbamazépine + OH)
def importCarbaOh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_oh.txt'):
            print("+ File 'carba_oh.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_oh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_oh.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (carbamazépine + perphénazine)
def importCarbaPerphe(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_perphenazine.txt'):
            print("+ File 'carba_perphenazine.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_perphenazine.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_perphenazine.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (carbamazépine + neuro)
def importCarbaAntipsy(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_neuro.txt'):
            print("+ File 'carba_neuro.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/carba_neuro.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_neuro.txt' does not exist !", outnote)
