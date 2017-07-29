import flask
from flask_pymongo import PyMongo

app = flask.Flask(__name__)
app.config['MONGO1_HOST'] = 'mongo.getsporty.space.'
app.config['MONGO1_PORT'] = 27017
app.config['MONGO1_DBNAME'] = 'getsporty'
client = PyMongo(app, config_prefix='MONGO1')

GOOGLE_MAPS_API = 'AIzaSyA4CyqW3oF2E-hFH_tFtVbMZOXiDnqBvdY'

@app.route('/')
def display_points():
    pq = client.db.sportsgrounds.find({})
    return flask.render_template('display.html',
                           points=pq,
                           api=GOOGLE_MAPS_API)

if __name__ == '__main__':
    app.run()