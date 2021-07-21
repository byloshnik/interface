from flask import Flask, render_template, url_for, jsonify
import sqlite3

app = Flask(__name__)

lastAction = ""

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api', methods=['GET'])
def api_all():
    return jsonify(lastAction)

@app.route('/left')
def left():
    global lastAction
    lastAction = "moveLeft"
    return render_template("index.html")

@app.route('/right')
def right():
    global lastAction
    lastAction = "moveRight"
    return render_template("index.html")

@app.route('/users')
def user():
    connect = sqlite3.connect('db_students.db')
    cursor = connect.cursor()
    cursor.execute(f'SELECT * FROM Students')
    botinfo = cursor.fetchall()
    print(botinfo)
    return render_template("users.html", botinfo=botinfo)

if __name__ == '__main__':
    app.run(debug=True)