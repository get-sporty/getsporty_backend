# Get Sporty!

## Sportsground Data Model (sportsgrounds collection)
```python
{ name : 'The Allan Renwick Memorial Cricket Field',
  lat : 35.2809,
  long : 149.1300}
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
