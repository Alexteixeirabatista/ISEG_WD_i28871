from flask import Flask, request, make_response, render_template

app = Flask(_name_)

# @app.route('/')
# def index():
#     return 'Hello World!'

@app.route('/users/<username>')
def show_user(username):
    return f'User: {username}'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#    if request.method == 'POST': 
#       # handle login logic
#    else:
#       # show login form

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'test' and password == 'test':
            return 'Login successful'
        else:
            return 'Invalid username or password'

    return render_template('form.html')

# @app.route('/')
# def index():
#     response = make_response('Hello World!')
#     response.headers['Content-Type'] = 'text/plain'
#     return response

@app.route('/')
def index():
    name = 'John'
    return render_template('index.html', name=name)

if _name_ == '_main_':
    app.run()