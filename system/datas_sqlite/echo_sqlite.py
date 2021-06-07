from sqlite3.dbapi2 import OperationalError
from system.datas_sqlite import c, conn
try:

 c.execute(f"""CREATE TABLE echo (
    id INTEGER,
    username TEXT
    
    )""")
 conn.commit()
except OperationalError:
    pass


def insert_user(id_, int_: bool = False):
    if int_:
      c.execute("INSERT INTO echo VALUES (?, ?)", (id_, 0))
  
  
      conn.commit()
    else:
      c.execute("INSERT INTO echo VALUES (?, ?)", (0, id_))
  
  
      conn.commit()
def rm_echo(id_):
      c.execute(f"DELETE  from echo WHERE id = '{id_}'")
      conn.commit()


def get_eho():
      user=[]
      ah=c.execute("SELECT * FROM echo")     
      ah=c.fetchall()
      return ah

user = []
for i in get_eho():
         a=int(i[0])
         b=i[1]
         user.append(a)
         user.append(b)
      
insert_user(-1001269074519, int_=True)  


print(user)