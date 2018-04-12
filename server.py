from flask import Flask


app = Flask(__name__)

@app.route('/relay/<any(1,0):action>', methods = ['GET'])
def move_relay(action):
    if action == 1:
        return 'si'
    else:
        return 'no'
