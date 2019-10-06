from flask import Flask,  jsonify
from parser import Parser

app = Flask(__name__)

@app.route('/interface/<name>')
def getInterfaces(name):
    return jsonify( Parser.fromFile('config.txt').using(name).parse())

@app.route('/interface/<name>/<digit>')
def getUniqueInterfaces(name, digit):
    interfaceName = name + '/' + digit
    return jsonify( Parser.fromFile('config.txt').using(interfaceName).parse())

app.run(debug=True)