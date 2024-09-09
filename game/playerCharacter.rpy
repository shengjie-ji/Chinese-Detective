init -99 python:
  # Using Composition
  class PlayerCharacter:
      def __init__(self, name, stats **kwargs):
          self.character = Character(name, **kwargs)
          self.stats = stats  

### Characters
define chi      = PlayerCharacter('Song Qi', stats = {
    'Martial Arts' : 0,
    'Jogging'      : 0,
    'Eating Out'   : 0,
    'Casual Sex'   : 0,
    'Gamer'        : 0,
    'Raver'        : 0,
    'Side Hustle'  : 0,
    'Reader'       : 0,
    'Socialite'    : 0
    },
    color = (19, 252, 3)) 
