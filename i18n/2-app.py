#!/usr/bin/env python3
"""Basic Flask app, index page"""

# Import necessary modules
from flask import Flask, request, render_template
from flask_babel import Babel, _

# Create your Flask app and configure Babel
app = Flask(__name__)


class Config:
    """Config class for app configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


# Define the get_locale function
@babel.localeselector
def get_locale():
    """Get the best-matched language based on the user's preferences
    """
    # Determine the best-matched language based on the user's preferences
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    "home page"
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
