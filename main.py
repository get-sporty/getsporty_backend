import requests, flask, pymongo

from flask_restful import Resource, Api

connection = pymongo.MongoClient('mongo.getsporty.space')
db = connection.getsporty

app = flask.Flask(__name__)

@app.route('/geoloc')
def geoloc():
    return

@app.route('/register')
def register(json_data):
    user_data = json_data.encode('json')
    db.users.update({'user':user_data['user'],user_data,{'upsert':True})
    return

@app.route('/event')
def new_event(json_data):
    db.users.update()
    return

def push_notification():
    flask.request()

if __name__ == '__main__':
    app.run()
