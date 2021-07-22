import socket
import time
from flask import Flask, render_template, url_for, jsonify
import sys
import linuxcnc

local_ip = socket.gethostbyname(socket.getfqdn())
print('Local IP: '+ local_ip)

app = Flask(__name__)

lastAction = {'id': 0,
              'last_action': 'empty'}
s = linuxcnc.stat()
c = linuxcnc.command()

@app.route('/')
def index():
    return render_template("index_back.html")


@app.route('/api', methods=['GET'])
def api_all():
    return jsonify(lastAction)


@app.route('/move_left')
def move_left():
    s.poll()
    print('Status 444: ' + str(s.state))
    c.jog(linuxcnc.JOG_INCREMENT, 0, 10, 250)
    lastAction['id'] += 1
    lastAction['last_action'] = 'move_left'
    return render_template("index_back.html")


@app.route('/move_right')
def move_right():
    lastAction['id'] += 1
    lastAction['last_action'] = 'move_right'
    return render_template("index_back.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=12)