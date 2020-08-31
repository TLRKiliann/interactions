#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


# Display text in textbox from medifiles/interdrug (solian)
def importSolianBordel(self):
    try:
        if os.path.getsize('./medifiles/interdrug/solian_bordel.txt'):
            print("+ File 'solian_bordel.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/interdrug/solian_bordel.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'solian_bordel.txt' does not exist !", outnote)
