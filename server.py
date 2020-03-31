from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<username>") # Revisit decorators if you unclear of this syntax
def index(username):
    return render_template('index.html', name = username)

@app.route("/another")
def showing():
    return '<h1>Yo</h1>'

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run(debug = True)