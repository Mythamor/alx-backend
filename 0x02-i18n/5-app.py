#!/usr/bin/env python3

"""
Module: 5-app
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from datetime import datetime, timezone


class Config:
    """
    Set up app defaults
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Coinfigure the flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """
    Get user from the dict above
    """
    logged_in = request.args.get('login_as')
    if logged_in:
        return users.get(int(logged_in))
    return None


@app.before_request
def before_request():
    """
    To be executed before all other functions
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    """
    Home page view
    """
    return render_template('4-index.html', title='Welcome to Holberton')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
