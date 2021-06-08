 # Copyright (C) 2021 KeinShin@Github. All rights reserved


from system.data_mongo import db, client
ap = db['approved']

def turns(id):

  results = db.find({"id": id})
  rm = {'id': id}

  results = [i for i in results]
  results =  results[0]
  lis = results["turns"]
  user = results['id']
  if str(user) in str(id):
      newvalues = { "$set": { "turns": lis + 1 } }
      db.update_one(rm, newvalues)

def insert_user(id):
    results = db.find({"id": id, "turns": 0})
    results = [i for i in results]
    try:

     results =  results[0]
    except IndexError:
     results = False
    if results:
        return None
    else:

        user={ "id": id, "turns": 0 }
        db.insert_one(user)

def approve_(id):
    user = {"approve" : id}
    ap.insert_one(user)

def disapprove(id):

    user = {"approve" : id}
    ap.delete_one(user)



def users(id):
    db=ap
    results = db.find({"approve": id})
    results = [i for i in results]
    try:
     results =  results[0]
     results = results['approve']
    
     return results
    except IndexError:
        return None






def his_turn(id):
  results = db.find({"id": id})
  results = [i for i in results]
  return results[0]['turns']


def all_user():
  uer = []
  results = ap.find({})
  results = [i for i in results]
  for i in results:
     uer.append(i['approve'])
  return uer



