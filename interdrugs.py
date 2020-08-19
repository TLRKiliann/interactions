#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles files (seroquel + carabamazepine)
def importationViolente(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_sero.txt'):
            print("+ File 'carba_sero.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_sero.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_sero.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (seroquel + depakine)
def importationSeroDepak(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_depak.txt'):
            print("+ File 'sero_depak.txt' exist (read)!")
            with open('./medifiles/interdrug/sero_depak.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_depak.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (seroquel + érythromicine)
def importationSeroEry(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_erythro.txt'):
            print("+ File 'sero_erythro.txt' exist (read)!")
            with open('./medifiles/interdrug/sero_erythro.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_erythro.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (seroquel + kétoconazol)
def importationSeroKeto(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_keto.txt'):
            print("+ File 'sero_keto.txt' exist (read)!")
            with open('./medifiles/interdrug/sero_keto.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_keto.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (seroquel + lithium)
def importationSeroLith(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_lith.txt'):
            print("+ File 'sero_lith.txt' exist (read)!")
            with open('./medifiles/interdrug/sero_lith.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_lith.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (seroquel + MeOH)
def importationSeroMeoh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_metha.txt'):
            print("+ File 'sero_metha.txt' exist (read)!")
            with open('./medifiles/interdrug/sero_metha.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_metha.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (seroquel + kétoconazol)
def importationSeroPheny(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_pheny.txt'):
            print("+ File 'sero_pheny.txt' exist (read)!")
            with open('./medifiles/interdrug/sero_pheny.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_pheny.txt' does not exist !", outnote)
    
# Display text in textbox from medifiles files (seroquel + kétoconazol)
def importationCarbaAnticoa(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_anticoa.txt'):
            print("+ File 'carba_anticoa.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_anticoa.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_anticoa.txt' does not exist !", outnote)

def importationCarbaAntipsy(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_neuro.txt'):
            print("+ File 'carba_neuro.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_neuro.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_neuro.txt' does not exist !", outnote)

def importationLepoCarba(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_carba.txt'):
            print("+ File 'lepo_carba.txt' exist (read)!")
            with open('./medifiles/interdrug/lepo_carba.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_carba.txt' does not exist !", outnote)

def importationLepoIpp(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_ipp.txt'):
            print("+ File 'lepo_ipp.txt' exist (read)!")
            with open('./medifiles/interdrug/lepo_ipp.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_ipp.txt' does not exist !", outnote)

def importationLepoAtd(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_atd.txt'):
            print("+ File 'lepo_atd.txt' exist (read)!")
            with open('./medifiles/interdrug/lepo_atd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_atd.txt' does not exist !", outnote)

def importationLepoAtb(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_atb.txt'):
            print("+ File 'lepo_atb.txt' exist (read)!")
            with open('./medifiles/interdrug/lepo_atb.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_atb.txt' does not exist !", outnote)

def importationLepoAntiHist(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_antihist.txt'):
            print("+ File 'lepo_antihist.txt' exist (read)!")
            with open('./medifiles/interdrug/lepo_antihist.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_antihist.txt' does not exist !", outnote)

def importationLepoMae(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_mae.txt'):
            print("+ File 'lepo_mae.txt' exist (read)!")
            with open('./medifiles/interdrug/lepo_mae.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_mae.txt' does not exist !", outnote)

def importationLepoNeuro(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_neuro.txt'):
            print("+ File 'lepo_neuro.txt' exist (read)!")
            with open('./medifiles/interdrug/lepo_neuro.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_neuro.txt' does not exist !", outnote)

def importationLepoBzd(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_bzd.txt'):
            print("+ File 'lepo_bzd.txt' exist (read)!")
            with open('./medifiles/interdrug/lepo_bzd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_bzd.txt' does not exist !", outnote)

def importationLepoOh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_oh.txt'):
            print("+ File 'lepo_oh.txt' exist (read)!")
            with open('./medifiles/interdrug/lepo_oh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_oh.txt' does not exist !", outnote)

def importationLepoMeOH(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_meoh.txt'):
            print("+ File 'lepo_meoh.txt' exist (read)!")
            with open('./medifiles/interdrug/lepo_meoh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_meoh.txt' does not exist !", outnote)

def importationLepoLith(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_lith.txt'):
            print("+ File 'lepo_lith.txt' exist (read)!")
            with open('./medifiles/interdrug/lepo_lith.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_lith.txt' does not exist !", outnote)

def importationLepoCoag(self):
    try:
        if os.path.getsize('./medifiles/interdrug/lepo_coagul.txt'):
            print("+ File 'lepo_coagul.txt' exist (read)!")
            with open('./medifiles/interdrug/lepo_coagul.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lepo_coagul.txt' does not exist !", outnote)
