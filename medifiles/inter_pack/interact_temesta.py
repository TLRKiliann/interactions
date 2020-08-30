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