#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles/interdrug (tranxi + neuro)
def importTranxiNeuro(self):
    try:
        if os.path.getsize('./medifiles/interdrug/tranxi_neuro.txt'):
            print("+ File 'tranxi_neuro.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/tranxi_neuro.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'tranxi_neuro.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (tranxi + bzd)
def importTranxiBzd(self):
    try:
        if os.path.getsize('./medifiles/interdrug/tranxi_bzd.txt'):
            print("+ File 'tranxi_bzd.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/tranxi_bzd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'tranxi_bzd.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (tranxi + hypno)
def importTranxiHypno(self):
    try:
        if os.path.getsize('./medifiles/interdrug/tranxi_hypno.txt'):
            print("+ File 'tranxi_hypno.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/tranxi_hypno.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'tranxi_hypno.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (tranxi + myo)
def importTranxiMyo(self):
    try:
        if os.path.getsize('./medifiles/interdrug/tranxi_myo.txt'):
            print("+ File 'tranxi_myo.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/tranxi_myo.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'tranxi_myo.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (tranxi + group)
def importTranxiGroup(self):
    try:
        if os.path.getsize('./medifiles/interdrug/tranxi_group.txt'):
            print("+ File 'tranxi_group.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/tranxi_group.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'tranxi_group.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (tranxi + ipp)
def importTranxiIpp(self):
    try:
        if os.path.getsize('./medifiles/interdrug/tranxi_ipp.txt'):
            print("+ File 'tranxi_ipp.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/tranxi_ipp.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'tranxi_ipp.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (tranxi + opio)
def importTranxiOpio(self):
    try:
        if os.path.getsize('./medifiles/interdrug/tranxi_opio.txt'):
            print("+ File 'tranxi_opio.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/tranxi_opio.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'tranxi_opio.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (tranxi + oh)
def importTranxiOh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/tranxi_oh.txt'):
            print("+ File 'tranxi_oh.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/tranxi_oh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'tranxi_oh.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (tranxi + cisa)
def importTranxiCisa(self):
    try:
        if os.path.getsize('./medifiles/interdrug/tranxi_cisa.txt'):
            print("+ File 'tranxi_cisa.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/tranxi_cisa.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'tranxi_cisa.txt' does not exist !", outnote)
