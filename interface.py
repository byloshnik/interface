import socket
import time
from flask import Flask, render_template, url_for, jsonify, request
import sys
import linuxcnc
import numpy

local_ip = socket.gethostbyname(socket.getfqdn())
print('Local IP: ' + local_ip)

app = Flask(__name__)
s = linuxcnc.stat()
c = linuxcnc.command()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api', methods=['GET'])
def api_all():
    s.poll()
    return jsonify('Position 2: ' + str(tuple(round(x, 3) for x in tuple_diff(s.joint_actual_position, s.g92_offset))))


@app.route('/jog')
def jog():
    c.jog(linuxcnc.JOG_INCREMENT, int(
        request.args['axis']), 100, float(request.args['distance']))
    return jsonify("Success")


@app.route('/home')
def home():
    if request.args['axis'] == 'all':
        # for axis in s.axis:
        for axis in range(4):
            c.home(axis)
    else:
        c.home(int(request.args['axis']))
    return jsonify("Success")


def tuple_diff(a, b):
    return tuple(numpy.subtract(a, b))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="786")
