import socket
from flask import Flask


app = Flask(__name__)


@app.route('/square//',methods=['GET'])
def cuadrado(s1,s2):
    return str(s1**s2)


@app.route('/greetings')
def index():
    return 'Hello World !'
    print socket.getfqdn()


