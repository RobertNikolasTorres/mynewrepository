from flask import Flask    # From the flask module import the Flask class

app = Flask(__name__)       # Create an instance of Flask into app (object)

@app.get("/")               # Flask decorator for defininig routes
def index():                # A wrapped function is called a "view function"
    me = {                  # Python3 dictionary
        "first_name": "Robert",
        "last_name": "GPL",
        "hobbies": "DIY stuff",
        "is_online": True
    }
    return me               # When you return a dictionary, it is converted to JSON