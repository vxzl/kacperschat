# deps/packs
import time as t
from pystyle import *
import os
import colorama
from colorama import Fore, Back, Style
from subprocess import run

from sys import exit
from os import name, system

users = {}
status = ''

def clear():
    if name == 'nt':       #If Windows clear screen
        _ = system('cls')
    else:                  #If Linux etc. clear screen
        _ = system('clear')

def newUser():
    newUsername = input('Create new username: ')

    if newUsername in users:
        print('\nUsername already exists!\n')
        input('Press [Enter] to continue')
    else:
        newPassword = input('Create new password: ')
        users[newUsername] = newPassword #Append to dictionary(users)
        print('\nAccount created successfully!\n')
        input('Press [Enter] to continue')