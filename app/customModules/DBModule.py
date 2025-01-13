import sqlite3, os
from flask import Flask, request, render_template, redirect, url_for, flash, session
from customModules import APIModule
import random

app = Flask(__name__)
app.secret_key = os.urandom(32)

def init_db():
    """Initializes db"""
    if not os.path.exists('user_info.db'):
        conn = sqlite3.connect('user_info.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                favorites TEXT NOT NULL)''')
        conn.commit()
        conn.close()
    if not os.path.exists('api_info.db'):
        conn = sqlite3.connect('api_info.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS game_info(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                GameName TEXT NOT NULL,
                text TEXT NOT NULL
                )''')
        conn.commit()
        conn.close()
def setup_word_API():
    try:
        with sqlite3.connect('api_info.db') as conn:
            dictionary = APIModule.getDict()
            c=conn.cursor()
            for i in dictionary:
                gameName = "def_game"
                word_def_syns = i
                c.execute("INSERT INTO game_info(GameName, text) VALUES(?, ?)", (gameName, word_def_syns))
        conn.commit()
        conn.close
    except sqlite3.IntegrityError:
        flash('Database Error')

def get_rand_word():
    try:
        with sqlite3.connect('api_info.db') as conn:
            c = conn.cursor()
            rand = random.randint(1, 97)
            result = c.execute("SELECT * FROM game_info WHERE (id, GameName) = (?, ?)", (rand, "def_game")).fetchone()
            print(result, rand)
    except sqlite3.IntegrityError:
        print('Database Error')




    
