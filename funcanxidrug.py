#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


def anxioDrug40(self):
    """
    Per drug atarax
    """
    try:
        if os.path.getsize('./medifiles/perdrug/atarax.txt'):
            print("+ File 'atarax.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/atarax.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'atarax.txt' does not exist !", outnote)

def anxioDrug42(self):
    """
    Per drug demetrin
    """
    try:
        if os.path.getsize('./medifiles/perdrug/demetrin.txt'):
            print("+ File 'demetrin.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/demetrin.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'demetrin.txt' does not exist !", outnote)

def anxioDrug43(self):
    """
    Per drug lexotanil
    """
    try:
        if os.path.getsize('./medifiles/perdrug/lexotanil.txt'):
            print("+ File 'lexotanil.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/lexotanil.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'lexotanil.txt' does not exist !", outnote)

def anxioDrug44(self):
    """
    Per drug rivotril
    """
    try:
        if os.path.getsize('./medifiles/perdrug/rivotril.txt'):
            print("+ File 'rivotril.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/rivotril.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'rivotril.txt' does not exist !", outnote)

def anxioDrug45(self):
    """
    Per drug rohypnol
    """
    try:
        if os.path.getsize('./medifiles/perdrug/rohypnol.txt'):
            print("+ File 'rohypnol.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/rohypnol.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'rohypnol.txt' does not exist !", outnote)

def anxioDrug46(self):
    """
    Per drug seresta
    """
    try:
        if os.path.getsize('./medifiles/perdrug/seresta.txt'):
            print("+ File 'seresta.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/seresta.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'seresta.txt' does not exist !", outnote)

def anxioDrug47(self):
    """
    Per drug temesta
    """
    try:
        if os.path.getsize('./medifiles/perdrug/temesta.txt'):
            print("+ File 'temesta.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/temesta.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'temesta.txt' does not exist !", outnote)

def anxioDrug48(self):
    """
    Per drug tranxilium
    """
    try:
        if os.path.getsize('./medifiles/perdrug/tranxilium.txt'):
            print("+ File 'tranxilium.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/perdrug/tranxilium.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'tranxilium.txt' does not exist !", outnote)