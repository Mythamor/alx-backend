#!/usr/bin/env python3

"""
Module: 3-app
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _
from datetime import datetime, timezone


# Coinfigure the flask app
app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Set up app defaults
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    """
    Home page view
    """
    return render_template('3-index.html', title='Welcome to Holberton')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
