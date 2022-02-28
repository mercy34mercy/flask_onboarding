# -*- coding: utf-8 -*-
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return 'hello, world'

@app.route('/json',methods=['POST'])
def json():
    json = request.json
    return json