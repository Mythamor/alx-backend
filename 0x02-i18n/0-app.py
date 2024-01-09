#!/usr/bin/env python3

"""
Module: 0-app
"""

from flask import Flask

app = Flask(__name__)

from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('0-index.html', title='Welcome to Holberton')
