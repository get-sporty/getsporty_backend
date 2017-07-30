from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO1_HOST'] = 'mongo.getsporty.space.'
app.config['MONGO1_PORT'] = 27017
app.config['MONGO1_DBNAME'] = 'getsporty'
client = PyMongo(app, config_prefix='MONGO1')

GOOGLE_MAPS_API = 'AIzaSyA4CyqW3oF2E-hFH_tFtVbMZOXiDnqBvdY'

@app.route('/')
def display_points():
    has_event_colour = '239B56'
    has_no_event_colour = 'FE7569'
    icon_base = 'http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|{0}'
    points_dict = {}

    event_query = client.db.events.find({})
    #Process locations with events in them
    for e in event_query:
        #If the location hasn't been seen yet
        if str(e['loc']) not in points_dict.keys():
            #Add content and green marker
            point = client.db.sportsgrounds.find_one({'_id': e['loc']})
            point['content'] = ['<p><h3>Events On</h3>']
            point['icon'] = icon_base.format(has_event_colour)
            points_dict[str(e['loc'])] = point
        #Subscription link for events
        event_id = str(e['_id'])
        event_name = e['name']
        new = points_dict[str(e['loc'])]['content']
        new.append('<p><a href="http://127.0.0.1:5000/subscribe_event?event={0}">{1}</a>'.format(event_id,event_name))
        points_dict[str(e['loc'])]['content'] = new
    #Get all points to check location. Can be optimised
    point_query = client.db.sportsgrounds.find({})

    #Process the non-event points
    for point in point_query:
        #If the location hasn't been seen yet
        if str(point['_id']) not in points_dict.keys():
            point['content'] = ['<p><h3>Events On</h3>No events yet!']
            point['icon'] = icon_base.format(has_no_event_colour)
            points_dict[str(point['_id'])] = point
    points_list = points_dict.values()

    #Add new entry to all points
    for i,p in enumerate(points_list):
        points_list[i]['content'].append('<p><h3>New Event</h3><a href="http://127.0.0.1:5000/new_event?ground={0}">New Event</a>'.format(p['_id']))
    return render_template('display.html',
                           points=points_list,
                           api=GOOGLE_MAPS_API)

@app.route('/new_event',methods=['GET','POST'])
def new_event():
    if request.method == 'POST':
        name = request.form['name']
        print name
        creator = (request.form['creator_name'],request.form['creator_email'])
        active = True
        loc = ObjectId(request.form['field'])
        num_players = request.form['num_players']
        subscriber = [creator]
        client.db.events.insert({'name':name,'creator':creator,'active':active,'loc':loc,'num_player':num_players,'subscriber':subscriber})
        return redirect(url_for("display_points"))
    else:
        d = request.args.get('ground')
        e = client.db.sportsgrounds.find_one({'_id':ObjectId(d)})['name']
        return render_template('new_event.html',
                            name=e,
                            ground=d)


@app.route('/subscribe_event',methods=['GET','POST'])
def subscribe_event():
    if request.method == 'POST':
        event = request.form['event']
        new_user = (request.form['user'],request.form['email'])
        client.db.events.find_one_and_update({'_id':ObjectId(event)},{'$push':{'subscriber':new_user}})
        return redirect(url_for("display_points"))
    else:
        d = request.args.get('event')
        e = client.db.events.find_one({'_id': ObjectId(d)})
        f = client.db.sportsgrounds.find_one({'_id':ObjectId(e['loc'])})['name']
        print d
        return render_template('subscribe_event.html',
                               event=e,
                               loc_name=f)

if __name__ == '__main__':
    app.run()

