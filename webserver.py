from flask import Flask

app = Flask("My Website")

@app.route("/")
def homepage():
    return "Weclome to my website!"

app.run()
