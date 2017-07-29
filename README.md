# Get Sporty!

## Sportsground Data Model (sportsgrounds collection)
```python
{
        'name' : name
        'location': {
            'type': "Point",
            'coordinates' : [lon, lat]
        }
            }
```

## Games Data Model (games collection)

```python
{ name : 'The renwallz challenge',
  creator : 'ajrenwi', #possibly OAuth?
  active : True,
  loc : <ref to field>,
  num_players : 24, #2 cricket teams, event should send start notification to players once it hits this amount
  subscribed : 2, #num of players in game
  }
```
