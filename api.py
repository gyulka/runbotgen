import sqlite3
from config import db
import json

import requests

from flask import Blueprint, request
import sqlite3
from config import db, tg_token
import requests


def db_connect():
    return sqlite3.connect(db)


api = Blueprint('botsapi', __name__)


@api.route('/')
def index():
    return 'cgorun bots database is wroking'


@api.route('/get_token')
def get_token():
    con = db_connect()
    con.execute('')
