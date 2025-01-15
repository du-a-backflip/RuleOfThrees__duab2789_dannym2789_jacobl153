from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from customModules import APIModule, DBModule

app = Flask(__name__)
app.secret_key = os.urandom(32)

DBModule.init_db()

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if DBModule.findUser(username, password):
            wrongInformation = False
            session['username'] = username
            return redirect(url_for('home'))
        else: 
            wrongInformation = True
    return render_template("login.html", wrongInfo = wrongInformation)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    userExist = False
    passwordMatch = True
    if 'username' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password1 = request.form['password1']
        if password == password1:
            if DBModule.registerUser(username, password):
                session ['username'] = username
                return redirect(url_for('home'))
            else: 
                userExist = True
        else: 
            passwordMatch = False
    return render_template("register.html", passwordMatch = passwordMatch, )

@app.route('/settings', methods = ['GET', 'POST'])
def settings():
    return render_template("settings.html")

@app.route('/search/<query>', methods = ['GET', 'POST'])
def search(query):
    return render_template("")

@app.route('/memory_match', methods = ['GET', 'POST'])
def memory_match():
    return render_template("mem_match.html")


@app.route('/typing_test', methods = ['GET', 'POST'])
def typing_test():
    return render_template("type_test.html")


@app.route('/word_guesser', methods = ['GET', 'POST'])
def word_guesser():
    points = 0
    text = DBModule.get_rand_word()[0]
    all_info = text.split("+")
    word = all_info[0]
    definition = all_info[1]
    syn_list = all_info[2].split(", ")
    if request.method == 'POST':
        points = DBModule.check_guess()
    return render_template("word_guess.html", word = word, definition = definition, syn_list = syn_list, points = points, gameName = "Word Guesser")
   

@app.route('/reaction', methods =['GET', 'POST'])
def reaction_speed():
    return render_template('reaction.html')    


if __name__ == "__main__":
    app.debug = True
    app.run()
