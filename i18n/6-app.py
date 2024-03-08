#!/usr/bin/env python3
"""
models parameters
"""
import flask
from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

# fictitious users
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# babel Configuration settings
class Config(object):
    """
    app configuration
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", methods=['GET'])
def index():
    """template """
    return render_template('5-index.html')


def get_user() -> dict:
    """Retrieve user based on login_as parameter"""
    # get the login_as parameter from the request
    user_id = request.args.get('login_as')
    try:
        # convert the login_as parameter to an int
        user_id = int(user_id)
        # if the user_id exists in the users dictionary
        if user_id in users:
            return users[user_id]
        # if the user_id does not exist in the users dictionary
    except (ValueError, TypeError):
        pass
    # if any of the above conditions are not met, return None
    return None


@app.before_request
def before_request():
    """ Définir l'utilisateur global s'il est connecté"""
    user = get_user()
    if user:
        g.user = user


@babel.localeselector
def get_locale():
    """ if a user is logged in, use the locale from the user settings"""
    if request.args.get('locale'):
        if request.args.get('locale') in Config.LANGUAGES:
            return request.args.get('locale')

    if hasattr(g, "user") and (
        g.user['locale'] and
        g.user['locale'] in Config.LANGUAGES
    ):
        return g.user['locale']

    return request.accept_languages.best_match(['en', 'fr'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
