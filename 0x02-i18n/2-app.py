#!/usr/bin/env python3

"""
Module: 1-app
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from datetime import datetime, timezone


app = Flask(__name__)


class Config:
    """
    Set up app defaults
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

    def get_locale():
        return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=Config.get_locale)


@app.route('/')
def index():
    """
    Home page view
    """
    return render_template('1-index.html', title='Welcome to Holberton')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
