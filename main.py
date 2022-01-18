from json.decoder import JSONDecodeError
import time
import os
import multiprocessing
import random
import re
if os.name == 'posix':
  import simplejson as json
if os.name == 'nt':
  import json
try:
 import discum
except:
 os.system('py -m pip install random_user_agent')
 os.system('py -m pip install requests')
 os.system('py -m pip install discum')
 import discum
print("""\
░█████╗░░██╗░░░░░░░██╗░█████╗░  ░██████╗███████╗██╗░░░░░███████╗  ██████╗░░█████╗░████████╗
██╔══██╗░██║░░██╗░░██║██╔══██╗  ██╔════╝██╔════╝██║░░░░░██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░██║░╚██╗████╗██╔╝██║░░██║  ╚█████╗░█████╗░░██║░░░░░█████╗░░  ██████╦╝██║░░██║░░░██║░░░
██║░░██║░░████╔═████║░██║░░██║  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░
╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝  ██████╔╝███████╗███████╗██║░░░░░  ██████╦╝╚█████╔╝░░░██║░░░
░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░

**Version: 1.1.0**""")
time.sleep(2)
try:
  from tkinter import messagebox
  use_terminal=False
except:
  use_terminal=True
once=False
wbm=[12,16]
update = 0
class client:
  commands=[
    "owo hunt",
    "owo hunt",
    "owo battle"
    ]
  class color:
    purple = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    if os.name == "nt":
      purple = ''
      okblue = ''
      okcyan = ''
      okgreen = ''
      warning = ''
      fail = ''
      reset = ''
      bold = ''
      underline = ''
  with open('settings.json', "r") as file:
        data = json.load(file)
        token = data["token"]
        channel = data["channel"]
        proxy = data["proxy"]
  if data["token"] and data["channel"] == 'nothing':
   print(f"{color.fail} !!! [ERROR] !!! {color.reset} Please Enter Information To Continue")
   time.sleep(1)
   os.system('py newdata.py')
  print('=========================')
  print('|                       |')
  print('| [1] Load data         |')
  print('| [2] Create new data   |')
  print('| [3] Credit            |')
  print('=========================')
  time.sleep(1)
  time.sleep(1)
choice = int(input('Enter your choice: '))
if (choice == 1):
      pass
if (choice == 2):
      os.system('py newdata.py')
if (choice == 3):
      print(f'{client.color.okcyan} =========Credit=========={client.color.reset}')
      print(f'{client.color.purple} [Developer] {client.color.reset} Nizel')
      print(f'{client.color.purple} [Contributor] {client.color.reset} ahihiyou20')
      print(f'{client.color.okcyan} Most update made by ahihiyou20 for some reason idk {client.color.reset}')
      time.sleep(5)
      exit() 
else: 
 print(f'{client.color.fail} !! [ERROR] !! {client.color.reset} Wrong input!')
 time.sleep(2)
 exit()
def at():
  return f'\033[0;43m{time.strftime("%d %b %Y %H:%M:%S", time.localtime())}\033[0;21m'
bot = discum.Client(token=client.token,proxy= client.proxy, log=False)
@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental: #ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
@bot.gateway.command
def issuechecker(resp):
 if resp.event.ready:
   m = resp.parsed.auto()
   if m['author']['id'] == '408785106942164992':
    if 'captcha' in m['content']:
     print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED {msgonec[-6:]}')
     time.sleep(99999)
    if '(2/5)' in m['content']:
     print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED {msgonec[-6:]}')
     time.sleep(99999)
    if '(3/5)' in m['content']:
     print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED {msgonec[-6:]}')
     time.sleep(99999)
    if '(4/5)' in m['content']:
     print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED {msgonec[-6:]}')
     time.sleep(99999)
    if '(5/5)' in m['content']:
     print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED {msgonec[-6:]}')
     time.sleep(99999)
    if 'banned' in m['content']:
     print(f'{at()}{client.color.fail} !!! [BANNED] !!! {client.color.reset} your account have been banned from owo bot please open a issue on the Support Discord server')
     time.sleep(99999)
@bot.gateway.command
def runner(resp):
  if resp.event.ready:
        global wbm
        owodes=0
        command=random.choice(client.commands)
        command2=random.choice(client.commands)
        bot.typingAction(str(client.channel))
        bot.sendMessage(str(client.channel), command)
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command}")
        if not command2==command:
          bot.typingAction(str(client.channel))
          time.sleep(13)
          bot.sendMessage(str(client.channel), command2)
          print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command2}")
        time.sleep(random.randint(wbm[0],wbm[1]))
@bot.gateway.command
def owopray(resp):
 if resp.event.ready:
  bot.sendMessage(str(client.channel), "owo pray")
  print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo pray")
  time.sleep(13)
@bot.gateway.command
def gems(resp):
 if resp.event.ready:
  bot.typingAction(str(client.channel))
  time.sleep(5)
  bot.sendMessage(str(client.channel), "owo inv")
  print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo inv")
  time.sleep(7)
  msgs=bot.getMessages(str(client.channel), num=5)
  msgs=json.loads(msgs.text)
  inv = 0
  for msgone in msgs:
    if msgone['author']['id']==str(408785106942164992) and 'Inventory' in msgone['content']:
      inv=re.findall(r'`(.*?)`', msgone['content'])
  if not inv:
    exit()
  else:
    if '50' in inv:
      bot.sendMessage(str(client.channel), "owo lb all")
      print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo lb all")
      time.sleep(13)
      gems(resp)
      return
    for item in inv:
      try: 
        if int(item) > 100:
          inv.pop(inv.index(item)) #weapons
      except: #backgounds etc
        inv.pop(inv.index(item))
    tier = [[],[],[]]
    print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} Found {len(inv)} gems Inventory")
    for gem in inv:
      gem =int(gem)
      if 50 < gem < 60:
        tier[0].append(gem)
      elif 60 < gem < 70:
        tier[1].append(gem)
      elif 70 < gem < 80:
        tier[2].append(gem)
    for level in range(0,3):
      if not len(tier[level]) == 0:
        bot.sendMessage(str(client.channel), "owo use "+str(max(tier[level])))
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo use {str(max(tier[level]))}")
        time.sleep(7)
@bot.gateway.command
def loopie(resp):
 if resp.event.ready:
  x=True
  pray = 0
  gem=pray
  main=time.time()
  while x:
      runner(resp)
      if time.time() - pray > random.randint(300, 600):
        owopray(resp)
        pray=time.time()
      if time.time() - gem > random.randint(600, 1000):
        gems(resp)
        gem=time.time()
      if time.time() - main > random.randint(1000, 2000):
        time.sleep(random.randint(300, 600))
        main=time.time()

def defination1():
  global once
  if not once:
    once=True
    if __name__ == '__main__':
      lol=multiprocessing.Process(target=loopie)
      lol.run()
bot.gateway.run(auto_reconnect=True)
