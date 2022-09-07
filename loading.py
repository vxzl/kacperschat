# deps/packs
import time as t
from pystyle import *
import os
import colorama
from colorama import Fore, Back, Style
from subprocess import run
import style1

style1.style(50, 0, 8, 3, 5)


print(Fore.GREEN + "Validating:")
t.sleep(0.3)
print(Fore.GREEN + ".. 10%")
t.sleep(0.5)
print()
print(Fore.GREEN + ".... 20%")
t.sleep(0.5)
print()
print(Fore.GREEN + "...... 30%")
t.sleep(0.5)
print()
print(Fore.GREEN + "........ 40%")
t.sleep(0.5)
print()
print(Fore.GREEN + ".......... 50%")
t.sleep(2)
print()
print(Fore.GREEN + "............. 80%")
t.sleep(0.4)
print()
print(Fore.GREEN + ".............. 90%")
t.sleep(0.3)
print()
print(Fore.GREEN + "Loaded, welcome to the GGGC V1.1")



os.system("clear")
t.sleep(1)
exec(open("existing.py").read())