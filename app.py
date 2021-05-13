from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def landing():
    return 'Plant Sensor API'


@app.route('/', methods=['POST'])
def api():
    print(request)
    return 200
