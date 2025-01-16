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

app = Flask(__name__)
app.secret_key = os.urandom(32)

DBModule.init_db()

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/login', methods = ['GET', 'POST'])
def login(): #note to self, add flash messages in this
    if 'username' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if DBModule.findUser(username, password):
            session['username'] = username
            flash(f"Successfully Logged in!", category="success")
            return redirect(url_for('home'))
        else:
            flash(f"No account found with this username and password", category="error")
    return render_template("login.html")

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password1 = request.form['password1']
        if password == password1:
            if DBModule.registerUser(username, password):
                session ['username'] = username
                flash(f"Welcome {username}! You've been registered!", category="success")
                return redirect(url_for('home'))
            else:
                flash(f"User already exists; Pick a different username", category="error")
        else:
            flash(f"Passwords don't match", category="error")
    return render_template("register.html")

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    session.pop('username', None)
    flash(f"Successfully logged out!", category="success")
    return redirect(url_for('home'))

@app.route('/settings', methods = ['GET', 'POST'])
def settings():
    if 'username' in session:
        return render_template('settings.html')
    return render_template("login.html")

@app.route('/search/<query>', methods = ['GET', 'POST'])
def search(query):
    return render_template("")

@app.route('/memory_match', methods = ['GET', 'POST'])
def memory_match():
    return render_template("mem_match.html")


@app.route('/typing_test', methods = ['GET', 'POST'])
def typing_test():
    quote = APIModule.getQuote()
    print(2)
    return render_template("type_test.html", quote = quote)


@app.route('/word_guesser', methods = ['GET', 'POST'])
def word_guesser():
    lives = 3
    turns = 0
    gif = ""
    text = DBModule.get_rand_word()[0]
    all_info = text.split("+")
    word = all_info[0]
    definition = all_info[1]
    syn_list = all_info[2].split(", ")
    if request.method == 'POST':
        lives = DBModule.check_guess()
        turns = int(request.form.get('turns')) + 1
        if lives == 0:
            flash(f"You ran out of lives! New game started...", category="error")
            turns = 0
            lives = 3
    return render_template("word_guess.html", word = word, definition = definition, syn_list = syn_list, lives = lives, turns= turns, gameName = "Word Guesser")


@app.route('/reaction', methods =['GET', 'POST'])
def reaction_speed():
    return render_template('reaction.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
