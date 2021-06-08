 # Copyright (C) 2021 KeinShin@Github. All rights reserved



from system.data_mongo import db
from collections import OrderedDict


en = db['env']


def set_env(env, value):
    env_ = {env: value}
    en.insert_one(env_)



def get_env(env):
    try:
      results = en.find({})
      red = []
      results = [i for i in results]
      # results =  results[0]
      for i in get_env(env):
          red.append(i[env])
      return list(OrderedDict.fromkeys(red))
    
    except IndexError or KeyError:
        return None



def del_env(env):
    results = db.find({})
    results = [i for i in results]
    results =  results[0]
    results = results[env]
    env = {env: results}
    en.delete_one(env)

# set_env("deaf", "no")
for i in get_env('deaf'):
    print(i['deaf'])