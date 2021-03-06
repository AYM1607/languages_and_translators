
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMA HOLA QUE TAL\n    phrase : a QUE TAL\n    \n    a : HOLA COMA a\n      | HOLA\n      |\n    '
    
_lr_action_items = {'HOLA':([0,5,],[3,3,]),'QUE':([0,2,3,5,7,],[-4,4,-3,-4,-2,]),'$end':([1,6,],[0,-1,]),'COMA':([3,],[5,]),'TAL':([4,],[6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'phrase':([0,],[1,]),'a':([0,5,],[2,7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> phrase","S'",1,None,None,None),
  ('phrase -> a QUE TAL','phrase',3,'p_phrase','hola.py',28),
  ('a -> HOLA COMA a','a',3,'p_a','hola.py',35),
  ('a -> HOLA','a',1,'p_a','hola.py',36),
  ('a -> <empty>','a',0,'p_a','hola.py',37),
]
