#!/usr/bin/env python3
"""
A basic Flask application with Babel configuration for localization.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    Configuration for Flask app with Babel integration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for supported languages based on the
    Accept-Language header from the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """
    Renders the home page with localized messages.
    """
    return render_template('0-index.html', title=_("home_title"), header=_("home_header"))


if __name__ == '__main__':
    app.run(debug=True)
