from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

# https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/