#!/usr/bin/env python3

"""
Module: 0-app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Home page view
    """
    return render_template('0-index.html', title='Welcome to Holberton')


if __name__ == "__main__":
    app.run(debug=True)
