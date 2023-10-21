#!/usr/bin/python3
"""Script that starts a Flask web application:

Requirements:
    - Web application must be listening on 0.0.0.0, port 5000
    - Routes:
      /: display “Hello HBNB!”.
      /hbnb: display “HBNB”.
      /c/<text>: display “C ” followed by the value of the text variable
     (replace underscore _ symbols with a space ).
    - You must use the option strict_slashes=False in your route definition

"""

# Imports the Flask module and creates a Flask web server from the Flask module
from flask import Flask

# Creates a new web application object, which we’ll use to configure routes.
app = Flask(__name__)


@app.route('/', strict_slashes=False)
""" -This Decorator tells Flask what URL should trigger our function.
-strict_slashes=False: option means the route is defined without trailing
slashes and Flask redirects all URLs with trailing slashes to this route.
"""


def show_hello_HBNB():
    """This function is triggered when the user visits the root URL"""
    return 'Hello HBNB!'
    """Returns the string ‘Hello HBNB!"""


@app.route('/hbnb', strict_slashes=False)
""" This decorator tells Flask to trigger the show_HBNB() function when
the ‘/hbnb’ URL is visited.
"""


def show_HBNB():
    """This function is triggered when the user visits the ‘/hbnb’ URL"""
    return 'HBNB'
    """returns the string ‘HBNB"""


@app.route('/c/<text>', strict_slashes=False)
"""
This decorator tells Flask to trigger the show_C(text) function when the
‘/c/<text>’ URL is visited. <text> is a variable part of the URL.
"""


def show_C(text):
    """This function is triggered when the user visits the ‘/c/<text>’ URL"""
    return 'C {}'.format(text.replace('_', ' '))
    """eturns a string that starts with 'C ’ and ends with the <text> from
    the URL, with underscores replaced by spaces.
    """


# -If this script is run directly (not imported), then it will run the app
#   on host 0.0.0.0 (which makes it publicly available) and on port 5000.
# -Set socket to run the app on.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
