import requests, flask, pymongo

connection = pymongo.MongoClient('mongo.getsporty.space')
db = connection.getsporty
spherical_distance = 750/1000 #distance in kilometres

for ground in db.sportsgrounds.find({}):
    if "Canberra" in ground['name']:
        print ground

app = flask.Flask(__name__)
