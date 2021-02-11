import requests
import json

#constants
dot = 200
dash = 500
pause = 200
long_pause = 1000
headers = {'Content-Type': 'application/json'}

#env
api_url = ""    #change this
author = "" #change this

#Initialize message
message = {
    "author": author,
    "stream": []
}

def post(message, api_url=api_url, headers=headers):
    response = requests.post(api_url, data = message, headers=headers)
    print(response)
    if response.status_code == 200:
        print("Posted successfully")
    else:
        print("Failed")

morse = {
    ' ':'/',
    'a':'.-',
    'b': '-...',
    'c':'-.-.',
    'd':'-..',
    'e':'.',
    'f':'..-.',
    'g':'--',
    'h':'--.',
    'i':'..',
    'j':'.---',
    'k':'-.-',
    'l':'.-..',
    'm':'--',
    'n':'-.',
    'o':'---',
    'p':'.--.',
    'q':'--.-',
    'r':'.-.',
    's':'...',
    't':'-',
    'u':'..-',
    'v':'...-',
    'w':'.--',
    'x':'-..-',
    'y':'-.--',
    'z':'--..'
}

def code(string):
    message = ''
    push = []
    for char in string:
        message += morse[char]
    for char in message:
        if char == '.':
            x = [1, dot]
            y = [0,pause]
            push.append(x)
            push.append(y)
        elif char == '-':
            x = [1,dash] 
            y = [0,pause]
            push.append(x)
            push.append(y)
        else:
            push.append([0, long_pause])
    
    return push

user_input = input("Your message >")
message["stream"] = code(user_input.lower())
message = json.dumps(message)
print(message)
print("Would you like to post?")
if input("Yes? >").lower() == "yes":
    post(message)
input("Press Enter...")