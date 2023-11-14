from flask import Flask, request

app = Flask(__name__)

@app.route('/') # Define the route. This would be http://127.0.0.1:5000
def index():
    return '<h3>Hello, World!</h3>' # We can send this basic string across HTTP

# What if we wanted to send an object / Python? We need to do more

@app.route('/spam') # Define the route. This would be http://127.0.0.1:5000/spam
def spam(): # Define a handler function to handle the route
    person = { 'name': 'John', 'age': 21 }
    return person, 201 # We can give the 201 as the status code
    # Flask packages up this route and provides the basic HTTP headers, etc.
    # Flask JSON-ifies the object

# @app.route('/hello') # Request: GET http://127.0.0.1:5000/hello?name=Matt
# def hello():
#     # print(request.headers) # We can get the request headers
#     name = request.args.get('name') # GET http://127.0.0.1:5000/hello?name=Jon now sets the name as Jon
#     # name = 'Jack'
#     return { 'message': f'Hello, {name}!' }

# THIS IS HOW YOU CAN RECEIVE RESTful API PARAMETERS
@app.route('/hello/<name>') # Request: GET http://127.0.0.1:5000/hello/blahblah
def hello(name): # Whatever you call the <>, you need it in the function as a parameter
    # name = request.args.get('name') # GET http://127.0.0.1:5000/hello?name=Jon now sets the name as Jon
    # name = 'Jack'
    return { 'message': f'Hello, {name}!' }

# GET http://127.0.0.1:5000/add/12/39
@app.route('/add/<int:num1>/<int:num2>') # Telling flask these are int
# Specifying data type also handles the error handling for you
def add(num1, num2):
        # num1 = int(request.args.get('num1')) 
        # num2 = int(request.args.get('num2'))
        return { 'result': num1 + num2 }
    # We don't need the try/except here because <int:num1> handles errors

# @app.route('/add') # Request: GET http://127.0.0.1:5000/add?num1=10&num2=24
# def add():
#     try:
#         num1 = int(request.args.get('num1')) # We need int() because URLs are always strings
#         num2 = int(request.args.get('num2'))
#         return { 'result': num1 + num2 }
#     except TypeError:
#         return { 'error': 'num1 and num2 must be int' }, 400 # Error handling for cases when num1 and num2 are not int

@app.errorhandler(TypeError) # Error handling for cases when num1 and num2 aren't provided
def type_error(error):
    return { 'error': str(error) }, 400

# The default 401 Error is in HTML. Flask must always return a JSON result, therefore
@app.errorhandler(404)
def not_found(error):
    # return { 'error': 'Not Found' }, 404 # We can define what the error is 
    return { 'error': str(error) }, 404 # Or we can allow Python to handle the error message

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, port=5001) # You can also set the port yourself