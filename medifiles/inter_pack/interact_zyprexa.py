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