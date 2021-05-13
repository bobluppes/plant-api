from flask import Flask
from flask import request
import logging
import uuid
import json

app = Flask(__name__)


@app.route('/')
def landing():
    return 'Plant Sensor API'


@app.route('/', methods=['POST'])
def api():
    data = request.json

    print(data)
    
    message = app.config['AZURE_TABLE']
    rowkey = str(uuid.uuid4())

    data['rowKey'] = rowkey


    message.set(json.dumps(data))
    return rowkey
