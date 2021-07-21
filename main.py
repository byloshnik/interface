from flask import Flask, render_template, url_for, jsonify
import sqlite3

app = Flask(__name__)

lastAction = {'id': 0,
              'last_action': 'empty'}


@app.route('/')
def index():
    return render_template("index_back.html")


@app.route('/api', methods=['GET'])
def api_all():
    return jsonify(lastAction)


@app.route('/move_left')
def move_left():
    lastAction['id'] += 1
    lastAction['last_action'] = 'move_left'
    return render_template("index_back.html")


@app.route('/move_right')
def move_right():
    lastAction['id'] += 1
    lastAction['last_action'] = 'move_right'
    return render_template("index_back.html")


if __name__ == '__main__':
    app.run(debug=True)