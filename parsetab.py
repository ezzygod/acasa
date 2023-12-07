
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COS DIVIDE LOG LPAREN MINUS NUMBER PLUS POWER RPAREN SIN SQRT TAN TIMESexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression POWER expressionexpression : SQRT expression\n                  | LOG expressionexpression : SIN expression\n                  | COS expression\n                  | TAN expressionexpression : LPAREN expression RPARENexpression : NUMBER'
    
_lr_action_items = {'SQRT':([0,2,3,4,5,6,7,9,10,11,12,13,],[2,2,2,2,2,2,2,2,2,2,2,2,]),'LOG':([0,2,3,4,5,6,7,9,10,11,12,13,],[3,3,3,3,3,3,3,3,3,3,3,3,]),'SIN':([0,2,3,4,5,6,7,9,10,11,12,13,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'COS':([0,2,3,4,5,6,7,9,10,11,12,13,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'TAN':([0,2,3,4,5,6,7,9,10,11,12,13,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'LPAREN':([0,2,3,4,5,6,7,9,10,11,12,13,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'NUMBER':([0,2,3,4,5,6,7,9,10,11,12,13,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'$end':([1,8,14,15,16,17,18,20,21,22,23,24,25,],[0,-12,-6,-7,-8,-9,-10,-1,-2,-3,-4,-5,-11,]),'PLUS':([1,8,14,15,16,17,18,19,20,21,22,23,24,25,],[9,-12,9,9,9,9,9,9,9,9,9,9,9,-11,]),'MINUS':([1,8,14,15,16,17,18,19,20,21,22,23,24,25,],[10,-12,10,10,10,10,10,10,10,10,10,10,10,-11,]),'TIMES':([1,8,14,15,16,17,18,19,20,21,22,23,24,25,],[11,-12,11,11,11,11,11,11,11,11,11,11,11,-11,]),'DIVIDE':([1,8,14,15,16,17,18,19,20,21,22,23,24,25,],[12,-12,12,12,12,12,12,12,12,12,12,12,12,-11,]),'POWER':([1,8,14,15,16,17,18,19,20,21,22,23,24,25,],[13,-12,13,13,13,13,13,13,13,13,13,13,13,-11,]),'RPAREN':([8,14,15,16,17,18,19,20,21,22,23,24,25,],[-12,-6,-7,-8,-9,-10,25,-1,-2,-3,-4,-5,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,3,4,5,6,7,9,10,11,12,13,],[1,14,15,16,17,18,19,20,21,22,23,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','calc2.py',55),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','calc2.py',56),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','calc2.py',57),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','calc2.py',58),
  ('expression -> expression POWER expression','expression',3,'p_expression_binop','calc2.py',59),
  ('expression -> SQRT expression','expression',2,'p_expression_unop','calc2.py',72),
  ('expression -> LOG expression','expression',2,'p_expression_unop','calc2.py',73),
  ('expression -> SIN expression','expression',2,'p_expression_trig','calc2.py',80),
  ('expression -> COS expression','expression',2,'p_expression_trig','calc2.py',81),
  ('expression -> TAN expression','expression',2,'p_expression_trig','calc2.py',82),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','calc2.py',91),
  ('expression -> NUMBER','expression',1,'p_expression_number','calc2.py',95),
]
