import socket
import time
from flask import Flask, render_template, url_for, jsonify
import sys
import linuxcnc
import numpy

from psutil import process_iter
from signal import SIGKILL # or SIGKILL


local_ip = socket.gethostbyname(socket.getfqdn())
print('Local IP: '+ local_ip)

app = Flask(__name__)

lastAction = {'id': 0,
              'last_action': 'empty'}

s = linuxcnc.stat()

c = linuxcnc.command()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api', methods=['GET'])
def api_all():
    s.poll()
    return jsonify('Position 2: ' + str( tuple(round(x, 3) for x in tuple_diff(s.joint_actual_position, s.g92_offset) )  ))


@app.route('/move_left')
def move_left():  
    s.poll()
    c.jog(linuxcnc.JOG_INCREMENT, 0, 100, -250)
    return jsonify("OKK")


@app.route('/move_right')
def move_right():
    print('Status 2: ' + str(s.state))
    c.jog(linuxcnc.JOG_INCREMENT, 0, 100, +250)

    return render_template("index.html")

def tuple_diff(a, b):
    return tuple(numpy.subtract(a, b))


if __name__ == '__main__':
    # s.poll()
    app.run(debug=True, host="0.0.0.0", port="2999")