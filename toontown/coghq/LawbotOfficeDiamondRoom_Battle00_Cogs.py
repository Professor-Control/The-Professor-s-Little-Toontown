from SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 10000
BattlePlace1 = 10000
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': BattlePlace1,
                'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': 10,
  'battleCell': BattleCellId,
  'pos': Point3(-6, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 11,
  'battleCell': BattleCellId,
  'pos': Point3(-2, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 10,
  'battleCell': BattleCellId,
  'pos': Point3(2, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 11,
  'battleCell': BattleCellId,
  'pos': Point3(6, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1}]
ReserveCogData = []
