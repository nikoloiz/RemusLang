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



#Interpreter code here:
def interpret(query):
    uin = query.split(" ")
    if "out" in uin:
        if uin[1] == 'var':
            print(thisdict[uin[2]])
        elif uin[1] == 'result':
            print(thisdict[uin[2]])

        else:
            todisplay = ''
            for word in uin:
                if not word == 'out':
                    todisplay = todisplay + ' ' + word
            print(todisplay)


    elif "in" in uin:
        thisdict[uin[1]] = input(uin[2] + " ")

    elif "concat" in uin:
        thisdict[uin[1]] = uin[2] + ' ' + uin[3]


    elif "var" in uin:
        thisdict[uin[1]] = uin[2]

    elif "call" in uin:
         response = requests.get(uin[1])
         if response.status_code == 200:
            global call_result
            call_result = response.json()
            thisdict['call'] = call_result
         else:
             print(Fore.RED + 'ApiCallError: Returned response of ' +  str(response.status_code))
             sys.exit()

    elif 'json' in uin:
        try:
            print(call_result[uin[1]])
        except:
            print(Fore.RED + 'JsonParseError: Could not find ' + uin[1] + ' in JSON input.')

    else:
        print(Fore.RED + "CommandNotFoundError: Invalid Command: " + Fore.WHITE + uin[0])
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