import sqlite3, os
from flask import Flask, request, render_template, redirect, url_for, flash, session
from customModules import APIModule
import random

app = Flask(__name__)
app.secret_key = os.urandom(32)

################### make Database #############################
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

def init_db():
    conn = sqlite3.connect('user_info.db') #initializes DB and creates users info table
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            favorites TEXT NOT NULL)
            ''')
    conn.commit()
    conn.close()

    conn = sqlite3.connect('api_info.db') #initializes DB for APIs
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS game_info(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            GameName TEXT NOT NULL,
            text TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()
    setup_word_API()

def get_rand_word():
    try:
        with sqlite3.connect('api_info.db') as conn:
            c = conn.cursor()
            rand = random.randint(1, 97)
            result = c.execute("SELECT text FROM game_info WHERE (id, GameName) = (?, ?)", (rand, "def_game")).fetchone()
            return(result)
    except sqlite3.IntegrityError:
        print('Database Error')

def addUser(username, password):
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    query = "INSERT INTO users (username, password, favorites) VALUES (?, ?, ?)"
    c.execute(query, (username, password, ""))
    db.commit()
    db.close()

def findUser(username, password):
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username, ))
    user = c.fetchone()
    print(user)
    if user is not None:
        print(user)
        return password == user[1]
    return False

def registerUser(username, password):
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username, ))
    user = c.fetchone()
    if user is None:
        addUser(username, password)
        return True
    return False

def check_guess():
    lives = int(request.form.get('lives'))
    guess = request.form.get('word')
    word = request.form.get("word_to_guess")
    syn_list = request.form.get('syn_list')
    syn_list = syn_list[:].replace("\'", "").split(", ")
    print(guess)
    print(word)
    print(syn_list)
    if guess == word:
        return lives + 1
    for syn in syn_list:
        if guess == syn:
            return lives
    return lives-1
