 # Copyright (C) 2021 KeinShin@Github. All rights reserved

from system.datas_sqlite import c, conn
from collections import *
from sqlite3 import OperationalError
try:
 c.execute(f"""CREATE TABLE gban (
  id TEXT 
  )""")
 conn.commit()
except OperationalError:
    pass
try:
 c.execute(f"""CREATE TABLE chets (
  chats TEXT
  )""")
 conn.commit()
except OperationalError:
    pass


def insert_chets(chats):
    c.execute("INSERT INTO chets VALUES (?)", ((chats,)))
    
    conn.commit()
def insert_id(ids,
):
    c.execute("INSERT INTO gban VALUES (?)", ((ids,)))
    
    conn.commit()


def chets():
    d =[]
    ah=c.execute("SELECT * FROM chets")     
    ah=c.fetchall()
    for i in ah:
             d.append(f'{i[0]}'
             
             )

    return list(OrderedDict.fromkeys(d))


def ids():
    d =[]
    ah=c.execute("SELECT * FROM gban")     
    ah=c.fetchall()
    for i in ah:
             d.append(f'{i[0]}'
             
             )

    return list(OrderedDict.fromkeys(d))

def del_ids(id_):
    c.execute(f"DELETE  from gban WHERE id = {id_}")
    conn.commit()
