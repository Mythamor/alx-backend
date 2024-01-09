#!/usr/bin/env python3

"""
Module: 5-app
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from datetime import datetime, timezone
import pytz.exceptions
from pytz import timezone
import locale


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
def before_request() -> None:
    """
    To be executed before all other functions
    """
    user = get_user()
    g.user = user

    time_now = pytz.utc.localize(datetime.utcnow())
	time = time_now.astimezone(timezone(get_timezone()))
	locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
	time_format = "%b %d, %Y %I:%M:%S %p"
	g.time = time.strftime(time_format)


@babel.localeselector
def get_locale():
    """
    Get locale from  user’s preferred local if it is supported
    priority:
            Locale from URL parameters
            Locale from user settings
            Locale from request header
            Default locale
    """
    # Locale from url params
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale

    # Locale from user settings
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    # Locale from request header
    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    # Default locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@babel.timezoneselector
def get_timezone():
    """
    Get timezone based on:
        URL parameters
    `   user settings
        Default UTC
    """
    # Find timezone parameter in URL parameters
    time_zone = request.args.get('timezone', None)
    if time_zone:
        try:
            return timezone(time_zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Find time zone from user settings
    if g.user:
        try:
            time_zone = g.user.get('timezone')
            return timezone(time_zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Default to UTC
    default_utc = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_utc



@app.route('/')
def index():
    """
    Home page view
    """
    return render_template('6-index.html', title='Welcome to Holberton')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
