from flask import Flask 
import controllers, models 

app = Flask(__name__) 
# create an instance of this class. The first argument is the name of the application’s module. 
# __name__ is a convenient shortcut that works in most cases. 
# Flask requires this so that it knows where to look for resources like templates and static files. 

app.secret_key = 'secret_key'
# a secret key that will be used for securely signing the session cookie and can be used by extensions or 
# your app.py for any other security-related needs. It should be a string of long random bytes.

app.register_blueprint(controllers.app)
# blueprint connects a collection of views, templates and routes from the controllers.py file 
# that can be applied to the app.py.

if __name__ == '__main__':
# if the Python interpreter is running that module as the main program, the __name__ variable is set to "__main__"; 
# if this file is imported from another module, __name__ will be set to the name of the module.
    models.init_db()
    # The init db() function connects to the database and creates the users table. 
    app.run(debug=True)
    # debugging mode on, the debugger actively monitors everything that's happening as the program runs. 

