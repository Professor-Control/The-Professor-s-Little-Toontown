from SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 10100
BattleParent = 10102
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': 10100,
                'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': 5,
  'battleCell': BattleCellId,
  'pos': Point3(-4, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 7,
  'battleCell': BattleCellId,
  'pos': Point3(0, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 5,
  'battleCell': BattleCellId,
  'pos': Point3(4, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0}]
ReserveCogData = []
