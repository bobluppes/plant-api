from flask import Flask
from flask import request
import logging

app = Flask(__name__)


@app.route('/')
def landing():
    return 'Plant Sensor API'


@app.route('/', methods=['POST'])
def api():
    print(request)
    logging.info(request)
    return 200
