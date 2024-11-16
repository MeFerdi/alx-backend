#!/usr/bin/env python3
"""
A basic Flask application with Babel configuration for localization.
"""

from flask import Flask, render_template
from flask_babel import Babel


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


@app.route('/')
def home() -> str:
    """
    Renders the home page with a welcome message.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
