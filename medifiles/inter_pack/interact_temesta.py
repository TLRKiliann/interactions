#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles/interdrug (temesta + neuro)
def importTemestaNeuro(self):
    try:
        if os.path.getsize('./medifiles/interdrug/temesta_neuro.txt'):
            print("+ File 'temesta_neuro.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/temesta_neuro.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'temesta_neuro.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (temesta + mae)
def importTemestaMae(self):
    try:
        if os.path.getsize('./medifiles/interdrug/temesta_mae.txt'):
            print("+ File 'temesta_mae.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/temesta_mae.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'temesta_mae.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (temesta + myo)
def importTemestaMyo(self):
    try:
        if os.path.getsize('./medifiles/interdrug/temesta_myo.txt'):
            print("+ File 'temesta_myo.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/temesta_myo.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'temesta_myo.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (temesta + opio)
def importTemestaOpio(self):
    try:
        if os.path.getsize('./medifiles/interdrug/temesta_opio.txt'):
            print("+ File 'temesta_opio.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/temesta_opio.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'temesta_opio.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (temesta + uri)
def importTemestaUri(self):
    try:
        if os.path.getsize('./medifiles/interdrug/temesta_uri.txt'):
            print("+ File 'temesta_uri.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/temesta_uri.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'temesta_uri.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (temesta + café)
def importTemestaTheo(self):
    try:
        if os.path.getsize('./medifiles/interdrug/temesta_theo.txt'):
            print("+ File 'temesta_theo.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/temesta_theo.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'temesta_theo.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (temesta + scopolamine)
def importTemestaScopo(self):
    try:
        if os.path.getsize('./medifiles/interdrug/temesta_scopo.txt'):
            print("+ File 'temesta_scopo.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/temesta_scopo.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'temesta_scopo.txt' does not exist !", outnote)

# Display text in textbox from medifiles/interdrug (temesta + oh)
def importTemestaOh(self):
    try:
        if os.path.getsize('./medifiles/interdrug/temesta_oh.txt'):
            print("+ File 'temesta_oh.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/temesta_oh.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'temesta_oh.txt' does not exist !", outnote)
