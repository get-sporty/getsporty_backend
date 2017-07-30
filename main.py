import requests, flask, pymongo

from flask_restful import Resource, Api

connection = pymongo.MongoClient('mongo.getsporty.space')
db = connection.getsporty

app = flask.Flask(__name__)

@app.route('/geoloc')
def geoloc():
    '''
    Unsure what this one is meant to do
    '''
    return

@app.route('/register')
def register(json_data):
    '''
    Register for a specified sport event
    '''
    user_data = json_data.encode('json')
    db.users.update({'user':user_data['user'],user_data,{'upsert':True})
    return

@app.route('/event')
def new_event(json_data):
    '''
    add a new event, using the event template specified in the README
    '''
    db.events.update(json_data) 
    return
	
@app.route('/results')
def get_nearby_points(json_data):
    '''
    get the nearby events, between minDistance and maxDistance
    '''
    location = json_data['location']
    points = []
    for i in db.events.find({
        'location': {
            '$near': {
                '$geometry': {location},
                '$minDistance': 5,
                '$maxDistance': 1000,
            }
        }
    }):
        points.append(i)
    return points    #I have no idea how flask works

def push_notification():
    flask.request()

if __name__ == '__main__':
    app.run()
