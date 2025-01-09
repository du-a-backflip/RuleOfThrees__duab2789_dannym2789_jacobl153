from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from customModules import dBModule, APIModule

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods = ['GET', 'POST'])
def home():

@app.route('/login', methods = ['GET', 'POST'])
def login():

@app.route('/register', methods = ['GET', 'POST'])
def register():

@app.route('/settings', methods = ['GET', 'POST'])
def settings():

@app.route('/search/<query>')
