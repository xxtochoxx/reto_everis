import socket
from flask import Flask


app = Flask(__name__)


@app.route('/square/',methods=['GET'])
def cuadrado(s1):
	res = str(s1**s1)
    return 'number :' + s1 + 'square ' + res


@app.route('/greetings')
def hello():
    return 'Hello World !'
    print socket.getfqdn()


