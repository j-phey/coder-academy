from flask import Flask # Import the Class Flask, from the flask library
from datetime import datetime
import json

# Flask turns the computer into a server.

app = Flask(__name__) # Create object called app, an instance of the Flask class

@app.route("/")
def homepage():
    return """<p>Hi, welcome to my API! Here are the endpoints that are available:</p>
    <ul>
    <li>Current Time: /time</li>
    <li>Educator Info: /educators</li>
    </ul>"""

@app.route("/goodbye/")
def goodbye_world():
    return "<p>Goodbye, World!</p>"

@app.route("/coder_time/")
def coder():
    return "<p>This web app was created in a class at Coder Academy.</p>"

@app.route("/time")
def current_time():
    time_dict = {"current time": str(datetime.now().strftime('%H:%M'))}
    return json.dumps(time_dict)

@app.route("/educators")
def educators():
    educator_dict = {
        "educators": [
            {
                "Name": "Oliver",
                "Specialty": "Automated testing"
            },
            {
                "Name": "Jairo",
                "Specialty": "Discrete Mathematics"
            },
            {
                "Name": "Amir",
                "Specialty": "Web Development"
            },
            {
                "Name": "Iryna",
                "Specialty": "Database Engineering"
            },
            {
                "Name": "George",
                "Specialty": "Internet Security"
            },
        ]
    }
    return json.dumps(educator_dict)


# Server Challenge
@app.route("/current_time/")
def current_time2():
    current_time_formatted = datetime.now().strftime('%H:%M')
    return f'<p>{current_time_formatted}</p>'

if __name__ == '__main__':
  #Insert whichever port you would like
  app.run(debug=True, port=5001)