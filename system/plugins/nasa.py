# Copyright (C) 2021 KeinShin@Github. All rights reserved

from pyrogram import filters
import urllib.request

YT = "AIzaSyDlKcqJc173XG80oB1RCh1ly79KKy1R_qo"
import logging
from system import COMMAND_HELP, app, HNDLR
import requests
from system.plugins import light
import random
import os
API = "iuPzOezHMHey7tbWDJnk1BmmbM772sygky5YfNZT"
@light.on(["nasa"])
async def nasa(client, message):
  txt = message.text
  if "earth" in txt:
    await message.edit("**Getting an osm earth photo wait a while! ( mainly 1 min )**")
 
    try:
      url = f'https://api.nasa.gov/EPIC/api/natural/all?api_key=iuPzOezHMHey7tbWDJnk1BmmbM772sygky5YfNZT'
      x = requests.get(url)
      s=x.json()
      zz = s[0]
      z = [i for i in s]
      a=[]
      for i in z:
         s=i['date']
         
         a.append(s)
      ac= random.SystemRandom()
  
      random_num = ac.choice(a)
      random_num=random_num.split(" ")[0]
      #   logging.info(random_num)
  
  
      url2= f"https://api.nasa.gov/EPIC/api/natural/date/{random_num}?api_key=iuPzOezHMHey7tbWDJnk1BmmbM772sygky5YfNZT"
      r2=requests.get(url2)
      # print(url2)
      #   logging.info(r2)
      s=r2.json()
      es=s[0]
      s=es['image']
      cap=es['caption']
      random_num=random_num.split("-")
      random_num="/".join(random_num)
      sed=requests.get(f"https://api.nasa.gov/EPIC/archive/natural/{random_num}/png/{s}.png?api_key=iuPzOezHMHey7tbWDJnk1BmmbM772sygky5YfNZT")
      file = open("sed.png", "wb")
      file.write(sed.content)
      file.close()
      await app.send_photo(message.chat.id, 'sed.png', caption=cap)
      os.remove('sed.png')
    except BaseException as e:
        await message.edit(f"ERROR - {e}")
  elif "astro " in txt:
      txt = txt.split()[2]
      print(txt)
      url= f"https://api.nasa.gov/neo/rest/v1/feed?start_date={txt}&api_key=iuPzOezHMHey7tbWDJnk1BmmbM772sygky5YfNZT"
      r=requests.get(url)
      r=r.json()
      r=r['links']

      r=r['near_earth_objects']
      sed=r['2015-09-11']
      sed=sed[0]
      sed=sed['name']  
  elif "astro" or "earth" not in txt:
        
     txtw = txt.split() # if 1 or more inputs
     if " " in txt:
       txt=" ".join(txtw[1:])

       await message.edit(f"**FINDING INFO ABOUT {txt} from nasa's database**")
    
       try:
        ur = f"https://images-api.nasa.gov/search?q={txt}"
        r=requests.get(ur)
       
        s = r.json()
       except Exception:
         await message.edit(f"**{txt} is not available**")
       sed=s['collection']
       cont=sed['items'][0]['links'][0]
       data = sed['items'][0]['data'][0]
    #  print(data)
       title=data["title"]
       created=data['date_created']
       try:
        des=data['description']
       except KeyError:
        des = ""

       img=cont['href']
       urllib.request.urlretrieve(img, "nasa.jpg")
       await app.send_photo(message.chat.id, "nasa.jpg", caption=f"""
**I found some thing about** `{txt}` **from nasa's database**

**TITLE** -  `{title}`

**CREATED AT**  - `{created}`

**INFO** - `{des}`
""")
       await message.delete()
       os.remove("nasa.jpg")


COMMAND_HELP.update({
  "nasa": f"`{HNDLR}nasa (earth or astro or anything u would like to search)`\n\n**Click on this detail button for more** @lightning_support_group",
  "nasa's help": f"`{HNDLR}nasa <text to search>`\
  \n**EX** - {HNDLR}nasa Orion\
  \n**USE**: __finds the given query details from nasa database__\
  \n\n{HNDLR}nasa earth\
  \n**USE***: __find a picture of earth captured by nasa__\
  \n\n`{HNDLR}nasa astro <any date> `\
  \n**USE**: __given any date bot will any astro departured earth from that date__\
  \n**EX** __{HNDLR}nasa astro 05-07-11:",
  "nasa's type": "Scientific"
})
