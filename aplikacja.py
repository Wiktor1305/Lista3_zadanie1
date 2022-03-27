from flask import Flask

aplikacja = Flask(__name__)

@aplikacja.route("/")
def index():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    aplikacja.run(debug=True)