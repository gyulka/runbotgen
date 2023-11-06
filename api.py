import sqlite3
from config import db
import json
from collections import defaultdict

import requests

from flask import Blueprint, request
import sqlite3
from config import db, tg_token
import requests

updates = defaultdict(list)


def db_connect():
    return sqlite3.connect(db)


def mytry(func):
    def ans():
        try:
            func()
        except Exception as error:
            return {'success': False, 'error': error.__str__()}

    return ans


api = Blueprint('botsapi', __name__)


@api.route('/')
def index():
    return 'cgorun bots database is wroking'


@api.route('/add_bot')
@mytry
def add_bot():
    data = json.loads(request.data.decode('utf-8'))
    con = db_connect()
    con.execute('insert into bots(token,name,ison) values(?,?,0)', (data['token'], data['name']))
    con.commit()

    return {'success': True}


@api.route('/get_token')
def get_token():
    try:
        con = db_connect()
        x = con.execute('select id,token from bots where ison=0').fetchall()
        if not x:
            return {'success': False, 'error': 'no tokens available'}
        x.sort(key=lambda x: x[::-1])
        con.execute('update bots set ison=1 where id=?', (x[-1][0],))
        con.commit()
        return {'success': True, 'token': x[-1][1], 'id': x[-1]}
    except Exception as error:
        return {'success': False, 'error': error.__str__()}


@api.route('/bot_off', methods=['POST'])
@mytry
def bot_off():
    data = json.loads(request.data.decode('utf-8'))
    con = db_connect()
    con.execute('update bots set ison=0 where id=?', (data['id']))
    con.commit()
    return {'success': True}


@api.route('/get_updates')
@mytry
def get_updates():
    data = json.loads(request.data.decode('utf-8'))
    ans = {'success': True, 'updates': updates[data['target']]}
    updates[data['target']].clear()
    return ans


@api.route('/setupdates')
@mytry
def set_updates():
    data = json.loads(request.data.decode('utf-8'))
    to = [data['target']]
    if data['target'] == 'all':
        to = updates.keys()
    for i in to:
        updates[i].append(data['update'])

    return {'success': True}


@api.route('/update_balance')
@mytry
def update_balance():
    data = json.loads(request.data.decode('utf-8'))
    con = db_connect()
    con.execute('update bots set summ=? where id=?', (data['balance'], data['id']))
    con.commit()
    return {'success': True}


if __name__ == '__main__':
    pass
