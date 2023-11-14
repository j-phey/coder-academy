from flask import Flask # Import the Class Flask, from the flask library
from datetime import datetime

# Flask turns the computer into a server.

app = Flask(__name__) # Create object called app, an instance of the Flask class

@app.route("/") # Decorator. Tells Flask how to respond to the request.
# The following code will trigger when the specified route is hit
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/goodbye/")
def goodbye_world():
    return "<p>Goodbye, World!</p>"

@app.route("/coder_time/")
def coder():
    return "<p>This web app was created in a class at Coder Academy.</p>"

# This app now has three routes:

# / - the root address
# /goodbye/
# /coder/

# Server Challenge
@app.route("/current_time/")
def current_time():
    current_time_formatted = datetime.now().strftime('%H:%M')
    return f'<p>{current_time_formatted}</p>'

if __name__ == '__main__':
  #Insert whichever port you would like
  app.run(debug=True, port=5001)