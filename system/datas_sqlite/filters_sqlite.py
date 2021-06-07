 # Copyright (C) 2021 KeinShin@Github. All rights reserved


from sqlite3.dbapi2 import OperationalError
from system.datas_sqlite import c, conn
try:

 c.execute(f"""CREATE TABLE filters (
    chat TEXT, 
    filters TEXT,
    cmd  TEXT
    )""")
 conn.commit()
except OperationalError:
    pass

def insert(chat, filters ,cmd):
    conn.execute("INSERT INTO filters VALUES (?, ?, ?)", (chat, filters, cmd,))


    conn.commit()

def chats():
    d =[]
    ah=c.execute("SELECT * FROM filters")     
    ah=c.fetchall()
    for i in ah:
             d.append(
             f'{i[0]}')
    return d


def filters():
    d ={}
    ah=c.execute("SELECT * FROM filters")     
    ah=c.fetchall()
    for i in ah:
             

            a = i[0]

            try:

             d.update({
            a + f'_{i[1]}': f"{i[2]}"}
             
             )
            except TypeError:
                pass
    return d

def cmds():
    d =[]
    ah=c.execute("SELECT * FROM filters")     
    ah=c.fetchall()
    for i in ah:
             d.append(
             f'{i[1]}'
             
             )
    return d


def delete(chat, filter_):
      c.execute(f"DELETE  from filters WHERE chat = '{chat}' AND filters = '{filter_}'")
      conn.commit()
    

ah=c.execute("SELECT * FROM filters")     
ah=c.fetchall()
print(ah)