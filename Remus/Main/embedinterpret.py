import time
import sys
from typing import Dict
import requests
import json


call_result = "nill"
mslot1 = ''
mslot2 = ''
thisdict = {

}

def interpret(query):
    uin = query.split(" ")
    if "out" in uin:
        if uin[1] == 'var':
            return thisdict[uin[2]]
        elif uin[1] == 'result':
            return thisdict[uin[2]]

        else:
            if len(uin) == 3:
                return uin[1] + " " + uin[2]
            elif len(uin) == 4:
                return uin[1] + " " + uin[2] + " " + uin[3]
            elif len(uin) > 4:
                return "Error: Command 'out' cannot accept values longer than 3 words."
            else:
                return uin[1]

    elif "in" in uin:
        thisdict[uin[1]] = input(uin[2] + " ")


    elif "var" in uin:
        thisdict[uin[1]] = uin[2]

    elif "call" in uin:
         response = requests.get(uin[1])
         if response.status_code == 200:
            global call_result
            call_result = response.json()
            thisdict['call'] = call_result
         else:
             return 'ApiCallError: Returned response of ' +  str(response.status_code)
             sys.exit()

    elif 'json' in uin:
        try:
            return call_result[uin[1]]
        except:
            return 'JsonParseError: Could not find ' + uin[1] + ' in JSON input.'


#Code to add backwards-compatibility with Remus Syntax Level 1
    elif "mem" in uin:
        if uin[1] == "1":
            mslot1 = uin[2] + " "
        elif uin[1] == "2":
            mslot2 = uin[2] + " "
        elif uin[1] == "nill":
          mslot1 = "nill"
          mslot2 = "nill"
        else:
            return "Invalid memory slot ID. Expected '1' or '2'."

    else:
        return "CommandNotFoundError: Invalid Command: " + uin[0]
        sys.exit()

print(interpret('out hello'))