import flask

#object in the code that is our app, declaring app
#flask. --> coming from library
#Flask(__name__) --> passed the name of the app
app = flask.Flask(__name__)

#tell flask what function to run when flask app is visited
#hey flask, this function lives here!
@app.route("/")
def index():
    return "Hello world"

app.run()