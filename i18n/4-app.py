#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Configuration Babel """
    LANGUAGES = ["en", "fr"]
    Babel.default_locale = "en"
    Babel.default_timezone = "UTC"


app.config.from_object(Config)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """ Greeting

        Return:
            Initial template html
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ Locale language

        Return:
            Best match to the language
    """
    user_locale = request.args.get('locale')
    if user_locale in app.config['LANGUAGES']:
        return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
