#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles/interdrug (clopixol + neuro)
def importClopiNeuro(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_neuro.txt'):
            print("+ File 'clopixol_neuro.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_neuro.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_neuro.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + haldol)
def importClopiHaldo(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_haldol.txt'):
            print("+ File 'clopixol_haldol.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_haldol.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_haldol.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + seroquel)
def importClopiSero(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_seroquel.txt'):
            print("+ File 'clopixol_seroquel.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_seroquel.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_seroquel.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + lith)
def importClopiLith(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_lith.txt'):
            print("+ File 'clopixol_lith.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_lith.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_lith.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + bzd)
def importClopiBzd(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_bzd.txt'):
            print("+ File 'clopixol_bzd.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_bzd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_bzd.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + dopa)
def importClopiDopa(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_dopa.txt'):
            print("+ File 'clopixol_dopa.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_dopa.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_dopa.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + ahyperTA)
def importClopiHta(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_ahyperTA.txt'):
            print("+ File 'clopixol_ahyperTA.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_ahyperTA.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_ahyperTA.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + antiA)
def importClopiAntiArythm(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_antiA.txt'):
            print("+ File 'clopixol_antiA.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_antiA.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_antiA.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + antihist)
def importClopiAntiHist(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_antihist.txt'):
            print("+ File 'clopixol_antihist.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_antihist.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_antihist.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + atb)
def importClopiAtb(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_atb.txt'):
            print("+ File 'clopixol_atb.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_atb.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_atb.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + adrener)
def importClopiAdre(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_adrener.txt'):
            print("+ File 'clopixol_adrener.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_adrener.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_adrener.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + pimeto)
def importClopiPiMeto(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_pimeto.txt'):
            print("+ File 'clopixol_pimeto.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_pimeto.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_pimeto.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + barbi)
def importClopiBarbi(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_barbi.txt'):
            print("+ File 'clopixol_barbi.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_barbi.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_barbi.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + cisa)
def importClopiCisa(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_cisa.txt'):
            print("+ File 'clopixol_cisa.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_cisa.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_cisa.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + diu)
def importClopiDiu(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_diu.txt'):
            print("+ File 'clopixol_diu.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_diu.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_diu.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + opio)
def importClopiOpio(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_opio.txt'):
            print("+ File 'clopixol_opio.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_opio.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_opio.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (clopixol + oh)
def importClopiOh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/clopixol_oh.txt'):
            print("+ File 'clopixol_oh.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/clopixol_oh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'clopixol_oh.txt' does not exist !", outnote)
