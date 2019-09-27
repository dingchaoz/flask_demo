# Flask is a lightweight WSGI web application framework. It is designed to
# make getting started quick and easy, with the ability to scale up to complex
# applications. It began as a simple wrapper around Werkzeug and Jinja and has
# become one of the most popular Python web application frameworks.

# What is WSGI?
# A traditional web server does not understand or have any way to run Python
# applications. Therefore the Python community came up with WSGI as a standard
# interface that modules and containers could implement. WSGI is now the
# accepted approach for running Python web applications.
# that a WSGI container is a separate running process that runs on a different
# port than your web server. Our web server is configured to pass requests to
# the WSGI container which runs your web application, then pass the response
# (in the form of HTML) back to the requester

# import flask library and its underlying objects
from flask import Flask

# initialize a new Flask object to a variable called app.
# every Flask application must have an application instance
# The web server will pass all the requests to this object under the WSGI protocol.
app = Flask(__name__)

# __name__ might be the most mentioned dunder variables that is
# given a string value __main__ when file is executed
print(__name__)


# Connect the root directory to a home function call
# the app.route decorator defines a route on url, it takes
# in a url and when the client requests for this url, the app calls
# the corresponding function home() in this case
@app.route('/')
def home():
    return "this is home page"


if __name__ == "__main__":
    app.run(debug=True, port=8080)
