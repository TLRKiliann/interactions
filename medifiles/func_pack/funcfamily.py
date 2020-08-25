#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
import os
import subprocess


def familyPsycho(self):
    """
    Choose one family of medication !
    """
    try:
        if os.path.getsize('./medifiles/family/antipsycho.txt'):
            print("+ File 'antipsycho.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/family/antipsycho.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'antipsycho.txt' does not exist !", outnote)

def familyMae(self):
    try:
        if os.path.getsize('./medifiles/family/mae.txt'):
            print("+ File 'mae.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/family/mae.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'mae.txt' does not exist !", outnote)

def familyAtd(self):
    try:
        if os.path.getsize('./medifiles/family/atd.txt'):
            print("+ File 'atd.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/family/atd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'atd.txt' does not exist !", outnote)

def familyAnxio(self):
    try:
        if os.path.getsize('./medifiles/family/anxio.txt'):
            print("+ File 'anxio.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/family/anxio.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'anxio.txt' does not exist !", outnote)

def familyThymo(self):
    try:
        if os.path.getsize('./medifiles/family/thymo.txt'):
            print("+ File 'thymo.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/family/thymo.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'thymo.txt' does not exist !", outnote)

def familySomni(self):
    try:
        if os.path.getsize('./medifiles/family/somni.txt'):
            print("+ File 'somni.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/family/somni.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'somni.txt' does not exist !", outnote)

def familyBzd(self):
    try:
        if os.path.getsize('./medifiles/family/bzd.txt'):
            print("+ File 'bzd.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/family/bzd.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'bzd.txt' does not exist !", outnote)

def familyIcho(self):
    try:
        if os.path.getsize('./medifiles/family/icho.txt'):
            print("+ File 'icho.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/family/icho.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'icho.txt' does not exist !", outnote)

def familyPark(self):
    try:
        if os.path.getsize('./medifiles/family/park.txt'):
            print("+ File 'park.txt' exist (read)!")
            self.textBox.delete('0.0', 'end')
            self.textBox.update()
            with open('./medifiles/family/park.txt', 'r') as textfile:
                lines = textfile.readlines()
                for li in lines:
                    self.textBox.insert(END, li)
    except FileNotFoundError as outnote:
        print("+ Sorry, file 'park.txt' does not exist !", outnote)
