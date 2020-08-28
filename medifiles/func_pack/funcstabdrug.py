#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


def stabDrug1(self):
    """
    Per drug lithium
    """
    try:
        if os.path.getsize('./medifiles/perdrug/lithium.txt'):
            print("+ File 'lithium.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/lithium.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lithium.txt' does not exist !", outnote)
