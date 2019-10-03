from flask import Flask,  jsonify
from parser import Parser

app = Flask(__name__)

@app.route('/interface/<name>')
def getInterfaces(name):
    return jsonify( Parser.fromFile('config.txt').using(name).parse())