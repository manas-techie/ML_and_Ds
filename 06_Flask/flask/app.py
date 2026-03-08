from flask import Flask

#it creates a Flask application instance. The Flask class is imported from the flask module, and an instance of it is created and assigned to the variable app. This instance will be used to define routes and handle requests in the Flask application.

#WSGI Application: Flask is a WSGI (Web Server Gateway Interface) application, which means it can be run on any WSGI-compliant web server. The app.run() method starts the development server provided by Flask, allowing you to test your application locally.
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to flask app!"

@app.route("/index")
def index():
    return "Welcome to the index page!"


# debug=True: This argument enables debug mode, which provides helpful error messages and automatically reloads the server when code changes are detected. This is useful during development but should be turned off in production for security reasons.
if __name__ == "__main__":
    app.run(debug=True)