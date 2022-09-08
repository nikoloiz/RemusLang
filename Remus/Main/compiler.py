#Imports go here: 
import time
import sys
from typing import Dict
from guizero.TextBox import TextBox
import requests
import json
from guizero import App, Text
from colorama import init, Fore, Style, Back

init(autoreset=True)

#Variables go here:
call_result = "nill"
todisplay = 'nill'
thisdict = {}

#Functions go here:
def out(txt):
    f = open('script.sh', 'x')
    f.close()
    f = open('script.sh', 'a')
    f.write('echo ' + txt)


#Interpreter code here:
def interpret(query):
    uin = query.split(" ")
    if "out" in uin:
            todisplay = ''
            for word in uin:
                if not word == 'out':
                    todisplay = todisplay + ' ' + word
            out(todisplay)

    else:
        out("CommandNotFoundError: Invalid Command: " + uin[0])
        sys.exit()

try:
    interpretfile = sys.argv[1]
except:
    interpretfile = 'nill'
    while True:
        suin = input('>> ')
        interpret(suin)
        suin = ''

# Open file, split by lines & interpret it:
if not interpretfile == 'nill':
    f = open(interpretfile, 'r')
    lines = f.readlines()
    for line in lines:
        interpret(line)
    input('') #Stop cmd from auto-closing.