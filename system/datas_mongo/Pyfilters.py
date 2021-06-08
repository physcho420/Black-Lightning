

 # Copyright (C) 2021 KeinShin@Github. All rights reserved
import pprint
import json

from system.data_mongo import client
db = client.test_database

async def insert(chat, filters ,cmd):
     document = {chat: {filters: cmd}}
     return await db.test_collection.insert_one(document)



async def get_():
   d=[]
   cursor = db.test_collection.find({})
   for document in await cursor.to_list(length=100):
       #  print(document)
       d.append(document)
   print(d)
   if "1234" in d[0].keys():
        print(d["1234"])
  
# async def do_find_one():
#   document = await db.test_collection.find_one({'1234': {'hi': 'hemlo'}})
#   return document
# def filters():
#     d ={}
#     ah=c.execute("SELECT * FROM filters")     
#     ah=c.fetchall()
#     for i in ah:
             

#             a = i[0]

#             try:

#              d.update({
#             a + f'_{i[1]}': f"{i[2]}"}
             
#              )
#             except TypeError:
#                 pass
#     return d

# def cmds():
#     d =[]
#     ah=c.execute("SELECT * FROM filters")     
#     ah=c.fetchall()
#     for i in ah:
#              d.append(
#              f'{i[1]}'
             
#              )
#     return d


# def delete(chat, filter_):
#       c.execute(f"DELETE  from filters WHERE chat = '{chat}' AND filters = '{filter_}'")
#       conn.commit()
    

# ah=c.execute("SELECT * FROM filters")     
# ah=c.fetchall()
from system import app


app.loop.run_until_complete(get_())