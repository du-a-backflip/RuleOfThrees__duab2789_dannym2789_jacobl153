from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from customModules import APIModule, DBModule

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/register', methods = ['GET', 'POST'])
def register():
    return render_template("register.html")

@app.route('/settings', methods = ['GET', 'POST'])
def settings():
    return render_template("settings.html")

@app.route('/search/<query>', methods = ['GET', 'POST'])
def search(query):
    return render_template("")

@app.route('/view', methods = ['GET', 'POST'])
def view():
    return render_template("view.html")

if __name__ == "__main__":
    app.debug = True
    app.run()