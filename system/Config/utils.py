# Copyright (C) 2021 KeinShin@Github.


import os
from pathlib import Path
import platform
import string



import io


# with io.BytesIO(str.encode(OUTPUT)) as out_file
            # out_file.name = "cmd_list.text"
import logging
import os
from system.data_mongo.Pyfilters import get_
from system.data_mongo.env_db import get_env
import system
from system.Config import a






from googletrans import Translator, LANGUAGES
from googletrans.models import Translated
try:

 import heroku3
except Exception:
 os.system("pip3 install heroku3")
a = ""
async def owner_name():

    global a

    a += (await system.app.get_me() ).username
    return a
b = ""
async def bot_name():
    global b


    b += (await system.bot.get_me() ).username
    return b

# class Client(object):
    
#     async def owner(self):
#         self.usero = await system.app.get_me()
#         self.username = self.usero.username
#     # def user(self):
    #     return self.username


# from var import Var
# herokuclient = heroku3.from_key(Var.HEROKU_API_KEY)




class env(object):
    TG_API_ID = os.environ.get("TG_APP_ID", None)
    TG_API_HASH = os.environ.get("TG_API_HASH", None)
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)
    AFK_PM_MESSAGE = os.environ.get("AFK_PM_MESSAGE", None)
    TG_BOT_USER_NAME = os.environ.get("TG_BOT_USER_NAME", "@Kakrotooobot")
    PROTECTION = os.environ.get("PROTECTION", None)
    if PROTECTION is None:
        PROTECTION = "ON"
    if  not TG_BOT_USER_NAME:
        TG_BOT_USER_NAME = f'@{a}'
    APP_NAME = os.environ.get("APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    ALIVE_ASCII =  os.environ.get("ALIVE_ASCII", None)
    if not ALIVE_ASCII is None:
        pass
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    HNDLR = os.environ.get("HNDLR", ".")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    NO_ROWS_HELP_MENU = os.environ.get("NO_ROWS_HELP_MENU", None)
    if NO_ROWS_HELP_MENU is None:
        NO_ROWS_HELP_MENU = 3
    ENVIRONMENT = os.environ.get("ENVIRONMENT", False)

    # clien = Client()
    NO_COLUMNS_HELP_MENU = os.environ.get("NO_COLUMNS_HELP_MENU", None)
    if NO_COLUMNS_HELP_MENU is None:
        NO_COLUMNS_HELP_MENU = 7
  
    USER_NAME = os.environ.get("USER_NAME", None)
    OWNER_NAME = USER_NAME
    if OWNER_NAME is None:
  
        OWNER_NAME = b
    PM_SECURITY_MSG = os.environ.get("PM_SECURITY_MSG", None)
    SUDO_IDS = get_env('sudo')
    LOGS_CHAT_ID = os.environ.get("LOGS_CHAT_ID", None)
    COUNTRY = os.environ.get("COUNTRY", None)
    if COUNTRY is None:
        COUNTRY = "IN"
    if PM_SECURITY_MSG is None:
        PM_SECURITY_MSG = (
        f"**Hello User..\n**"
        f"**{str(OWNER_NAME)} is under  PM Security Your Message will be deleted until u're approved\nIf it is urgent contact him via {TG_BOT_USER_NAME}**"
    )
    else:
        WARNING = PM_SECURITY_MSG
    HELP_MENU_TXT = os.environ.get("HELP_MENY_TXT", None)
    if HELP_MENU_TXT is not None:
        HELP_MENU_TXT.split()[0]
    else:
        a = "**Black Lightning Help Menu for User**"
        a = HELP_MENU_TXT
    LANGUAGE = os.environ.get("LANGUAGE", None)
    if LANGUAGE is None:
        LANGUAGE = "english"
    



class var(object):
    try:

     import exconfig
    except ModuleNotFoundError:
        pass
    try:

      TG_API_ID = exconfig.TG_API_ID
      TG_API_HASH = exconfig.TG_API_HASH
      TG_BOT_TOKEN = exconfig.TG_BOT_TOKEN
    except AttributeError:
        logging.info("The credentials given in exconfig is in correct, correct and try again")
    AFK_PM_MESSAGE = get_env("afk_message")
    TG_BOT_USER_NAME = os.environ.get("TG_BOT_USER_NAME", "@Kakrotooobot")
    PROTECTION = get_env('protection')
    APP_NAME = None
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    MONGO_URL = get_env("mongo_db_url")
    HNDLR = get_env('hndlr')
    STRING_SESSION = get_env('string_session')
    NO_ROWS_HELP_MENU = get_env("NO_ROWS_HELP_MENU".lower())
    if NO_ROWS_HELP_MENU is None:
        NO_ROWS_HELP_MENU = 3

    # clien = Client()
    NO_COLUMNS_HELP_MENU = get_env("NO_COLUMNS_HELP_MENU".lower())
    if NO_COLUMNS_HELP_MENU is None:
        NO_COLUMNS_HELP_MENU = 7
  
    USER_NAME = get_env("user_name")
    OWNER_NAME = USER_NAME
    if OWNER_NAME is None:
  
        OWNER_NAME = b
    PM_SECURITY_MSG = get_env("PM_SECURITY_MSG")
    SUDO_IDS = get_env('sudo'.lower())
    LOGS_CHAT_ID = get_env("logs_chat_id")
    COUNTRY = get_env("COUNTRY".lower())
    if COUNTRY is None:
        COUNTRY = "IN"
    if PM_SECURITY_MSG is None:
        PM_SECURITY_MSG = (
        f"**Hello User..\n**"
        f"**{str(OWNER_NAME)} is under  PM Security Your Message will be deleted until u're approved\nIf it is urgent contact him via {TG_BOT_USER_NAME}**"
    )
    else:
        WARNING = PM_SECURITY_MSG
    HELP_MENU_TXT = get_env("help_menu_txt")
    if HELP_MENU_TXT is not None:
        HELP_MENU_TXT.split()[0]
    else:
        a = "**Black Lightning Help Menu for User**"
        a = HELP_MENU_TXT
    LANGUAGE = os.environ.get("LANGUAGE", None)
    if LANGUAGE is None:
        LANGUAGE = "english"

# Ported From https://github.com/jaskaranSM/HerokuManagerBot

if Path('exconfig.py').is_file():
    Variable = var

else:
    Variable = env
    
class HerokuHelper:
    def __init__(self, appName, apiKey):
        self.API_KEY = apiKey
        self.APP_NAME = appName
        self.herokuclient = self.getherokuclient()
        self.app = self.herokuclient.apps()[self.APP_NAME]

        self.herokuclient2 = heroku3.from_key(Variable.HEROKU_API_KEY)
    def getherokuclient(self):
        return heroku3.from_key(self.API_KEY)

    def getAccount(self):
        return self.herokuclient.account()

    def getLog(self):
        return self.app.get_log()

    def addEnvVar(self, key, value):
        self.app.config()[key] = value

    def restart(self):
        return self.app.restart()



class Owner:
    async def __init__(self):
         self.owner = system.app.me.id

async def errors_s():
    herokuHelper = HerokuHelper(Var.HEROKU_APP_NAME, Var.HEROKU_API_KEY)
    logfuck= herokuHelper.getLog()
    with open("logs.txt", "w") as log:
        log.write(logfuck)
    with open('logs.txt', 'r') as read:
        a =  read.read()
    log.close()
    read.close()
    return a

async def errors2():
    herokuHelper = HerokuHelper(Var.HEROKU_APP_NAME, Var.HEROKU_API_KEY)
    logfuck = herokuHelper.getLog()
    with open("logs.txt", "w") as log:
        log.write(logfuck)
    return 'logs.txt'

    
async def logs():
    herokuHelper = HerokuHelper(Var.HEROKU_APP_NAME, Var.HEROKU_API_KEY)
    logz = herokuHelper.getLog()
    with open("logs.txt", "r") as log:
        wah = log.readline()
    return  wah


def loader():
    pass



# Copyright (C) Midhun KM

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time




def language(text: str):
 

    # translator = Translator()
    # translation = translator.translate(text,  dest='en')

    return text

def hd_no(txt: str):
    contains_digit = False
    
    
    for character in txt:
    
        if character.isdigit():
    
            contains_digit = True
    
    return contains_digit



class user:
    async def user(self, id):
        self.user_=await system.app.get_users(int(id))
