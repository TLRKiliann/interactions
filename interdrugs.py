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

# Display text in textbox from medifiles files (seroquel + OH)
def importationSeroOh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/sero_oh.txt'):
            print("+ File 'sero_oh.txt' exist (read)!")
            with open('./medifiles/interdrug/sero_oh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'sero_oh.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (seroquel + phénytoïne)
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
    
# Display text in textbox from medifiles files (seroquel + anticoagul)
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

# Display text in textbox from medifiles files (seroquel + atb)
def importationCarbaAtb(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_atb.txt'):
            print("+ File 'carba_atb.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_atb.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_atb.txt' does not exist !", outnote)

# Display text in textbox from medifiles files (seroquel + atd)
def importationCarbaAntidep(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_atdtc.txt'):
            print("+ File 'carba_atdtc.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_atdtc.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_atdtc.txt' does not exist !", outnote)

def importationCarbaDepak(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_depak.txt'):
            print("+ File 'carba_depak.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_depak.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_depak.txt' does not exist !", outnote)

def importationCarbaAntidiu(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_diuret.txt'):
            print("+ File 'carba_diuret.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_diuret.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_diuret.txt' does not exist !", outnote)

def importationCarbaAntitub(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_isonia.txt'):
            print("+ File 'carba_isonia.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_isonia.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_isonia.txt' does not exist !", outnote)

def importationCarbaMae(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_mae.txt'):
            print("+ File 'carba_mae.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_mae.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_mae.txt' does not exist !", outnote)

def importationCarbaKeppra(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_levetira.txt'):
            print("+ File 'carba_levetira.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_levetira.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_levetira.txt' does not exist !", outnote)

def importationCarbaLith(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_lith.txt'):
            print("+ File 'carba_lith.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_lith.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_lith.txt' does not exist !", outnote)

def importationCarbaMyo(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_myorelax.txt'):
            print("+ File 'carba_myorelax.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_myorelax.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_myorelax.txt' does not exist !", outnote)

def importationCarbaOh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_oh.txt'):
            print("+ File 'carba_oh.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_oh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_oh.txt' does not exist !", outnote)

def importationCarbaPerphe(self):
    try:
        if os.path.getsize('./medifiles/interdrug/carba_perphenazine.txt'):
            print("+ File 'carba_perphenazine.txt' exist (read)!")
            with open('./medifiles/interdrug/carba_perphenazine.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'carba_perphenazine.txt' does not exist !", outnote)

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

# with depakine
def importationDepakMae(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_mae.txt'):
            print("+ File 'depak_mae.txt' exist (read)!")
            with open('./medifiles/interdrug/depak_mae.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_mae.txt' does not exist !", outnote)

def importationDepakNeuro(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_neuro.txt'):
            print("+ File 'depak_neuro.txt' exist (read)!")
            with open('./medifiles/interdrug/depak_neuro.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_neuro.txt' does not exist !", outnote)

def importationDepakAtd(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_atd.txt'):
            print("+ File 'depak_atd.txt' exist (read)!")
            with open('./medifiles/interdrug/depak_atd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_atd.txt' does not exist !", outnote)

def importationDepakBzd(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_bzd.txt'):
            print("+ File 'depak_bzd.txt' exist (read)!")
            with open('./medifiles/interdrug/depak_bzd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_bzd.txt' does not exist !", outnote)

def importationDepakOh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/depak_oh.txt'):
            print("+ File 'depak_oh.txt' exist (read)!")
            with open('./medifiles/interdrug/depak_oh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'depak_oh.txt' does not exist !", outnote)
