from flask import Blueprint, request, redirect, url_for, session
import views
import models

app = Blueprint('app', __name__)
# blueprint named app to be  

@app.route('/')
def index_controller():
    if 'username' in session:
        return redirect(url_for('app.home_controller'))
    return views.index()
# if the user's login was successful during their session, they would be taken to the function home_controller; 
# otherwise, they would be shown the content of the views.index() module function,
# show message: "Incorrect username or password"

@app.route('/home', methods=['GET', 'POST'])
def home_controller():
    if request.method == 'POST':
        session.pop('username', None)
        return redirect(url_for('app.index_controller'))
    return views.home(session['username'])
# if the method is of the type GET, the function returns the output of another function (views.home),
# passing as an argument the value of the variable username;
# if the method used to communicate with the server is of type POST, the user's current session is terminated (Logout),
# and the information from the function index_controller is returned.

@app.route('/login', methods=['GET', 'POST'])
def login_controller():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = models.get_user(username)
        if user is not None and user[1] == password:
            session['username'] = username
            return redirect(url_for('app.home_controller'))
        return views.index(error='Incorrect username or password')
    return redirect(url_for('app.index_controller'))
# if the method is of the type POST, the function reads the values inputted in the Index.htlm Login (Username and Password)
# and if they both match in the database, the user's Login is successful and they would be taken to the function 
# home_controller otherwise, they would be shown the error of the views.index() module function:
# "Incorrect username or password". If the method is of the type GET it would be taken to the function app_index.

@app.route('/register', methods=['GET', 'POST'])
def register_controller():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = models.get_user(username)
        if user is None:
            models.add_user(username, password)
            return redirect(url_for('app.index_controller'))
        return views.index(error='Username already taken')
    return redirect(url_for('app.index_controller'))
# if the method is of the type POST, the function reads the values inputted in the Index.htlm Register (Username and Password) 
# and insert them into the database through models.add_user and return to index_controller function. 
# If the inputted username is already taken, they would be shown the error of the views.index() module function:
#  "Username already taken". If the method is of the type GET it would be taken to the function app_index.

