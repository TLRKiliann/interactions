#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles/interdrug (abilify + carba)
def importAriAtd(self):
    try:
        if os.path.getsize('./medifiles/interdrug/ari_atd.txt'):
            print("+ File 'ari_atd.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/ari_atd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'ari_atd.txt' does not exist !", outnote)

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

# Display text in textbox from medifiles/interdrug (abilify + fluoxétine)
def importAriFluo(self):
    try:
        if os.path.getsize('./medifiles/interdrug/ari_fluo.txt'):
            print("+ File 'ari_fluo.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/ari_fluo.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'ari_fluo.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (abilify + kétoconazole)
def importAriKeto(self):
    try:
        if os.path.getsize('./medifiles/interdrug/ari_keto.txt'):
            print("+ File 'ari_keto.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/ari_keto.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'ari_keto.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (abilify + miscellanous)
def importAriMiscel(self):
    try:
        if os.path.getsize('./medifiles/interdrug/ari_miscel.txt'):
            print("+ File 'ari_miscel.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/ari_miscel.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'ari_miscel.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (abilify + OH)
def importAriOh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/ari_oh.txt'):
            print("+ File 'ari_oh.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/ari_oh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'ari_oh.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (abilify + paludéen)
def importAriPalu(self):
    try:
        if os.path.getsize('./medifiles/interdrug/ari_palu.txt'):
            print("+ File 'ari_palu.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/ari_palu.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'ari_palu.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (abilify + ISRS)
def importAriSrsirsn(self):
    try:
        if os.path.getsize('./medifiles/interdrug/ari_isrs.txt'):
            print("+ File 'ari_isrs.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/ari_isrs.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'ari_isrs.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (abilify + ahyperTA)
def importAriTa(self):
    try:
        if os.path.getsize('./medifiles/interdrug/ari_ahyperta.txt'):
            print("+ File 'ari_ahyperta.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/ari_ahyperta.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'ari_ahyperta.txt' does not exist !", outnote)

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
