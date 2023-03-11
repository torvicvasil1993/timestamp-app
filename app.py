""" from flask import Flask
import datetime
import os

app = Flask(__name__)

@app.route('/')
def hello():
    file_path = '/app/timestamp.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            prev_timestamp = f.read()
    else:
        prev_timestamp = 'No previous timestamp found'
    now = datetime.datetime.now()
    current_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, 'w') as f:
        f.write(current_timestamp)
    return 'Current timestamp: ' + current_timestamp + '<br/>' + 'Previous timestamp: ' + prev_timestamp

if __name__ == '__main__':
    app.run()
 """

# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
