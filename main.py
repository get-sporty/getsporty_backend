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
    event_query = client.db.events.find({})
    points_list = []
    already_known = []
    for e in event_query:
        try:
            found = False
            for i,q in enumerate(already_known):
                if q['loc'] == e['loc']:
                    found = True
                    ground = client.sportsground.find_one({'_id': ObjectId(e['loc'])})
                    already_known[i]['content'] = q['content'].append(u'<p><a href="http://app.getsporty.space/subscribe_event?event={1}>{2}</a>'.format(
                        ground['name'], e['_id'], e['name']))
            if not found:
                e['content'] = u'<h2>{0}</h2><p><a href="http://app.getsporty.space/subscribe_event?event={0}>{1}</a>'.format(e['_id'],e['name'])
                already_known.append(e['loc'])
            else:
                ground = client.sportsground.find_one({'_id':ObjectId(e['loc'])})
                e['content'] = u'<p><a href="http://app.getsporty.space/subscribe_event?event={1}>{2}</a>'.format(ground['name'],e['_id'],e['name'])
                already_known.append(e['loc'])
        except KeyError:
            pass
    point_query = client.db.sportsgrounds.find({})
    for p in point_query:
        if p['_id'] not in already_known:
            p['colour'] = 'red'
            points_list.append(p)
    for i,p in enumerate(points_list):
        points_list[i]['content'] = [('<p><a href="http://127.0.0.1:5000/new_event?ground={0}">New Event</a>'.format(p['_id']))]
    return render_template('display.html',
                           points=points_list,
                           api=GOOGLE_MAPS_API)

@app.route('/new_event')
def new_event():
    if request.method == 'POST':
        name = request.form['name']
        creator = (request.form['creator_name'],request.form['creator_email'])
        active = True
        loc = ObjectId(request.form['field'])
        num_players = request.form['num_players']
        subscriber = [creator]
        client.db.events.insert({'name':name,'creator':creator,'active':active,'loc':loc,'num_player':num_players,'subscriber':subscriber})
        redirect(url_for("display_points"))
    else:
        d = request.args.get('ground')
        print d
        return render_template('subscribe_event.html',ground=d)


@app.route('/subscribe_event')
def subscribe_event(request):
    if request.method == 'POST':
        event = request.form['event']
        new_user = (request.form['user'],request.form['email'])
        client.db.sportsgrounds.find_one_and_update({'_id':ObjectId(event)},{'$push':{'subscriber':new_user}})
        redirect(url_for("display_points"))
    else:
        d = request.args.get('event')
        print d
        return render_template('new_event.html',event=d)

if __name__ == '__main__':
    app.run()

