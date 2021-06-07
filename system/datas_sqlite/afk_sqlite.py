 # Copyright (C) 2021 KeinShin@Github. All rights reserved


from system.datas_sqlite import c, conn
from sqlite3 import OperationalError

def ex():
   try:
    c.execute(f"""CREATE TABLE afk (
     sed TEXT ,
     reason TEXT
     )""")
    conn.commit()
   except OperationalError:
       pass


def update_afk(boolian, reason):
    c.execute("INSERT INTO afk VALUES (?, ?)", ((boolian, reason)))
    conn.commit()

def del_afk():
    c.execute(f"""SELECT * FROM afk""")
    a=c.fetchall()
    if a[0][0] == 'True':

      c.execute(f"DELETE  from afk WHERE sed = sed AND reason = reason")
      conn.commit()
    else:
      return None


def get_afk():
    try:

     c.execute(f"""SELECT * FROM afk""")
    except OperationalError:
        ex()
        c.execute(f"""SELECT * FROM afk""")

    a=c.fetchall()
    try:

     if a[0][0] == "True":
         return True
    except IndexError:
        return None
    else:
        return None

def get_reason():
    c.execute(f"""SELECT * FROM afk""")
    a=c.fetchall()
    try:
     a=a[0][1]
    except IndexError:
     a = False
    if a :
        
        return a
    else:
        return None
def restart():
    c.execute("DROP TABLE afk")
    conn.commit()

c.execute(f"""SELECT * FROM afk""")
a=c.fetchall()
print(a)