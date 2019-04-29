
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'and closedBra closedParen coma div do doubleColon doubleEquals elif else end endline equals exit id if int integer less lessEquals minus more moreEquals mul not notEquals openBra openParen or parens plus print program rea read real string subroutine swap then\n    programa : program id V F B end program\n    \n    V : V Tipo Dim doubleColon Rid action_addSymbols action_32\n      |\n    \n    Rid : id\n       | Rid coma id\n    \n    Tipo : integer\n         | real\n    \n    Dim : openBra int action_30 closedBra\n        | openBra int action_30 closedBra openBra int action_31 closedBra\n        |\n    \n    F : F subroutine id B end subroutine\n      |\n    \n    B : B S\n      |\n    \n    S : Dimensional action_7 equals EA action_8\n      | id parens\n      | read RDimensional\n      | print RDimOrString\n      | if action_16 Relif ElseOrEmpty end if action_20\n      | do id action_24 equals EA action_25 coma EA action_26 IntOrEmpty then B action_29 end do\n      | do then action_21 B action_22 end do\n      | swap Dimensional coma Dimensional\n      | exit action_23 \n      | id openParen closedParen\n    \n    Dimensional : id DimensionsOrEmpty\n    \n    DimensionsOrEmpty : openParen EA action_setDim1 ComaEAOrEmpty closedParen\n                      |\n    \n    ComaEAOrEmpty : coma EA action_setDim2\n                  |\n    \n    RDimensional : Dimensional action_1 action_36\n                 | RDimensional coma Dimensional action_1 action_36\n    \n    RDimOrString : DimOrString\n                 | RDimOrString coma DimOrString\n    \n    DimOrString : Dimensional action_1 action_33\n                | string action_34\n                | endline action_34\n    \n    Relif : openParen EL closedParen action_17 then B\n          | Relif elif action_18 openParen EL closedParen action_17 then B\n    \n    ElseOrEmpty : else action_19 B\n                |\n    \n    IntOrEmpty : coma int action_28\n               | action_27\n    \n    EA : MultDiv\n       | EA SumOrSub action_3 MultDiv action_4\n    \n    SumOrSub : plus\n             | minus\n    \n    MultDiv : EAParens\n            | MultDiv MDSymbols action_5 EAParens action_6\n    \n    MDSymbols : mul\n              | div\n    \n    EAParens : EItem\n             | openParen EA closedParen\n    \n    EL : AND\n       | EL or action_10 AND action_9\n    \n    AND : Equality\n        | AND and action_12 Equality action_11\n    \n    Equality : EItem EQSymbols action_13 EItem action_14\n             | openParen EL closedParen\n             | not EL action_15\n    \n    EItem : Dimensional action_1\n          | int action_2\n          | rea action_2_rea\n    \n    EQSymbols : less\n              | more\n              | doubleEquals\n              | notEquals\n              | lessEquals\n              | moreEquals\n    action_addSymbols :action_1 :action_2 :action_2_rea :action_3 :action_4 :action_5 :action_6 :action_7 :action_8 :action_9 :action_10 :action_11 :action_12 :action_13 :action_14 :action_15 :action_16 :action_17 :action_18 :action_19 :action_20 :action_21 :action_22 :action_23 :action_24 :action_25 :action_26 :action_27 :action_28 :action_29 :action_30 :action_31 :action_32 :action_33 :action_34 :action_36 :action_setDim1 :action_setDim2 :'
    
_lr_action_items = {'program':([0,14,],[2,29,]),'$end':([1,29,],[0,-1,]),'id':([2,3,4,5,9,10,15,17,18,20,21,22,23,24,26,27,28,31,32,33,34,35,36,37,38,41,43,44,45,46,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,68,69,71,72,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,98,99,100,101,102,103,104,106,108,109,110,111,112,115,118,119,120,121,122,123,124,125,126,131,133,134,135,136,137,138,141,142,143,149,150,151,153,157,158,161,168,172,174,176,179,],[3,-3,-12,-14,13,23,-13,33,33,40,33,-93,-14,46,-16,33,-25,-17,-70,-27,-18,-32,-70,-104,-104,-91,-23,13,-69,-4,33,-24,-43,-47,-51,-70,-71,-72,33,33,-105,33,33,-103,-35,-36,33,-14,33,-102,104,-73,-45,-46,-75,-49,-50,-60,-61,-62,-78,-70,-30,-33,-34,-89,33,33,33,13,-22,-11,-2,-5,-52,33,33,33,-15,-105,-14,-80,-82,-83,-63,-64,-65,-66,-67,-68,-26,-74,-76,-31,-90,33,13,33,33,33,-44,-48,-19,-14,33,-21,13,-14,13,-14,13,-20,]),'integer':([3,4,45,46,71,103,104,],[-3,7,-69,-4,-102,-2,-5,]),'real':([3,4,45,46,71,103,104,],[-3,8,-69,-4,-102,-2,-5,]),'subroutine':([3,4,5,45,46,70,71,102,103,104,],[-3,-12,10,-69,-4,102,-102,-11,-2,-5,]),'end':([3,4,5,9,15,22,23,26,28,31,32,33,34,35,36,37,38,41,43,44,45,46,49,51,52,53,54,55,56,59,62,63,64,65,68,71,82,83,84,85,86,87,88,89,90,92,100,101,102,103,104,106,111,112,115,129,131,133,134,135,136,138,149,150,151,153,158,161,168,172,174,176,177,179,],[-3,-12,-14,14,-13,-93,-14,-16,-25,-17,-70,-27,-18,-32,-70,-104,-104,-91,-23,70,-69,-4,-24,-43,-47,-51,-70,-71,-72,-105,-103,-35,-36,-40,-14,-102,-60,-61,-62,-78,-70,-30,-33,-34,113,-89,-92,-22,-11,-2,-5,-52,-15,-105,-14,146,-26,-74,-76,-31,-90,-39,-44,-48,-19,-14,-21,-37,-14,-38,-14,-99,178,-20,]),'read':([3,4,5,9,15,22,23,26,28,31,32,33,34,35,36,37,38,41,43,44,45,46,49,51,52,53,54,55,56,59,62,63,64,68,71,82,83,84,85,86,87,88,89,92,100,101,102,103,104,106,111,112,115,131,133,134,135,136,138,149,150,151,153,158,161,168,172,174,176,179,],[-3,-12,-14,17,-13,-93,-14,-16,-25,-17,-70,-27,-18,-32,-70,-104,-104,-91,-23,17,-69,-4,-24,-43,-47,-51,-70,-71,-72,-105,-103,-35,-36,-14,-102,-60,-61,-62,-78,-70,-30,-33,-34,-89,17,-22,-11,-2,-5,-52,-15,-105,-14,-26,-74,-76,-31,-90,17,-44,-48,-19,-14,-21,17,-14,17,-14,17,-20,]),'print':([3,4,5,9,15,22,23,26,28,31,32,33,34,35,36,37,38,41,43,44,45,46,49,51,52,53,54,55,56,59,62,63,64,68,71,82,83,84,85,86,87,88,89,92,100,101,102,103,104,106,111,112,115,131,133,134,135,136,138,149,150,151,153,158,161,168,172,174,176,179,],[-3,-12,-14,18,-13,-93,-14,-16,-25,-17,-70,-27,-18,-32,-70,-104,-104,-91,-23,18,-69,-4,-24,-43,-47,-51,-70,-71,-72,-105,-103,-35,-36,-14,-102,-60,-61,-62,-78,-70,-30,-33,-34,-89,18,-22,-11,-2,-5,-52,-15,-105,-14,-26,-74,-76,-31,-90,18,-44,-48,-19,-14,-21,18,-14,18,-14,18,-20,]),'if':([3,4,5,9,15,22,23,26,28,31,32,33,34,35,36,37,38,41,43,44,45,46,49,51,52,53,54,55,56,59,62,63,64,68,71,82,83,84,85,86,87,88,89,92,100,101,102,103,104,106,111,112,113,115,131,133,134,135,136,138,149,150,151,153,158,161,168,172,174,176,179,],[-3,-12,-14,19,-13,-93,-14,-16,-25,-17,-70,-27,-18,-32,-70,-104,-104,-91,-23,19,-69,-4,-24,-43,-47,-51,-70,-71,-72,-105,-103,-35,-36,-14,-102,-60,-61,-62,-78,-70,-30,-33,-34,-89,19,-22,-11,-2,-5,-52,-15,-105,136,-14,-26,-74,-76,-31,-90,19,-44,-48,-19,-14,-21,19,-14,19,-14,19,-20,]),'do':([3,4,5,9,15,22,23,26,28,31,32,33,34,35,36,37,38,41,43,44,45,46,49,51,52,53,54,55,56,59,62,63,64,68,71,82,83,84,85,86,87,88,89,92,100,101,102,103,104,106,111,112,115,131,133,134,135,136,138,146,149,150,151,153,158,161,168,172,174,176,178,179,],[-3,-12,-14,20,-13,-93,-14,-16,-25,-17,-70,-27,-18,-32,-70,-104,-104,-91,-23,20,-69,-4,-24,-43,-47,-51,-70,-71,-72,-105,-103,-35,-36,-14,-102,-60,-61,-62,-78,-70,-30,-33,-34,-89,20,-22,-11,-2,-5,-52,-15,-105,-14,-26,-74,-76,-31,-90,20,158,-44,-48,-19,-14,-21,20,-14,20,-14,20,179,-20,]),'swap':([3,4,5,9,15,22,23,26,28,31,32,33,34,35,36,37,38,41,43,44,45,46,49,51,52,53,54,55,56,59,62,63,64,68,71,82,83,84,85,86,87,88,89,92,100,101,102,103,104,106,111,112,115,131,133,134,135,136,138,149,150,151,153,158,161,168,172,174,176,179,],[-3,-12,-14,21,-13,-93,-14,-16,-25,-17,-70,-27,-18,-32,-70,-104,-104,-91,-23,21,-69,-4,-24,-43,-47,-51,-70,-71,-72,-105,-103,-35,-36,-14,-102,-60,-61,-62,-78,-70,-30,-33,-34,-89,21,-22,-11,-2,-5,-52,-15,-105,-14,-26,-74,-76,-31,-90,21,-44,-48,-19,-14,-21,21,-14,21,-14,21,-20,]),'exit':([3,4,5,9,15,22,23,26,28,31,32,33,34,35,36,37,38,41,43,44,45,46,49,51,52,53,54,55,56,59,62,63,64,68,71,82,83,84,85,86,87,88,89,92,100,101,102,103,104,106,111,112,115,131,133,134,135,136,138,149,150,151,153,158,161,168,172,174,176,179,],[-3,-12,-14,22,-13,-93,-14,-16,-25,-17,-70,-27,-18,-32,-70,-104,-104,-91,-23,22,-69,-4,-24,-43,-47,-51,-70,-71,-72,-105,-103,-35,-36,-14,-102,-60,-61,-62,-78,-70,-30,-33,-34,-89,22,-22,-11,-2,-5,-52,-15,-105,-14,-26,-74,-76,-31,-90,22,-44,-48,-19,-14,-21,22,-14,22,-14,22,-20,]),'openBra':([6,7,8,73,],[12,-6,-7,105,]),'doubleColon':([6,7,8,11,73,159,],[-10,-6,-7,24,-8,-9,]),'int':([12,27,48,57,60,66,76,77,78,79,80,81,93,98,99,105,108,109,110,118,119,120,121,122,123,124,125,126,137,141,142,143,157,169,],[25,55,55,55,55,55,-73,-45,-46,-75,-49,-50,55,55,55,130,55,55,55,-80,-82,-83,-63,-64,-65,-66,-67,-68,55,55,55,55,55,173,]),'parens':([13,],[26,]),'openParen':([13,19,27,33,39,48,57,60,66,76,77,78,79,80,81,91,93,98,99,108,109,110,114,118,119,137,141,142,157,],[27,-86,48,60,66,48,48,48,93,-73,-45,-46,-75,-49,-50,-88,93,93,48,48,48,48,137,-80,-82,93,93,93,48,]),'equals':([13,16,28,30,40,67,131,],[-27,-77,-25,57,-94,99,-26,]),'elif':([15,22,26,28,31,32,33,34,35,36,37,38,43,49,51,52,53,54,55,56,59,62,63,64,65,82,83,84,85,86,87,88,89,101,106,111,112,131,133,134,135,136,149,150,151,153,158,161,168,172,179,],[-13,-93,-16,-25,-17,-70,-27,-18,-32,-70,-104,-104,-23,-24,-43,-47,-51,-70,-71,-72,-105,-103,-35,-36,91,-60,-61,-62,-78,-70,-30,-33,-34,-22,-52,-15,-105,-26,-74,-76,-31,-90,-44,-48,-19,-14,-21,-37,-14,-38,-20,]),'else':([15,22,26,28,31,32,33,34,35,36,37,38,43,49,51,52,53,54,55,56,59,62,63,64,65,82,83,84,85,86,87,88,89,101,106,111,112,131,133,134,135,136,149,150,151,153,158,161,168,172,179,],[-13,-93,-16,-25,-17,-70,-27,-18,-32,-70,-104,-104,-23,-24,-43,-47,-51,-70,-71,-72,-105,-103,-35,-36,92,-60,-61,-62,-78,-70,-30,-33,-34,-22,-52,-15,-105,-26,-74,-76,-31,-90,-44,-48,-19,-14,-21,-37,-14,-38,-20,]),'string':([18,61,],[37,37,]),'endline':([18,61,],[38,38,]),'then':([20,28,33,51,52,53,54,55,56,82,83,84,106,117,131,133,134,140,149,150,160,165,166,167,170,171,173,175,],[41,-25,-27,-43,-47,-51,-70,-71,-72,-60,-61,-62,-52,-87,-26,-74,-76,153,-44,-48,-87,-96,168,-97,174,-42,-98,-41,]),'closedBra':([25,47,130,147,],[-100,73,-101,159,]),'closedParen':([27,28,33,50,51,52,53,54,55,56,74,75,82,83,84,94,95,96,106,107,116,127,131,132,133,134,139,144,148,149,150,152,154,155,156,162,163,164,],[49,-25,-27,-106,-43,-47,-51,-70,-71,-72,106,-29,-60,-61,-62,117,-53,-55,-52,131,139,-85,-26,-107,-74,-76,-58,-59,-28,-44,-48,160,-79,-81,-84,-54,-56,-57,]),'rea':([27,48,57,60,66,76,77,78,79,80,81,93,98,99,108,109,110,118,119,120,121,122,123,124,125,126,137,141,142,143,157,],[56,56,56,56,56,-73,-45,-46,-75,-49,-50,56,56,56,56,56,56,-80,-82,-83,-63,-64,-65,-66,-67,-68,56,56,56,56,56,]),'coma':([28,31,32,33,34,35,36,37,38,42,45,46,50,51,52,53,54,55,56,59,62,63,64,75,82,83,84,86,87,88,89,104,106,112,128,131,133,134,135,145,149,150,165,167,],[-25,58,-70,-27,61,-32,-70,-104,-104,69,72,-4,-106,-43,-47,-51,-70,-71,-72,-105,-103,-35,-36,108,-60,-61,-62,-70,-30,-33,-34,-5,-52,-105,-95,-26,-74,-76,-31,157,-44,-48,-96,169,]),'mul':([28,33,51,52,53,54,55,56,82,83,84,106,131,133,134,150,],[-25,-27,80,-47,-51,-70,-71,-72,-60,-61,-62,-52,-26,80,-76,-48,]),'div':([28,33,51,52,53,54,55,56,82,83,84,106,131,133,134,150,],[-25,-27,81,-47,-51,-70,-71,-72,-60,-61,-62,-52,-26,81,-76,-48,]),'plus':([28,33,50,51,52,53,54,55,56,74,82,83,84,85,106,128,131,132,133,134,149,150,165,],[-25,-27,77,-43,-47,-51,-70,-71,-72,77,-60,-61,-62,77,-52,77,-26,77,-74,-76,-44,-48,77,]),'minus':([28,33,50,51,52,53,54,55,56,74,82,83,84,85,106,128,131,132,133,134,149,150,165,],[-25,-27,78,-43,-47,-51,-70,-71,-72,78,-60,-61,-62,78,-52,78,-26,78,-74,-76,-44,-48,78,]),'less':([28,33,54,55,56,82,83,84,97,131,],[-25,-27,-70,-71,-72,-60,-61,-62,121,-26,]),'more':([28,33,54,55,56,82,83,84,97,131,],[-25,-27,-70,-71,-72,-60,-61,-62,122,-26,]),'doubleEquals':([28,33,54,55,56,82,83,84,97,131,],[-25,-27,-70,-71,-72,-60,-61,-62,123,-26,]),'notEquals':([28,33,54,55,56,82,83,84,97,131,],[-25,-27,-70,-71,-72,-60,-61,-62,124,-26,]),'lessEquals':([28,33,54,55,56,82,83,84,97,131,],[-25,-27,-70,-71,-72,-60,-61,-62,125,-26,]),'moreEquals':([28,33,54,55,56,82,83,84,97,131,],[-25,-27,-70,-71,-72,-60,-61,-62,126,-26,]),'and':([28,33,54,55,56,82,83,84,95,96,127,131,139,144,154,155,156,162,163,164,],[-25,-27,-70,-71,-72,-60,-61,-62,119,-55,-85,-26,-58,-59,119,-81,-84,-54,-56,-57,]),'or':([28,33,54,55,56,82,83,84,94,95,96,116,127,131,139,144,152,154,155,156,162,163,164,],[-25,-27,-70,-71,-72,-60,-61,-62,118,-53,-55,118,118,-26,-58,-59,118,-79,-81,-84,-54,-56,-57,]),'not':([66,93,98,118,119,137,141,142,],[98,98,98,-80,-82,98,98,98,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'V':([3,],[4,]),'F':([4,],[5,]),'Tipo':([4,],[6,]),'B':([5,23,68,115,153,168,174,],[9,44,100,138,161,172,176,]),'Dim':([6,],[11,]),'S':([9,44,100,138,161,172,176,],[15,15,15,15,15,15,15,]),'Dimensional':([9,17,18,21,27,44,48,57,58,60,61,66,69,93,98,99,100,108,109,110,137,138,141,142,143,157,161,172,176,],[16,32,36,42,54,16,54,54,86,54,36,54,101,54,54,54,16,54,54,54,54,16,54,54,54,54,16,16,16,]),'DimensionsOrEmpty':([13,33,],[28,28,]),'action_7':([16,],[30,]),'RDimensional':([17,],[31,]),'RDimOrString':([18,],[34,]),'DimOrString':([18,61,],[35,88,]),'action_16':([19,],[39,]),'action_23':([22,],[43,]),'Rid':([24,],[45,]),'action_30':([25,],[47,]),'EA':([27,48,57,60,99,108,157,],[50,74,85,50,128,132,165,]),'MultDiv':([27,48,57,60,99,108,109,157,],[51,51,51,51,51,51,133,51,]),'EAParens':([27,48,57,60,99,108,109,110,157,],[52,52,52,52,52,52,52,134,52,]),'EItem':([27,48,57,60,66,93,98,99,108,109,110,137,141,142,143,157,],[53,53,53,53,97,97,97,53,53,53,53,97,97,97,156,53,]),'action_1':([32,36,54,86,],[59,62,82,112,]),'action_34':([37,38,],[63,64,]),'Relif':([39,],[65,]),'action_24':([40,],[67,]),'action_21':([41,],[68,]),'action_addSymbols':([45,],[71,]),'action_setDim1':([50,],[75,]),'SumOrSub':([50,74,85,128,132,165,],[76,76,76,76,76,76,]),'MDSymbols':([51,133,],[79,79,]),'action_2':([55,],[83,]),'action_2_rea':([56,],[84,]),'action_36':([59,112,],[87,135,]),'action_33':([62,],[89,]),'ElseOrEmpty':([65,],[90,]),'EL':([66,93,98,137,],[94,116,127,152,]),'AND':([66,93,98,137,141,],[95,95,95,95,154,]),'Equality':([66,93,98,137,141,142,],[96,96,96,96,96,155,]),'action_32':([71,],[103,]),'ComaEAOrEmpty':([75,],[107,]),'action_3':([76,],[109,]),'action_5':([79,],[110,]),'action_8':([85,],[111,]),'action_18':([91,],[114,]),'action_19':([92,],[115,]),'EQSymbols':([97,],[120,]),'action_22':([100,],[129,]),'action_17':([117,160,],[140,166,]),'action_10':([118,],[141,]),'action_12':([119,],[142,]),'action_13':([120,],[143,]),'action_15':([127,],[144,]),'action_25':([128,],[145,]),'action_31':([130,],[147,]),'action_setDim2':([132,],[148,]),'action_4':([133,],[149,]),'action_6':([134,],[150,]),'action_20':([136,],[151,]),'action_9':([154,],[162,]),'action_11':([155,],[163,]),'action_14':([156,],[164,]),'action_26':([165,],[167,]),'IntOrEmpty':([167,],[170,]),'action_27':([167,],[171,]),'action_28':([173,],[175,]),'action_29':([176,],[177,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> program id V F B end program','programa',7,'p_programa','fort.py',226),
  ('V -> V Tipo Dim doubleColon Rid action_addSymbols action_32','V',7,'p_V','fort.py',233),
  ('V -> <empty>','V',0,'p_V','fort.py',234),
  ('Rid -> id','Rid',1,'p_Rid','fort.py',240),
  ('Rid -> Rid coma id','Rid',3,'p_Rid','fort.py',241),
  ('Tipo -> integer','Tipo',1,'p_Tipo','fort.py',253),
  ('Tipo -> real','Tipo',1,'p_Tipo','fort.py',254),
  ('Dim -> openBra int action_30 closedBra','Dim',4,'p_Dim','fort.py',262),
  ('Dim -> openBra int action_30 closedBra openBra int action_31 closedBra','Dim',8,'p_Dim','fort.py',263),
  ('Dim -> <empty>','Dim',0,'p_Dim','fort.py',264),
  ('F -> F subroutine id B end subroutine','F',6,'p_F','fort.py',270),
  ('F -> <empty>','F',0,'p_F','fort.py',271),
  ('B -> B S','B',2,'p_B','fort.py',277),
  ('B -> <empty>','B',0,'p_B','fort.py',278),
  ('S -> Dimensional action_7 equals EA action_8','S',5,'p_S','fort.py',284),
  ('S -> id parens','S',2,'p_S','fort.py',285),
  ('S -> read RDimensional','S',2,'p_S','fort.py',286),
  ('S -> print RDimOrString','S',2,'p_S','fort.py',287),
  ('S -> if action_16 Relif ElseOrEmpty end if action_20','S',7,'p_S','fort.py',288),
  ('S -> do id action_24 equals EA action_25 coma EA action_26 IntOrEmpty then B action_29 end do','S',15,'p_S','fort.py',289),
  ('S -> do then action_21 B action_22 end do','S',7,'p_S','fort.py',290),
  ('S -> swap Dimensional coma Dimensional','S',4,'p_S','fort.py',291),
  ('S -> exit action_23','S',2,'p_S','fort.py',292),
  ('S -> id openParen closedParen','S',3,'p_S','fort.py',293),
  ('Dimensional -> id DimensionsOrEmpty','Dimensional',2,'p_Dimensional','fort.py',301),
  ('DimensionsOrEmpty -> openParen EA action_setDim1 ComaEAOrEmpty closedParen','DimensionsOrEmpty',5,'p_DimensionsOrEmpty','fort.py',308),
  ('DimensionsOrEmpty -> <empty>','DimensionsOrEmpty',0,'p_DimensionsOrEmpty','fort.py',309),
  ('ComaEAOrEmpty -> coma EA action_setDim2','ComaEAOrEmpty',3,'p_ComaEAOrEmpty','fort.py',315),
  ('ComaEAOrEmpty -> <empty>','ComaEAOrEmpty',0,'p_ComaEAOrEmpty','fort.py',316),
  ('RDimensional -> Dimensional action_1 action_36','RDimensional',3,'p_RDimensional','fort.py',322),
  ('RDimensional -> RDimensional coma Dimensional action_1 action_36','RDimensional',5,'p_RDimensional','fort.py',323),
  ('RDimOrString -> DimOrString','RDimOrString',1,'p_RDimOrString','fort.py',329),
  ('RDimOrString -> RDimOrString coma DimOrString','RDimOrString',3,'p_RDimOrString','fort.py',330),
  ('DimOrString -> Dimensional action_1 action_33','DimOrString',3,'p_DimOrString','fort.py',336),
  ('DimOrString -> string action_34','DimOrString',2,'p_DimOrString','fort.py',337),
  ('DimOrString -> endline action_34','DimOrString',2,'p_DimOrString','fort.py',338),
  ('Relif -> openParen EL closedParen action_17 then B','Relif',6,'p_Relif','fort.py',344),
  ('Relif -> Relif elif action_18 openParen EL closedParen action_17 then B','Relif',9,'p_Relif','fort.py',345),
  ('ElseOrEmpty -> else action_19 B','ElseOrEmpty',3,'p_ElseOrEmpty','fort.py',351),
  ('ElseOrEmpty -> <empty>','ElseOrEmpty',0,'p_ElseOrEmpty','fort.py',352),
  ('IntOrEmpty -> coma int action_28','IntOrEmpty',3,'p_IntOrEmpty','fort.py',358),
  ('IntOrEmpty -> action_27','IntOrEmpty',1,'p_IntOrEmpty','fort.py',359),
  ('EA -> MultDiv','EA',1,'p_EA','fort.py',365),
  ('EA -> EA SumOrSub action_3 MultDiv action_4','EA',5,'p_EA','fort.py',366),
  ('SumOrSub -> plus','SumOrSub',1,'p_SumOrSub','fort.py',372),
  ('SumOrSub -> minus','SumOrSub',1,'p_SumOrSub','fort.py',373),
  ('MultDiv -> EAParens','MultDiv',1,'p_MultDiv','fort.py',380),
  ('MultDiv -> MultDiv MDSymbols action_5 EAParens action_6','MultDiv',5,'p_MultDiv','fort.py',381),
  ('MDSymbols -> mul','MDSymbols',1,'p_MDSymbols','fort.py',387),
  ('MDSymbols -> div','MDSymbols',1,'p_MDSymbols','fort.py',388),
  ('EAParens -> EItem','EAParens',1,'p_EAParens','fort.py',395),
  ('EAParens -> openParen EA closedParen','EAParens',3,'p_EAParens','fort.py',396),
  ('EL -> AND','EL',1,'p_EL','fort.py',402),
  ('EL -> EL or action_10 AND action_9','EL',5,'p_EL','fort.py',403),
  ('AND -> Equality','AND',1,'p_AND','fort.py',409),
  ('AND -> AND and action_12 Equality action_11','AND',5,'p_AND','fort.py',410),
  ('Equality -> EItem EQSymbols action_13 EItem action_14','Equality',5,'p_Equality','fort.py',416),
  ('Equality -> openParen EL closedParen','Equality',3,'p_Equality','fort.py',417),
  ('Equality -> not EL action_15','Equality',3,'p_Equality','fort.py',418),
  ('EItem -> Dimensional action_1','EItem',2,'p_EItem','fort.py',424),
  ('EItem -> int action_2','EItem',2,'p_EItem','fort.py',425),
  ('EItem -> rea action_2_rea','EItem',2,'p_EItem','fort.py',426),
  ('EQSymbols -> less','EQSymbols',1,'p_EQSymbols','fort.py',432),
  ('EQSymbols -> more','EQSymbols',1,'p_EQSymbols','fort.py',433),
  ('EQSymbols -> doubleEquals','EQSymbols',1,'p_EQSymbols','fort.py',434),
  ('EQSymbols -> notEquals','EQSymbols',1,'p_EQSymbols','fort.py',435),
  ('EQSymbols -> lessEquals','EQSymbols',1,'p_EQSymbols','fort.py',436),
  ('EQSymbols -> moreEquals','EQSymbols',1,'p_EQSymbols','fort.py',437),
  ('action_addSymbols -> <empty>','action_addSymbols',0,'p_action_addSymbols','fort.py',447),
  ('action_1 -> <empty>','action_1',0,'p_action_1','fort.py',453),
  ('action_2 -> <empty>','action_2',0,'p_action_2','fort.py',500),
  ('action_2_rea -> <empty>','action_2_rea',0,'p_action_2_rea','fort.py',506),
  ('action_3 -> <empty>','action_3',0,'p_action_3','fort.py',512),
  ('action_4 -> <empty>','action_4',0,'p_action_4','fort.py',517),
  ('action_5 -> <empty>','action_5',0,'p_action_5','fort.py',540),
  ('action_6 -> <empty>','action_6',0,'p_action_6','fort.py',545),
  ('action_7 -> <empty>','action_7',0,'p_action_7','fort.py',568),
  ('action_8 -> <empty>','action_8',0,'p_action_8','fort.py',615),
  ('action_9 -> <empty>','action_9',0,'p_action_9','fort.py',633),
  ('action_10 -> <empty>','action_10',0,'p_action_10','fort.py',656),
  ('action_11 -> <empty>','action_11',0,'p_action_11','fort.py',661),
  ('action_12 -> <empty>','action_12',0,'p_action_12','fort.py',684),
  ('action_13 -> <empty>','action_13',0,'p_action_13','fort.py',689),
  ('action_14 -> <empty>','action_14',0,'p_action_14','fort.py',694),
  ('action_15 -> <empty>','action_15',0,'p_action_15','fort.py',717),
  ('action_16 -> <empty>','action_16',0,'p_action_16','fort.py',732),
  ('action_17 -> <empty>','action_17',0,'p_action_17','fort.py',737),
  ('action_18 -> <empty>','action_18',0,'p_action_18','fort.py',753),
  ('action_19 -> <empty>','action_19',0,'p_action_19','fort.py',763),
  ('action_20 -> <empty>','action_20',0,'p_action_20','fort.py',773),
  ('action_21 -> <empty>','action_21',0,'p_action_21','fort.py',781),
  ('action_22 -> <empty>','action_22',0,'p_action_22','fort.py',787),
  ('action_23 -> <empty>','action_23',0,'p_action_23','fort.py',800),
  ('action_24 -> <empty>','action_24',0,'p_action_24','fort.py',809),
  ('action_25 -> <empty>','action_25',0,'p_action_25','fort.py',823),
  ('action_26 -> <empty>','action_26',0,'p_action_26','fort.py',841),
  ('action_27 -> <empty>','action_27',0,'p_action_27','fort.py',867),
  ('action_28 -> <empty>','action_28',0,'p_action_28','fort.py',873),
  ('action_29 -> <empty>','action_29',0,'p_action_29','fort.py',879),
  ('action_30 -> <empty>','action_30',0,'p_action_30','fort.py',903),
  ('action_31 -> <empty>','action_31',0,'p_action_31','fort.py',911),
  ('action_32 -> <empty>','action_32',0,'p_action_32','fort.py',919),
  ('action_33 -> <empty>','action_33',0,'p_action_33','fort.py',929),
  ('action_34 -> <empty>','action_34',0,'p_action_34','fort.py',938),
  ('action_36 -> <empty>','action_36',0,'p_action_36','fort.py',952),
  ('action_setDim1 -> <empty>','action_setDim1',0,'p_action_setDim1','fort.py',961),
  ('action_setDim2 -> <empty>','action_setDim2',0,'p_action_setDim2','fort.py',973),
]
