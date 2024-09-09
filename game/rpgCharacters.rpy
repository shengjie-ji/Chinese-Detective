init -99 python:
  # Using Composition
  class RPGCharacter:
      def __init__(self, name, relationship, **kwargs):
          self.character = Character(name, **kwargs)
          self.relationship = relationship  

### Characters
define chi      = Character('Song Qi', color = (19, 252, 3)) 
define dre      = RPGCharacter('Drita Xhaferi', relationship = {
    'Respect'   : 70,
    'Fear'      : 20,
    'Affection' : 70,
    'Community' : 40,
    'Motive'    : 'Novelty',
    'Flaw'      : 'Gelangweilt',
    'Stress'    : 30,
    'Memory'    : 90
    },
    color = (244, 3, 252)) 
define client   = RPGCharacter('Client', relationship = {
    'Respect'   : 50,
    'Fear'      : 20,
    'Affection' : 20,
    'Community' : 10,
    'Motive'    : 'Concern',
    'Flaw'      : 'Homeostasis',
    'Stress'    : 25,
    'Memory'    : 70
    },
    color = (252, 90, 3)) 
define bill   = RPGCharacter('Bill', relationship = {
    'Respect'   : 20,
    'Fear'      : 70,
    'Affection' : 10,
    'Community' : 10,
    'Motive'    : 'Survive',
    'Flaw'      : 'Scavenger',
    'Stress'    : 70,
    'Memory'    : 40
    },
    color = (3, 28, 252)) 
define tutorial = Character("Tutorial", color = (3, 252, 223)) 
define eva      = RPGCharacter("Eva", relationship = {
    'Respect'   : 80,
    'Fear'      : 10,
    'Affection' : 90,
    'Community' : 20,
    'Motive'    : 'Peace',
    'Flaw'      : 'Saint',
    'Stress'    : 10,
    'Memory'    : 50
    }, color = (252, 3, 3)) 
