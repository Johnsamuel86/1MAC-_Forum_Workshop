from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hi! this is the Home Page"

@app.route("/SayHello/<name>")
def say_hello(name):
    return "Hello {}".format(name)


if __name__ == "__main__":
    app.run(debug=True)
