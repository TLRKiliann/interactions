#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles/interdrug (leponex + carbamazépine)
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

# Display text in textbox from medifiles/interdrug (leponex + valproate)
def importLepoValpro(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_valpro.txt'):
            print("+ File 'lepo_valpro.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_valpro.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_valpro.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (leponex + phénytoïne)
def importLepoPheny(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_phenyto.txt'):
            print("+ File 'lepo_phenyto.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_phenyto.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_phenyto.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (carbamazépine + ipp)
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

# Display text in textbox from medifiles/interdrug (leponex + atd)
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

# Display text in textbox from medifiles/interdrug (leponex + atd isrs)
def importLepoIsrs(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_isrs.txt'):
            print("+ File 'lepo_isrs.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_isrs.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_isrs.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (leponex + atd irsna)
def importLepoIrsna(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_irsna.txt'):
            print("+ File 'lepo_irsna.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_irsna.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_irsna.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (leponex + atd imao)
def importLepoImao(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_imao.txt'):
            print("+ File 'lepo_imao.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_imao.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_imao.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (leponex + atb)
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

# Display text in textbox from medifiles/interdrug (leponex + atb)
def importLepoAmyco(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_amyco.txt'):
            print("+ File 'lepo_amyco.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_amyco.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_amyco.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (leponex + cc)
def importLepoContracept(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_cc.txt'):
            print("+ File 'lepo_cc.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_cc.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_cc.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (leponex + antihistaminique)
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

# Display text in textbox from medifiles/interdrug (leponex + mae)
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

# Display text in textbox from medifiles/interdrug (leponex + neuro)
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

# Display text in textbox from medifiles/interdrug (leponex + bzd)
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

# Display text in textbox from medifiles/interdrug (leponex + café)
def importLepoCafe(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_caf.txt'):
            print("+ File 'lepo_caf.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_caf.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_caf.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (leponex + tabac)
def importLepoTabac(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_tabac.txt'):
            print("+ File 'lepo_tabac.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/lepo_tabac.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_tabac.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (leponex + OH)
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

# Display text in textbox from medifiles/interdrug (leponex + méthadone)
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

# Display text in textbox from medifiles/interdrug (leponex + lithium)
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

# Display text in textbox from medifiles/interdrug (leponex + coagulant)
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
