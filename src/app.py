#'/api/v1/details'
#'/api/v1/healthz'

from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)


@app.route('/api/v1/details')

def details():
    return jsonify({
        "name": "ship-boring",
        "version": "0.0.1",
        "message": "This is a sample Python application that demonstrates how to build a simple REST API using Flask.",
        "time": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "Hostname": socket.gethostname(),
        "author": "Santosh P Katageri"
    })


@app.route('/api/v1/healthz')
def healthz():
    return jsonify({
        "status": "healthy"
    }), 200 

if __name__ == '__main__':
    app.run(host='0.0.0.0')