#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles/interdrug (leponex + carbamazépine)
def importTranxi...(self):
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