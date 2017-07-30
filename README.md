# Get Sporty!

## Screenshots

### Main App
-Green points have active events
-Red don't have events
-Both allow the user at add events!
![main app](https://image.ibb.co/gKzPVQ/image.png)

### New Event
-Needs proper css
![new event](https://image.ibb.co/jS8q4k/image.png)

### Subscription Service
-Needs proper css
-Allows connection through email
![subscription service](https://image.ibb.co/c8qyqQ/image.png

### Built on Amazon and .SPACE
![route 53](https://image.ibb.co/nAsBAQ/image.png)
![ec2](https://image.ibb.co/dhWzx5/image.png)

### MongoDB for flexibility
![mongodb](https://image.ibb.co/g28JqQ/image.png)

## Basic data models
### Sportsground Data Model (sportsgrounds collection)
```python
{
    'name' : name,
    'type' : [list, of, sports],
    'location': {
        'type': "Point",
        'coordinates' : [lon, lat]
    }
}
```

### Games Data Model (events collection)

```python
{ name : 'The renwallz challenge',
  creator : 'renwallz', #possibly OAuth?
  active : True,
  loc : <ref to field>,
  num_players : 24, #2 cricket teams, event should send start notification to players once it hits this amount
  subscribed : 2, #num of players in game
  time_created: current_timestamp, #time the event was created, in the future it could refer to scheduled time of game
  }
```

### Users Data Model (users collection)

```python
{ 
    'name' : name
    'email' : email
    'password': password #sha512 hashed password with salt
    'OAuth': OAuth token #if we have infinite time
}
```
