#!/usr/bin/env python3

"""
This module provides a flask app instance
"""

from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ A Config class for configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def indexHtml() -> str:
    """ Creates html template """
    page_title = 'Welcome to Holberton'
    content = 'Hello world'
    return render_template('2-index.html',
                           page_title=page_title,
                           content=content)


@babel.localselector
def get_locale() -> str:
    """ Gets the language to be used """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
