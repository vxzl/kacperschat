# deps/packs
import time as t
from pystyle import *
import os
import colorama
from colorama import Fore, Back, Style


login = """
 ██▓     ▒█████    ▄████  ██▓ ███▄    █ 
▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██▒ ██ ▀█   █ 
▒██░    ▒██░  ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒
▒██░    ▒██   ██░░▓█  ██▓░██░▓██▒  ▐▌██▒
░██████▒░ ████▓▒░░▒▓███▀▒░██░▒██░   ▓██░
░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒ 
░ ░ ▒  ░  ░ ▒ ▒░   ░   ░  ▒ ░░ ░░   ░ ▒░
  ░ ░   ░ ░ ░ ▒  ░ ░   ░  ▒ ░   ░   ░ ░ 
    ░  ░    ░ ░        ░  ░           ░                                 
"""[1:-1]

print(Fore.WHITE, Style.DIM + login)
print(Style.NORMAL)

t.sleep(1)

GGGC = input(Fore.WHITE + "Name: ")
print()
pt = """
 ██▓███   ▄▄▄        ██████   ██████  █     █░ ▒█████   ██▀███  ▓█████▄ 
▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌
▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌
▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌
▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓ 
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ 
░░         ░   ▒   ░  ░  ░  ░  ░  ░    ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░ 
               ░  ░      ░        ░      ░        ░ ░     ░        ░    
                                                                 ░                                      
"""[1:-1]
print()
t.sleep(1)
print(Fore.WHITE, Style.DIM + pt)
t.sleep(1)
print(Style.NORMAL)
password = input("If you forgot your name, enter a back-up password: ")

if GGGC == "Candice" or GGGC == "Isla" or GGGC == "Taylor" or GGGC == "Sean" or GGGC == "Marisol":
  print("Welcome to the Group Chat")
elif password == "Plum":
  print()
  print("Password Accepted.")
else:
  exit(print("Incorrect info."))


print()