from flask import Flask, render_template
import os

# Create a Flask application instance.
# The __name__ argument helps Flask locate the application's files.
app = Flask(__name__)

# Define a route for the root URL ("/").
# When a user accesses the root URL, the hello() function will be called.
@app.route("/")
def hello():
    """
    This function handles requests to the root URL ("/").
    It renders the 'index.html' template and passes the title "My Flask App" to the template.
    """
    #  Instead of returning a string, we now render an HTML template.
    #  The render_template function looks for files in a folder named "templates"
    #  in the same directory as the script.
    return render_template('index.html', title="My Flask App")

# Define another route for "/about".
@app.route("/about")
def about():
    """
    This function handles requests to the "/about" URL.
    It simply returns a string, which will be displayed in the user's browser.
    """
    return "About This Application"

#  Add a route that shows how to get environment variables
@app.route("/environment")
def environment():
    """
    This function demonstrates how to access environment variables.
    Environment variables are often used to store configuration settings,
    such as database URLs or API keys, without hardcoding them in the script.
    """
    #  Attempt to retrieve the value of the environment variable "MESSAGE".
    #  If the variable is not set, the default value "No message set" is used.
    message = os.environ.get("MESSAGE", "No message set")
    #  Return the message.
    return f"Message: {message}"

#  Add a dynamic route
@app.route("/user/<username>")
def user(username):
    """
    This route demonstrates how to create a dynamic route that accepts a variable.
    The <username> part of the URL is a placeholder for a value that will be
    passed to the view function as an argument.
    """
    return f"Hello, {username}!"

# This condition checks if the script is being run directly (not imported as a module).
# If it is, it starts the Flask development server.
if __name__ == "__main__":
    #  Run the Flask application.
    #  The debug=True option enables debugging mode, which provides helpful error
    #  messages and automatic reloading of the server when you make changes to the code.
    #  It should be set to False in a production environment.
    app.run(debug=True)
