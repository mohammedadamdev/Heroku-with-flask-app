from distutils.log import debug
from flask import Flask
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return "Hello Adam"

if __name__ == "__main__":
    app.run(debug=True)