import pickle
import numpy as np
import pandas as pd
import psycopg2 as db

CONNECTION = None
CACHE = None

def get_connection():
    global CONNECTION
    try:
        cursor = CONNECTION.cursor()
        cursor.execute('SELECT 1')
        cursor.fetchall()
    except:  # TODO: What exception?
        CONNECTION = db.connect(host="localhost", user="luiza_labs",
                                password="luiza_labs", dbname="luiza_labs")
    return CONNECTION

def get_cache():
    global CACHE
    if not CACHE:
        with open('data/cache.p', 'rb') as cache:
            CACHE = pickle.load(cache)
    return CACHE

def cook_sql_productsBought():
    return '''
        SELECT (uid, pid, at) 
        FROM interaction 
        WHERE (action = 'bought')
    '''

def cook_sql_AllLastViewedBeforeBuy(user, product, time_of_action):
    return '''
        SELECT MAX(at) FROM interaction 
        WHERE uid = %s AND pid = %s AND at <= to_timestamp(%s) AND action = 'viewed'
    '''% (user, product, time_of_action)




