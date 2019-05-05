
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'and closedBra closedParen coma div do doubleColon doubleEquals elif else end endline equals exit id if int integer less lessEquals minus more moreEquals mul not notEquals openBra openParen or parens plus print program rea read real string subroutine swap then\n    programa : program action_37 id V F action_38 B end program\n    \n    V : V Tipo Dim doubleColon Rid action_addSymbols action_32\n      |\n    \n    Rid : id\n       | Rid coma id\n    \n    Tipo : integer\n         | real\n    \n    Dim : openBra int action_30 closedBra\n        | openBra int action_30 closedBra openBra int action_31 closedBra\n        |\n    \n    F : F subroutine id action_39 B end subroutine action_40\n      |\n    \n    B : B S\n      |\n    \n    S : Dimensional equals EA action_8\n      | id parens action_41\n      | read RDimensional\n      | print RDimOrString\n      | if action_16 Relif ElseOrEmpty end if action_20\n      | do id action_24 equals EA action_25 coma EA action_26 IntOrEmpty then B action_29 end do\n      | do then action_21 B action_22 end do\n      | swap Dimensional coma Dimensional\n      | exit action_23 \n    \n    Dimensional : id DimensionsOrEmpty action_1\n    \n    DimensionsOrEmpty : openParen EA action_setDim1 ComaEAOrEmpty closedParen\n                      |\n    \n    ComaEAOrEmpty : coma EA action_setDim2\n                  |\n    \n    RDimensional : Dimensional action_36\n                 | RDimensional coma Dimensional action_36\n    \n    RDimOrString : DimOrString\n                 | RDimOrString coma DimOrString\n    \n    DimOrString : Dimensional action_33\n                | string action_34\n                | endline action_34\n    \n    Relif : openParen EL closedParen action_17 then B\n          | Relif elif action_18 openParen EL closedParen action_17 then B\n    \n    ElseOrEmpty : else action_19 B\n                |\n    \n    IntOrEmpty : coma int action_28\n               | action_27\n    \n    EA : MultDiv\n       | EA SumOrSub action_3 MultDiv action_4\n    \n    SumOrSub : plus\n             | minus\n    \n    MultDiv : EAParens\n            | MultDiv MDSymbols action_5 EAParens action_6\n    \n    MDSymbols : mul\n              | div\n    \n    EAParens : EItem\n             | openParen EA closedParen\n    \n    EL : AND\n       | EL or action_10 AND action_9\n    \n    AND : Equality\n        | AND and action_12 Equality action_11\n    \n    Equality : EItem EQSymbols action_13 EItem action_14\n             | openParen EL closedParen\n             | not EL action_15\n    \n    EItem : Dimensional\n          | int action_2\n          | rea action_2_rea\n    \n    EQSymbols : less\n              | more\n              | doubleEquals\n              | notEquals\n              | lessEquals\n              | moreEquals\n    action_addSymbols :action_1 :action_2 :action_2_rea :action_3 :action_4 :action_5 :action_6 :action_8 :action_9 :action_10 :action_11 :action_12 :action_13 :action_14 :action_15 :action_16 :action_17 :action_18 :action_19 :action_20 :action_21 :action_22 :action_23 :action_24 :action_25 :action_26 :action_27 :action_28 :action_29 :action_30 :action_31 :action_32 :action_33 :action_34 :action_36 :action_37 :action_38 :action_39 :action_40 :action_41 :action_setDim1 :action_setDim2 :'
    
_lr_action_items = {'program':([0,19,],[2,35,]),'$end':([1,35,],[0,-1,]),'id':([2,3,4,5,6,10,11,14,15,16,20,22,23,25,26,27,28,29,30,32,33,34,36,37,38,39,40,41,42,43,44,47,49,50,51,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,72,74,75,77,78,82,83,84,85,86,87,88,89,90,91,92,95,96,101,102,103,104,105,107,109,110,111,112,115,118,119,120,121,122,123,124,125,126,130,132,134,135,136,137,138,141,142,143,149,150,151,153,157,158,160,167,171,173,175,178,],[-104,4,-3,-12,-105,-14,15,18,-106,30,-13,39,39,46,39,-91,-14,-68,-4,-108,-69,39,39,-17,-103,-26,-18,-31,-101,-102,-102,-89,-23,18,-100,78,-16,-24,39,-42,-46,-50,-59,-70,-71,-76,39,-29,39,-33,-34,-35,39,-14,39,-2,-5,-72,-44,-45,-74,-48,-49,-60,-61,-15,-103,-32,-87,39,39,39,18,-22,-107,-51,39,39,39,-30,-14,-78,-80,-81,-62,-63,-64,-65,-66,-67,-11,-25,-73,-75,-88,39,18,39,39,39,-43,-47,-19,-14,39,-21,18,-14,18,-14,18,-20,]),'integer':([4,5,29,30,51,77,78,],[-3,8,-68,-4,-100,-2,-5,]),'real':([4,5,29,30,51,77,78,],[-3,9,-68,-4,-100,-2,-5,]),'subroutine':([4,5,6,29,30,51,76,77,78,105,130,],[-3,-12,11,-68,-4,-100,105,-2,-5,-107,-11,]),'end':([4,5,6,10,14,15,20,27,28,29,30,32,33,37,38,39,40,41,42,43,44,47,49,50,51,54,55,58,59,60,61,62,63,64,66,68,69,70,71,74,77,78,88,89,90,91,92,93,95,103,104,105,107,112,115,129,130,132,134,135,136,138,149,150,151,153,158,160,167,171,173,175,176,178,],[-3,-12,-105,-14,19,-106,-13,-91,-14,-68,-4,-108,-69,-17,-103,-26,-18,-31,-101,-102,-102,-89,-23,76,-100,-16,-24,-42,-46,-50,-59,-70,-71,-76,-29,-33,-34,-35,-39,-14,-2,-5,-60,-61,-15,-103,-32,113,-87,-90,-22,-107,-51,-30,-14,146,-11,-25,-73,-75,-88,-38,-43,-47,-19,-14,-21,-36,-14,-37,-14,-97,177,-20,]),'read':([4,5,6,10,14,15,20,27,28,29,30,32,33,37,38,39,40,41,42,43,44,47,49,50,51,54,55,58,59,60,61,62,63,64,66,68,69,70,74,77,78,88,89,90,91,92,95,103,104,105,107,112,115,130,132,134,135,136,138,149,150,151,153,158,160,167,171,173,175,178,],[-3,-12,-105,-14,22,-106,-13,-91,-14,-68,-4,-108,-69,-17,-103,-26,-18,-31,-101,-102,-102,-89,-23,22,-100,-16,-24,-42,-46,-50,-59,-70,-71,-76,-29,-33,-34,-35,-14,-2,-5,-60,-61,-15,-103,-32,-87,22,-22,-107,-51,-30,-14,-11,-25,-73,-75,-88,22,-43,-47,-19,-14,-21,22,-14,22,-14,22,-20,]),'print':([4,5,6,10,14,15,20,27,28,29,30,32,33,37,38,39,40,41,42,43,44,47,49,50,51,54,55,58,59,60,61,62,63,64,66,68,69,70,74,77,78,88,89,90,91,92,95,103,104,105,107,112,115,130,132,134,135,136,138,149,150,151,153,158,160,167,171,173,175,178,],[-3,-12,-105,-14,23,-106,-13,-91,-14,-68,-4,-108,-69,-17,-103,-26,-18,-31,-101,-102,-102,-89,-23,23,-100,-16,-24,-42,-46,-50,-59,-70,-71,-76,-29,-33,-34,-35,-14,-2,-5,-60,-61,-15,-103,-32,-87,23,-22,-107,-51,-30,-14,-11,-25,-73,-75,-88,23,-43,-47,-19,-14,-21,23,-14,23,-14,23,-20,]),'if':([4,5,6,10,14,15,20,27,28,29,30,32,33,37,38,39,40,41,42,43,44,47,49,50,51,54,55,58,59,60,61,62,63,64,66,68,69,70,74,77,78,88,89,90,91,92,95,103,104,105,107,112,113,115,130,132,134,135,136,138,149,150,151,153,158,160,167,171,173,175,178,],[-3,-12,-105,-14,24,-106,-13,-91,-14,-68,-4,-108,-69,-17,-103,-26,-18,-31,-101,-102,-102,-89,-23,24,-100,-16,-24,-42,-46,-50,-59,-70,-71,-76,-29,-33,-34,-35,-14,-2,-5,-60,-61,-15,-103,-32,-87,24,-22,-107,-51,-30,136,-14,-11,-25,-73,-75,-88,24,-43,-47,-19,-14,-21,24,-14,24,-14,24,-20,]),'do':([4,5,6,10,14,15,20,27,28,29,30,32,33,37,38,39,40,41,42,43,44,47,49,50,51,54,55,58,59,60,61,62,63,64,66,68,69,70,74,77,78,88,89,90,91,92,95,103,104,105,107,112,115,130,132,134,135,136,138,146,149,150,151,153,158,160,167,171,173,175,177,178,],[-3,-12,-105,-14,25,-106,-13,-91,-14,-68,-4,-108,-69,-17,-103,-26,-18,-31,-101,-102,-102,-89,-23,25,-100,-16,-24,-42,-46,-50,-59,-70,-71,-76,-29,-33,-34,-35,-14,-2,-5,-60,-61,-15,-103,-32,-87,25,-22,-107,-51,-30,-14,-11,-25,-73,-75,-88,25,158,-43,-47,-19,-14,-21,25,-14,25,-14,25,178,-20,]),'swap':([4,5,6,10,14,15,20,27,28,29,30,32,33,37,38,39,40,41,42,43,44,47,49,50,51,54,55,58,59,60,61,62,63,64,66,68,69,70,74,77,78,88,89,90,91,92,95,103,104,105,107,112,115,130,132,134,135,136,138,149,150,151,153,158,160,167,171,173,175,178,],[-3,-12,-105,-14,26,-106,-13,-91,-14,-68,-4,-108,-69,-17,-103,-26,-18,-31,-101,-102,-102,-89,-23,26,-100,-16,-24,-42,-46,-50,-59,-70,-71,-76,-29,-33,-34,-35,-14,-2,-5,-60,-61,-15,-103,-32,-87,26,-22,-107,-51,-30,-14,-11,-25,-73,-75,-88,26,-43,-47,-19,-14,-21,26,-14,26,-14,26,-20,]),'exit':([4,5,6,10,14,15,20,27,28,29,30,32,33,37,38,39,40,41,42,43,44,47,49,50,51,54,55,58,59,60,61,62,63,64,66,68,69,70,74,77,78,88,89,90,91,92,95,103,104,105,107,112,115,130,132,134,135,136,138,149,150,151,153,158,160,167,171,173,175,178,],[-3,-12,-105,-14,27,-106,-13,-91,-14,-68,-4,-108,-69,-17,-103,-26,-18,-31,-101,-102,-102,-89,-23,27,-100,-16,-24,-42,-46,-50,-59,-70,-71,-76,-29,-33,-34,-35,-14,-2,-5,-60,-61,-15,-103,-32,-87,27,-22,-107,-51,-30,-14,-11,-25,-73,-75,-88,27,-43,-47,-19,-14,-21,27,-14,27,-14,27,-20,]),'openBra':([7,8,9,53,],[13,-6,-7,79,]),'doubleColon':([7,8,9,12,53,147,],[-10,-6,-7,16,-8,-9,]),'int':([13,34,36,56,72,79,82,83,84,85,86,87,96,101,102,109,110,111,118,119,120,121,122,123,124,125,126,137,141,142,143,157,168,],[17,62,62,62,62,106,-72,-44,-45,-74,-48,-49,62,62,62,62,62,62,-78,-80,-81,-62,-63,-64,-65,-66,-67,62,62,62,62,62,172,]),'closedBra':([17,31,106,131,],[-98,53,-99,147,]),'parens':([18,],[32,]),'openParen':([18,24,34,36,39,45,56,72,82,83,84,85,86,87,94,96,101,102,109,110,111,114,118,119,137,141,142,157,],[34,-84,56,56,34,72,56,96,-72,-44,-45,-74,-48,-49,-86,96,96,56,56,56,56,137,-78,-80,96,96,96,56,]),'equals':([18,21,33,46,55,73,132,],[-26,36,-69,-92,-24,102,-25,]),'elif':([20,27,32,33,37,38,39,40,41,42,43,44,49,54,55,58,59,60,61,62,63,64,66,68,69,70,71,88,89,90,91,92,104,107,112,132,134,135,136,149,150,151,153,158,160,167,171,178,],[-13,-91,-108,-69,-17,-103,-26,-18,-31,-101,-102,-102,-23,-16,-24,-42,-46,-50,-59,-70,-71,-76,-29,-33,-34,-35,94,-60,-61,-15,-103,-32,-22,-51,-30,-25,-73,-75,-88,-43,-47,-19,-14,-21,-36,-14,-37,-20,]),'else':([20,27,32,33,37,38,39,40,41,42,43,44,49,54,55,58,59,60,61,62,63,64,66,68,69,70,71,88,89,90,91,92,104,107,112,132,134,135,136,149,150,151,153,158,160,167,171,178,],[-13,-91,-108,-69,-17,-103,-26,-18,-31,-101,-102,-102,-23,-16,-24,-42,-46,-50,-59,-70,-71,-76,-29,-33,-34,-35,95,-60,-61,-15,-103,-32,-22,-51,-30,-25,-73,-75,-88,-43,-47,-19,-14,-21,-36,-14,-37,-20,]),'string':([23,67,],[43,43,]),'endline':([23,67,],[44,44,]),'then':([25,33,39,55,58,59,60,61,62,63,88,89,107,117,132,134,135,140,149,150,159,164,165,166,169,170,172,174,],[47,-69,-26,-24,-42,-46,-50,-59,-70,-71,-60,-61,-51,-85,-25,-73,-75,153,-43,-47,-85,-94,167,-95,173,-41,-96,-40,]),'coma':([29,30,33,37,38,39,40,41,42,43,44,48,55,57,58,59,60,61,62,63,66,68,69,70,78,81,88,89,91,92,107,112,128,132,134,135,145,149,150,164,166,],[52,-4,-69,65,-103,-26,67,-31,-101,-102,-102,75,-24,-109,-42,-46,-50,-59,-70,-71,-29,-33,-34,-35,-5,109,-60,-61,-103,-32,-51,-30,-93,-25,-73,-75,157,-43,-47,-94,168,]),'mul':([33,39,55,58,59,60,61,62,63,88,89,107,132,134,135,150,],[-69,-26,-24,86,-46,-50,-59,-70,-71,-60,-61,-51,-25,86,-75,-47,]),'div':([33,39,55,58,59,60,61,62,63,88,89,107,132,134,135,150,],[-69,-26,-24,87,-46,-50,-59,-70,-71,-60,-61,-51,-25,87,-75,-47,]),'plus':([33,39,55,57,58,59,60,61,62,63,64,80,88,89,107,128,132,133,134,135,149,150,164,],[-69,-26,-24,83,-42,-46,-50,-59,-70,-71,83,83,-60,-61,-51,83,-25,83,-73,-75,-43,-47,83,]),'minus':([33,39,55,57,58,59,60,61,62,63,64,80,88,89,107,128,132,133,134,135,149,150,164,],[-69,-26,-24,84,-42,-46,-50,-59,-70,-71,84,84,-60,-61,-51,84,-25,84,-73,-75,-43,-47,84,]),'closedParen':([33,39,55,57,58,59,60,61,62,63,80,81,88,89,97,98,99,107,108,116,127,132,133,134,135,139,144,148,149,150,152,154,155,156,161,162,163,],[-69,-26,-24,-109,-42,-46,-50,-59,-70,-71,107,-28,-60,-61,117,-52,-54,-51,132,139,-83,-25,-110,-73,-75,-57,-58,-27,-43,-47,159,-77,-79,-82,-53,-55,-56,]),'less':([33,39,55,61,62,63,88,89,100,132,],[-69,-26,-24,-59,-70,-71,-60,-61,121,-25,]),'more':([33,39,55,61,62,63,88,89,100,132,],[-69,-26,-24,-59,-70,-71,-60,-61,122,-25,]),'doubleEquals':([33,39,55,61,62,63,88,89,100,132,],[-69,-26,-24,-59,-70,-71,-60,-61,123,-25,]),'notEquals':([33,39,55,61,62,63,88,89,100,132,],[-69,-26,-24,-59,-70,-71,-60,-61,124,-25,]),'lessEquals':([33,39,55,61,62,63,88,89,100,132,],[-69,-26,-24,-59,-70,-71,-60,-61,125,-25,]),'moreEquals':([33,39,55,61,62,63,88,89,100,132,],[-69,-26,-24,-59,-70,-71,-60,-61,126,-25,]),'and':([33,39,55,61,62,63,88,89,98,99,127,132,139,144,154,155,156,161,162,163,],[-69,-26,-24,-59,-70,-71,-60,-61,119,-54,-83,-25,-57,-58,119,-79,-82,-53,-55,-56,]),'or':([33,39,55,61,62,63,88,89,97,98,99,116,127,132,139,144,152,154,155,156,161,162,163,],[-69,-26,-24,-59,-70,-71,-60,-61,118,-52,-54,118,118,-25,-57,-58,118,-77,-79,-82,-53,-55,-56,]),'rea':([34,36,56,72,82,83,84,85,86,87,96,101,102,109,110,111,118,119,120,121,122,123,124,125,126,137,141,142,143,157,],[63,63,63,63,-72,-44,-45,-74,-48,-49,63,63,63,63,63,63,-78,-80,-81,-62,-63,-64,-65,-66,-67,63,63,63,63,63,]),'not':([72,96,101,118,119,137,141,142,],[101,101,101,-78,-80,101,101,101,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'action_37':([2,],[3,]),'V':([4,],[5,]),'F':([5,],[6,]),'Tipo':([5,],[7,]),'action_38':([6,],[10,]),'Dim':([7,],[12,]),'B':([10,28,74,115,153,167,173,],[14,50,103,138,160,171,175,]),'S':([14,50,103,138,160,171,175,],[20,20,20,20,20,20,20,]),'Dimensional':([14,22,23,26,34,36,50,56,65,67,72,75,96,101,102,103,109,110,111,137,138,141,142,143,157,160,171,175,],[21,38,42,48,61,61,21,61,91,42,61,104,61,61,61,21,61,61,61,61,21,61,61,61,61,21,21,21,]),'action_39':([15,],[28,]),'Rid':([16,],[29,]),'action_30':([17,],[31,]),'DimensionsOrEmpty':([18,39,],[33,33,]),'RDimensional':([22,],[37,]),'RDimOrString':([23,],[40,]),'DimOrString':([23,67,],[41,92,]),'action_16':([24,],[45,]),'action_23':([27,],[49,]),'action_addSymbols':([29,],[51,]),'action_41':([32,],[54,]),'action_1':([33,],[55,]),'EA':([34,36,56,102,109,157,],[57,64,80,128,133,164,]),'MultDiv':([34,36,56,102,109,110,157,],[58,58,58,58,58,134,58,]),'EAParens':([34,36,56,102,109,110,111,157,],[59,59,59,59,59,59,135,59,]),'EItem':([34,36,56,72,96,101,102,109,110,111,137,141,142,143,157,],[60,60,60,100,100,100,60,60,60,60,100,100,100,156,60,]),'action_36':([38,91,],[66,112,]),'action_33':([42,],[68,]),'action_34':([43,44,],[69,70,]),'Relif':([45,],[71,]),'action_24':([46,],[73,]),'action_21':([47,],[74,]),'action_32':([51,],[77,]),'action_setDim1':([57,],[81,]),'SumOrSub':([57,64,80,128,133,164,],[82,82,82,82,82,82,]),'MDSymbols':([58,134,],[85,85,]),'action_2':([62,],[88,]),'action_2_rea':([63,],[89,]),'action_8':([64,],[90,]),'ElseOrEmpty':([71,],[93,]),'EL':([72,96,101,137,],[97,116,127,152,]),'AND':([72,96,101,137,141,],[98,98,98,98,154,]),'Equality':([72,96,101,137,141,142,],[99,99,99,99,99,155,]),'ComaEAOrEmpty':([81,],[108,]),'action_3':([82,],[110,]),'action_5':([85,],[111,]),'action_18':([94,],[114,]),'action_19':([95,],[115,]),'EQSymbols':([100,],[120,]),'action_22':([103,],[129,]),'action_40':([105,],[130,]),'action_31':([106,],[131,]),'action_17':([117,159,],[140,165,]),'action_10':([118,],[141,]),'action_12':([119,],[142,]),'action_13':([120,],[143,]),'action_15':([127,],[144,]),'action_25':([128,],[145,]),'action_setDim2':([133,],[148,]),'action_4':([134,],[149,]),'action_6':([135,],[150,]),'action_20':([136,],[151,]),'action_9':([154,],[161,]),'action_11':([155,],[162,]),'action_14':([156,],[163,]),'action_26':([164,],[166,]),'IntOrEmpty':([166,],[169,]),'action_27':([166,],[170,]),'action_28':([172,],[174,]),'action_29':([175,],[176,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> program action_37 id V F action_38 B end program','programa',9,'p_programa','fort.py',223),
  ('V -> V Tipo Dim doubleColon Rid action_addSymbols action_32','V',7,'p_V','fort.py',230),
  ('V -> <empty>','V',0,'p_V','fort.py',231),
  ('Rid -> id','Rid',1,'p_Rid','fort.py',237),
  ('Rid -> Rid coma id','Rid',3,'p_Rid','fort.py',238),
  ('Tipo -> integer','Tipo',1,'p_Tipo','fort.py',250),
  ('Tipo -> real','Tipo',1,'p_Tipo','fort.py',251),
  ('Dim -> openBra int action_30 closedBra','Dim',4,'p_Dim','fort.py',259),
  ('Dim -> openBra int action_30 closedBra openBra int action_31 closedBra','Dim',8,'p_Dim','fort.py',260),
  ('Dim -> <empty>','Dim',0,'p_Dim','fort.py',261),
  ('F -> F subroutine id action_39 B end subroutine action_40','F',8,'p_F','fort.py',267),
  ('F -> <empty>','F',0,'p_F','fort.py',268),
  ('B -> B S','B',2,'p_B','fort.py',274),
  ('B -> <empty>','B',0,'p_B','fort.py',275),
  ('S -> Dimensional equals EA action_8','S',4,'p_S','fort.py',281),
  ('S -> id parens action_41','S',3,'p_S','fort.py',282),
  ('S -> read RDimensional','S',2,'p_S','fort.py',283),
  ('S -> print RDimOrString','S',2,'p_S','fort.py',284),
  ('S -> if action_16 Relif ElseOrEmpty end if action_20','S',7,'p_S','fort.py',285),
  ('S -> do id action_24 equals EA action_25 coma EA action_26 IntOrEmpty then B action_29 end do','S',15,'p_S','fort.py',286),
  ('S -> do then action_21 B action_22 end do','S',7,'p_S','fort.py',287),
  ('S -> swap Dimensional coma Dimensional','S',4,'p_S','fort.py',288),
  ('S -> exit action_23','S',2,'p_S','fort.py',289),
  ('Dimensional -> id DimensionsOrEmpty action_1','Dimensional',3,'p_Dimensional','fort.py',297),
  ('DimensionsOrEmpty -> openParen EA action_setDim1 ComaEAOrEmpty closedParen','DimensionsOrEmpty',5,'p_DimensionsOrEmpty','fort.py',304),
  ('DimensionsOrEmpty -> <empty>','DimensionsOrEmpty',0,'p_DimensionsOrEmpty','fort.py',305),
  ('ComaEAOrEmpty -> coma EA action_setDim2','ComaEAOrEmpty',3,'p_ComaEAOrEmpty','fort.py',311),
  ('ComaEAOrEmpty -> <empty>','ComaEAOrEmpty',0,'p_ComaEAOrEmpty','fort.py',312),
  ('RDimensional -> Dimensional action_36','RDimensional',2,'p_RDimensional','fort.py',318),
  ('RDimensional -> RDimensional coma Dimensional action_36','RDimensional',4,'p_RDimensional','fort.py',319),
  ('RDimOrString -> DimOrString','RDimOrString',1,'p_RDimOrString','fort.py',325),
  ('RDimOrString -> RDimOrString coma DimOrString','RDimOrString',3,'p_RDimOrString','fort.py',326),
  ('DimOrString -> Dimensional action_33','DimOrString',2,'p_DimOrString','fort.py',332),
  ('DimOrString -> string action_34','DimOrString',2,'p_DimOrString','fort.py',333),
  ('DimOrString -> endline action_34','DimOrString',2,'p_DimOrString','fort.py',334),
  ('Relif -> openParen EL closedParen action_17 then B','Relif',6,'p_Relif','fort.py',340),
  ('Relif -> Relif elif action_18 openParen EL closedParen action_17 then B','Relif',9,'p_Relif','fort.py',341),
  ('ElseOrEmpty -> else action_19 B','ElseOrEmpty',3,'p_ElseOrEmpty','fort.py',347),
  ('ElseOrEmpty -> <empty>','ElseOrEmpty',0,'p_ElseOrEmpty','fort.py',348),
  ('IntOrEmpty -> coma int action_28','IntOrEmpty',3,'p_IntOrEmpty','fort.py',354),
  ('IntOrEmpty -> action_27','IntOrEmpty',1,'p_IntOrEmpty','fort.py',355),
  ('EA -> MultDiv','EA',1,'p_EA','fort.py',361),
  ('EA -> EA SumOrSub action_3 MultDiv action_4','EA',5,'p_EA','fort.py',362),
  ('SumOrSub -> plus','SumOrSub',1,'p_SumOrSub','fort.py',368),
  ('SumOrSub -> minus','SumOrSub',1,'p_SumOrSub','fort.py',369),
  ('MultDiv -> EAParens','MultDiv',1,'p_MultDiv','fort.py',376),
  ('MultDiv -> MultDiv MDSymbols action_5 EAParens action_6','MultDiv',5,'p_MultDiv','fort.py',377),
  ('MDSymbols -> mul','MDSymbols',1,'p_MDSymbols','fort.py',383),
  ('MDSymbols -> div','MDSymbols',1,'p_MDSymbols','fort.py',384),
  ('EAParens -> EItem','EAParens',1,'p_EAParens','fort.py',391),
  ('EAParens -> openParen EA closedParen','EAParens',3,'p_EAParens','fort.py',392),
  ('EL -> AND','EL',1,'p_EL','fort.py',398),
  ('EL -> EL or action_10 AND action_9','EL',5,'p_EL','fort.py',399),
  ('AND -> Equality','AND',1,'p_AND','fort.py',405),
  ('AND -> AND and action_12 Equality action_11','AND',5,'p_AND','fort.py',406),
  ('Equality -> EItem EQSymbols action_13 EItem action_14','Equality',5,'p_Equality','fort.py',412),
  ('Equality -> openParen EL closedParen','Equality',3,'p_Equality','fort.py',413),
  ('Equality -> not EL action_15','Equality',3,'p_Equality','fort.py',414),
  ('EItem -> Dimensional','EItem',1,'p_EItem','fort.py',420),
  ('EItem -> int action_2','EItem',2,'p_EItem','fort.py',421),
  ('EItem -> rea action_2_rea','EItem',2,'p_EItem','fort.py',422),
  ('EQSymbols -> less','EQSymbols',1,'p_EQSymbols','fort.py',428),
  ('EQSymbols -> more','EQSymbols',1,'p_EQSymbols','fort.py',429),
  ('EQSymbols -> doubleEquals','EQSymbols',1,'p_EQSymbols','fort.py',430),
  ('EQSymbols -> notEquals','EQSymbols',1,'p_EQSymbols','fort.py',431),
  ('EQSymbols -> lessEquals','EQSymbols',1,'p_EQSymbols','fort.py',432),
  ('EQSymbols -> moreEquals','EQSymbols',1,'p_EQSymbols','fort.py',433),
  ('action_addSymbols -> <empty>','action_addSymbols',0,'p_action_addSymbols','fort.py',443),
  ('action_1 -> <empty>','action_1',0,'p_action_1','fort.py',449),
  ('action_2 -> <empty>','action_2',0,'p_action_2','fort.py',497),
  ('action_2_rea -> <empty>','action_2_rea',0,'p_action_2_rea','fort.py',503),
  ('action_3 -> <empty>','action_3',0,'p_action_3','fort.py',509),
  ('action_4 -> <empty>','action_4',0,'p_action_4','fort.py',514),
  ('action_5 -> <empty>','action_5',0,'p_action_5','fort.py',537),
  ('action_6 -> <empty>','action_6',0,'p_action_6','fort.py',542),
  ('action_8 -> <empty>','action_8',0,'p_action_8','fort.py',565),
  ('action_9 -> <empty>','action_9',0,'p_action_9','fort.py',585),
  ('action_10 -> <empty>','action_10',0,'p_action_10','fort.py',608),
  ('action_11 -> <empty>','action_11',0,'p_action_11','fort.py',613),
  ('action_12 -> <empty>','action_12',0,'p_action_12','fort.py',636),
  ('action_13 -> <empty>','action_13',0,'p_action_13','fort.py',641),
  ('action_14 -> <empty>','action_14',0,'p_action_14','fort.py',646),
  ('action_15 -> <empty>','action_15',0,'p_action_15','fort.py',669),
  ('action_16 -> <empty>','action_16',0,'p_action_16','fort.py',684),
  ('action_17 -> <empty>','action_17',0,'p_action_17','fort.py',689),
  ('action_18 -> <empty>','action_18',0,'p_action_18','fort.py',705),
  ('action_19 -> <empty>','action_19',0,'p_action_19','fort.py',715),
  ('action_20 -> <empty>','action_20',0,'p_action_20','fort.py',725),
  ('action_21 -> <empty>','action_21',0,'p_action_21','fort.py',733),
  ('action_22 -> <empty>','action_22',0,'p_action_22','fort.py',739),
  ('action_23 -> <empty>','action_23',0,'p_action_23','fort.py',752),
  ('action_24 -> <empty>','action_24',0,'p_action_24','fort.py',761),
  ('action_25 -> <empty>','action_25',0,'p_action_25','fort.py',775),
  ('action_26 -> <empty>','action_26',0,'p_action_26','fort.py',793),
  ('action_27 -> <empty>','action_27',0,'p_action_27','fort.py',819),
  ('action_28 -> <empty>','action_28',0,'p_action_28','fort.py',825),
  ('action_29 -> <empty>','action_29',0,'p_action_29','fort.py',831),
  ('action_30 -> <empty>','action_30',0,'p_action_30','fort.py',855),
  ('action_31 -> <empty>','action_31',0,'p_action_31','fort.py',863),
  ('action_32 -> <empty>','action_32',0,'p_action_32','fort.py',871),
  ('action_33 -> <empty>','action_33',0,'p_action_33','fort.py',881),
  ('action_34 -> <empty>','action_34',0,'p_action_34','fort.py',893),
  ('action_36 -> <empty>','action_36',0,'p_action_36','fort.py',900),
  ('action_37 -> <empty>','action_37',0,'p_action_37','fort.py',909),
  ('action_38 -> <empty>','action_38',0,'p_action_38','fort.py',916),
  ('action_39 -> <empty>','action_39',0,'p_action_39','fort.py',922),
  ('action_40 -> <empty>','action_40',0,'p_action_40','fort.py',929),
  ('action_41 -> <empty>','action_41',0,'p_action_41','fort.py',936),
  ('action_setDim1 -> <empty>','action_setDim1',0,'p_action_setDim1','fort.py',948),
  ('action_setDim2 -> <empty>','action_setDim2',0,'p_action_setDim2','fort.py',959),
]
