
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'and closedBra closedParen coma div do doubleColon doubleEquals elif else end equals exit id if int integer less lessEquals minus more moreEquals mul not notEquals openBra openParen or parens plus print program rea read real string subroutine swap then\n    programa : program id V F B end program\n    \n    V : V Tipo Dim doubleColon Rid\n      |\n    \n    Rid : id\n       | Rid coma id\n    \n    Tipo : integer\n         | real\n    \n    Dim : openBra int closedBra\n        | openBra int closedBra openBra int closedBra\n        |\n    \n    F : F subroutine id B end subroutine\n      |\n    \n    B : B S\n      |\n    \n    S : Dimensional action_7 equals EA action_8\n      | id parens\n      | read RDimensional\n      | print RDimOrString\n      | if Relif ElseOrEmpty end if\n      | do id equals EA coma EA IntOrEmpty then B end do\n      | do then B end do\n      | swap Dimensional coma Dimensional\n      | exit\n    \n    Dimensional : id DimensionsOrEmpty\n    \n    DimensionsOrEmpty : openParen EA ComaEAOrEmpty closedParen\n                      |\n    \n    ComaEAOrEmpty : coma EA\n                  |\n    \n    RDimensional : Dimensional\n                 | RDimensional coma Dimensional\n    \n    RDimOrString : DimOrString\n                 | RDimOrString coma DimOrString\n    \n    DimOrString : Dimensional\n                | string\n    \n    Relif : openParen EL closedParen then B\n          | Relif elif openParen EL closedParen then B\n    \n    ElseOrEmpty : else B\n                |\n    \n    IntOrEmpty : coma int\n               |\n    \n    EA : MultDiv\n       | EA SumOrSub action_3 MultDiv action_4\n    \n    SumOrSub : plus\n             | minus\n    \n    MultDiv : EAParens\n            | MultDiv MDSymbols action_5 EAParens action_6\n    \n    MDSymbols : mul\n              | div\n    \n    EAParens : EItem\n             | openParen EA closedParen\n    \n    EL : AND\n       | EL or AND\n    \n    AND : Equality\n        | AND and Equality\n    \n    Equality : EItem EQSymbols EItem\n             | openParen EL closedParen\n             | not EL\n    \n    EItem : Dimensional action_1\n          | int action_2\n          | rea action_2_rea\n    \n    EQSymbols : less\n              | more\n              | doubleEquals\n              | notEquals\n              | lessEquals\n              | moreEquals\n    action_1 :action_2 :action_2_rea :action_3 :action_4 :action_5 :action_6 :action_7 :action_8 :'
    
_lr_action_items = {'program':([0,14,],[2,29,]),'$end':([1,29,],[0,-1,]),'id':([2,3,4,5,9,10,15,17,18,20,21,22,23,24,26,27,28,31,32,33,34,35,36,37,39,41,43,44,45,47,49,50,51,52,53,54,55,56,57,60,61,66,67,68,69,71,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,93,94,95,96,97,98,99,100,101,105,106,107,109,110,111,113,114,115,118,122,123,125,126,128,130,131,132,135,137,138,140,],[3,-3,-12,-14,13,23,-13,33,33,40,33,-23,-14,45,-16,-24,33,-17,-29,-26,-18,-31,-33,-34,33,-14,13,-2,-4,33,-41,-45,-49,-67,-68,-69,33,33,33,-14,33,33,33,13,33,107,-70,33,-43,-44,-72,-47,-48,-58,-59,-60,-75,-30,-32,33,13,33,33,33,-61,-62,-63,-64,-65,-66,-22,-11,-5,-50,-25,33,33,-15,-19,-14,33,-21,-71,-73,13,-42,-46,-14,13,-14,13,-20,]),'integer':([3,4,44,45,107,],[-3,7,-2,-4,-5,]),'real':([3,4,44,45,107,],[-3,8,-2,-4,-5,]),'subroutine':([3,4,5,44,45,70,106,107,],[-3,-12,10,-2,-4,106,-11,-5,]),'end':([3,4,5,9,15,22,23,26,27,31,32,33,34,35,36,37,38,41,43,44,45,49,50,51,52,53,54,58,60,68,82,83,84,85,86,87,90,105,106,107,109,110,114,115,118,123,125,126,128,130,131,132,135,137,138,140,],[-3,-12,-14,14,-13,-23,-14,-16,-24,-17,-29,-26,-18,-31,-33,-34,-38,-14,70,-2,-4,-41,-45,-49,-67,-68,-69,88,-14,104,-58,-59,-60,-75,-30,-32,-37,-22,-11,-5,-50,-25,-15,-19,-14,-21,-71,-73,-35,-42,-46,-14,-36,-14,139,-20,]),'read':([3,4,5,9,15,22,23,26,27,31,32,33,34,35,36,37,41,43,44,45,49,50,51,52,53,54,60,68,82,83,84,85,86,87,90,105,106,107,109,110,114,115,118,123,125,126,128,130,131,132,135,137,138,140,],[-3,-12,-14,17,-13,-23,-14,-16,-24,-17,-29,-26,-18,-31,-33,-34,-14,17,-2,-4,-41,-45,-49,-67,-68,-69,-14,17,-58,-59,-60,-75,-30,-32,17,-22,-11,-5,-50,-25,-15,-19,-14,-21,-71,-73,17,-42,-46,-14,17,-14,17,-20,]),'print':([3,4,5,9,15,22,23,26,27,31,32,33,34,35,36,37,41,43,44,45,49,50,51,52,53,54,60,68,82,83,84,85,86,87,90,105,106,107,109,110,114,115,118,123,125,126,128,130,131,132,135,137,138,140,],[-3,-12,-14,18,-13,-23,-14,-16,-24,-17,-29,-26,-18,-31,-33,-34,-14,18,-2,-4,-41,-45,-49,-67,-68,-69,-14,18,-58,-59,-60,-75,-30,-32,18,-22,-11,-5,-50,-25,-15,-19,-14,-21,-71,-73,18,-42,-46,-14,18,-14,18,-20,]),'if':([3,4,5,9,15,22,23,26,27,31,32,33,34,35,36,37,41,43,44,45,49,50,51,52,53,54,60,68,82,83,84,85,86,87,88,90,105,106,107,109,110,114,115,118,123,125,126,128,130,131,132,135,137,138,140,],[-3,-12,-14,19,-13,-23,-14,-16,-24,-17,-29,-26,-18,-31,-33,-34,-14,19,-2,-4,-41,-45,-49,-67,-68,-69,-14,19,-58,-59,-60,-75,-30,-32,115,19,-22,-11,-5,-50,-25,-15,-19,-14,-21,-71,-73,19,-42,-46,-14,19,-14,19,-20,]),'do':([3,4,5,9,15,22,23,26,27,31,32,33,34,35,36,37,41,43,44,45,49,50,51,52,53,54,60,68,82,83,84,85,86,87,90,104,105,106,107,109,110,114,115,118,123,125,126,128,130,131,132,135,137,138,139,140,],[-3,-12,-14,20,-13,-23,-14,-16,-24,-17,-29,-26,-18,-31,-33,-34,-14,20,-2,-4,-41,-45,-49,-67,-68,-69,-14,20,-58,-59,-60,-75,-30,-32,20,123,-22,-11,-5,-50,-25,-15,-19,-14,-21,-71,-73,20,-42,-46,-14,20,-14,20,140,-20,]),'swap':([3,4,5,9,15,22,23,26,27,31,32,33,34,35,36,37,41,43,44,45,49,50,51,52,53,54,60,68,82,83,84,85,86,87,90,105,106,107,109,110,114,115,118,123,125,126,128,130,131,132,135,137,138,140,],[-3,-12,-14,21,-13,-23,-14,-16,-24,-17,-29,-26,-18,-31,-33,-34,-14,21,-2,-4,-41,-45,-49,-67,-68,-69,-14,21,-58,-59,-60,-75,-30,-32,21,-22,-11,-5,-50,-25,-15,-19,-14,-21,-71,-73,21,-42,-46,-14,21,-14,21,-20,]),'exit':([3,4,5,9,15,22,23,26,27,31,32,33,34,35,36,37,41,43,44,45,49,50,51,52,53,54,60,68,82,83,84,85,86,87,90,105,106,107,109,110,114,115,118,123,125,126,128,130,131,132,135,137,138,140,],[-3,-12,-14,22,-13,-23,-14,-16,-24,-17,-29,-26,-18,-31,-33,-34,-14,22,-2,-4,-41,-45,-49,-67,-68,-69,-14,22,-58,-59,-60,-75,-30,-32,22,-22,-11,-5,-50,-25,-15,-19,-14,-21,-71,-73,22,-42,-46,-14,22,-14,22,-20,]),'openBra':([6,7,8,46,],[12,-6,-7,72,]),'doubleColon':([6,7,8,11,46,124,],[-10,-6,-7,24,-8,-9,]),'int':([12,28,39,47,55,61,66,67,72,75,76,77,78,79,80,81,89,93,94,95,96,97,98,99,100,101,111,113,122,133,],[25,53,53,53,53,53,53,53,108,-70,53,-43,-44,-72,-47,-48,53,53,53,53,-61,-62,-63,-64,-65,-66,53,53,53,136,]),'parens':([13,],[26,]),'openParen':([13,19,28,33,39,47,55,59,61,66,67,75,76,77,78,79,80,81,89,93,94,111,113,122,],[28,39,47,28,61,47,47,89,61,61,47,-70,47,-43,-44,-72,-47,-48,61,61,61,47,47,47,]),'equals':([13,16,27,30,40,110,],[-26,-74,-24,55,67,-25,]),'elif':([15,22,26,27,31,32,33,34,35,36,37,38,49,50,51,52,53,54,82,83,84,85,86,87,105,109,110,114,115,118,123,125,126,128,130,131,132,135,140,],[-13,-23,-16,-24,-17,-29,-26,-18,-31,-33,-34,59,-41,-45,-49,-67,-68,-69,-58,-59,-60,-75,-30,-32,-22,-50,-25,-15,-19,-14,-21,-71,-73,-35,-42,-46,-14,-36,-20,]),'else':([15,22,26,27,31,32,33,34,35,36,37,38,49,50,51,52,53,54,82,83,84,85,86,87,105,109,110,114,115,118,123,125,126,128,130,131,132,135,140,],[-13,-23,-16,-24,-17,-29,-26,-18,-31,-33,-34,60,-41,-45,-49,-67,-68,-69,-58,-59,-60,-75,-30,-32,-22,-50,-25,-15,-19,-14,-21,-71,-73,-35,-42,-46,-14,-36,-20,]),'string':([18,57,],[37,37,]),'then':([20,27,33,49,50,51,52,53,54,82,83,84,92,109,110,125,126,127,129,130,131,134,136,],[41,-24,-26,-41,-45,-49,-67,-68,-69,-58,-59,-60,118,-50,-25,-71,-73,132,-40,-42,-46,137,-39,]),'closedBra':([25,108,],[46,124,]),'coma':([27,31,32,33,34,35,36,37,42,44,45,48,49,50,51,52,53,54,82,83,84,86,87,103,107,109,110,125,126,129,130,131,],[-24,56,-29,-26,57,-31,-33,-34,69,71,-4,76,-41,-45,-49,-67,-68,-69,-58,-59,-60,-30,-32,122,-5,-50,-25,-71,-73,133,-42,-46,]),'mul':([27,33,49,50,51,52,53,54,82,83,84,109,110,125,126,131,],[-24,-26,80,-45,-49,-67,-68,-69,-58,-59,-60,-50,-25,80,-73,-46,]),'div':([27,33,49,50,51,52,53,54,82,83,84,109,110,125,126,131,],[-24,-26,81,-45,-49,-67,-68,-69,-58,-59,-60,-50,-25,81,-73,-46,]),'plus':([27,33,48,49,50,51,52,53,54,73,82,83,84,85,103,109,110,112,125,126,129,130,131,],[-24,-26,77,-41,-45,-49,-67,-68,-69,77,-58,-59,-60,77,77,-50,-25,77,-71,-73,77,-42,-46,]),'minus':([27,33,48,49,50,51,52,53,54,73,82,83,84,85,103,109,110,112,125,126,129,130,131,],[-24,-26,78,-41,-45,-49,-67,-68,-69,78,-58,-59,-60,78,78,-50,-25,78,-71,-73,78,-42,-46,]),'closedParen':([27,33,48,49,50,51,52,53,54,62,63,64,73,74,82,83,84,91,102,109,110,112,116,117,119,120,121,125,126,130,131,],[-24,-26,-28,-41,-45,-49,-67,-68,-69,92,-51,-53,109,110,-58,-59,-60,117,-57,-50,-25,-27,127,-56,-52,-54,-55,-71,-73,-42,-46,]),'less':([27,33,52,53,54,65,82,83,84,110,],[-24,-26,-67,-68,-69,96,-58,-59,-60,-25,]),'more':([27,33,52,53,54,65,82,83,84,110,],[-24,-26,-67,-68,-69,97,-58,-59,-60,-25,]),'doubleEquals':([27,33,52,53,54,65,82,83,84,110,],[-24,-26,-67,-68,-69,98,-58,-59,-60,-25,]),'notEquals':([27,33,52,53,54,65,82,83,84,110,],[-24,-26,-67,-68,-69,99,-58,-59,-60,-25,]),'lessEquals':([27,33,52,53,54,65,82,83,84,110,],[-24,-26,-67,-68,-69,100,-58,-59,-60,-25,]),'moreEquals':([27,33,52,53,54,65,82,83,84,110,],[-24,-26,-67,-68,-69,101,-58,-59,-60,-25,]),'and':([27,33,52,53,54,63,64,82,83,84,102,110,117,119,120,121,],[-24,-26,-67,-68,-69,94,-53,-58,-59,-60,-57,-25,-56,94,-54,-55,]),'or':([27,33,52,53,54,62,63,64,82,83,84,91,102,110,116,117,119,120,121,],[-24,-26,-67,-68,-69,93,-51,-53,-58,-59,-60,93,93,-25,93,-56,-52,-54,-55,]),'rea':([28,39,47,55,61,66,67,75,76,77,78,79,80,81,89,93,94,95,96,97,98,99,100,101,111,113,122,],[54,54,54,54,54,54,54,-70,54,-43,-44,-72,-47,-48,54,54,54,54,-61,-62,-63,-64,-65,-66,54,54,54,]),'not':([39,61,66,89,93,94,],[66,66,66,66,66,66,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'V':([3,],[4,]),'F':([4,],[5,]),'Tipo':([4,],[6,]),'B':([5,23,41,60,118,132,137,],[9,43,68,90,128,135,138,]),'Dim':([6,],[11,]),'S':([9,43,68,90,128,135,138,],[15,15,15,15,15,15,15,]),'Dimensional':([9,17,18,21,28,39,43,47,55,56,57,61,66,67,68,69,76,89,90,93,94,95,111,113,122,128,135,138,],[16,32,36,42,52,52,16,52,52,86,36,52,52,52,16,105,52,52,16,52,52,52,52,52,52,16,16,16,]),'DimensionsOrEmpty':([13,33,],[27,27,]),'action_7':([16,],[30,]),'RDimensional':([17,],[31,]),'RDimOrString':([18,],[34,]),'DimOrString':([18,57,],[35,87,]),'Relif':([19,],[38,]),'Rid':([24,],[44,]),'EA':([28,47,55,67,76,122,],[48,73,85,103,112,129,]),'MultDiv':([28,47,55,67,76,111,122,],[49,49,49,49,49,125,49,]),'EAParens':([28,47,55,67,76,111,113,122,],[50,50,50,50,50,50,126,50,]),'EItem':([28,39,47,55,61,66,67,76,89,93,94,95,111,113,122,],[51,65,51,51,65,65,51,51,65,65,65,121,51,51,51,]),'ElseOrEmpty':([38,],[58,]),'EL':([39,61,66,89,],[62,91,102,116,]),'AND':([39,61,66,89,93,],[63,63,63,63,119,]),'Equality':([39,61,66,89,93,94,],[64,64,64,64,64,120,]),'ComaEAOrEmpty':([48,],[74,]),'SumOrSub':([48,73,85,103,112,129,],[75,75,75,75,75,75,]),'MDSymbols':([49,125,],[79,79,]),'action_1':([52,],[82,]),'action_2':([53,],[83,]),'action_2_rea':([54,],[84,]),'EQSymbols':([65,],[95,]),'action_3':([75,],[111,]),'action_5':([79,],[113,]),'action_8':([85,],[114,]),'action_4':([125,],[130,]),'action_6':([126,],[131,]),'IntOrEmpty':([129,],[134,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> program id V F B end program','programa',7,'p_programa','fort.py',157),
  ('V -> V Tipo Dim doubleColon Rid','V',5,'p_V','fort.py',163),
  ('V -> <empty>','V',0,'p_V','fort.py',164),
  ('Rid -> id','Rid',1,'p_Rid','fort.py',175),
  ('Rid -> Rid coma id','Rid',3,'p_Rid','fort.py',176),
  ('Tipo -> integer','Tipo',1,'p_Tipo','fort.py',187),
  ('Tipo -> real','Tipo',1,'p_Tipo','fort.py',188),
  ('Dim -> openBra int closedBra','Dim',3,'p_Dim','fort.py',195),
  ('Dim -> openBra int closedBra openBra int closedBra','Dim',6,'p_Dim','fort.py',196),
  ('Dim -> <empty>','Dim',0,'p_Dim','fort.py',197),
  ('F -> F subroutine id B end subroutine','F',6,'p_F','fort.py',202),
  ('F -> <empty>','F',0,'p_F','fort.py',203),
  ('B -> B S','B',2,'p_B','fort.py',208),
  ('B -> <empty>','B',0,'p_B','fort.py',209),
  ('S -> Dimensional action_7 equals EA action_8','S',5,'p_S','fort.py',214),
  ('S -> id parens','S',2,'p_S','fort.py',215),
  ('S -> read RDimensional','S',2,'p_S','fort.py',216),
  ('S -> print RDimOrString','S',2,'p_S','fort.py',217),
  ('S -> if Relif ElseOrEmpty end if','S',5,'p_S','fort.py',218),
  ('S -> do id equals EA coma EA IntOrEmpty then B end do','S',11,'p_S','fort.py',219),
  ('S -> do then B end do','S',5,'p_S','fort.py',220),
  ('S -> swap Dimensional coma Dimensional','S',4,'p_S','fort.py',221),
  ('S -> exit','S',1,'p_S','fort.py',222),
  ('Dimensional -> id DimensionsOrEmpty','Dimensional',2,'p_Dimensional','fort.py',228),
  ('DimensionsOrEmpty -> openParen EA ComaEAOrEmpty closedParen','DimensionsOrEmpty',4,'p_DimensionsOrEmpty','fort.py',235),
  ('DimensionsOrEmpty -> <empty>','DimensionsOrEmpty',0,'p_DimensionsOrEmpty','fort.py',236),
  ('ComaEAOrEmpty -> coma EA','ComaEAOrEmpty',2,'p_ComaEAOrEmpty','fort.py',241),
  ('ComaEAOrEmpty -> <empty>','ComaEAOrEmpty',0,'p_ComaEAOrEmpty','fort.py',242),
  ('RDimensional -> Dimensional','RDimensional',1,'p_RDimensional','fort.py',247),
  ('RDimensional -> RDimensional coma Dimensional','RDimensional',3,'p_RDimensional','fort.py',248),
  ('RDimOrString -> DimOrString','RDimOrString',1,'p_RDimOrString','fort.py',253),
  ('RDimOrString -> RDimOrString coma DimOrString','RDimOrString',3,'p_RDimOrString','fort.py',254),
  ('DimOrString -> Dimensional','DimOrString',1,'p_DimOrString','fort.py',259),
  ('DimOrString -> string','DimOrString',1,'p_DimOrString','fort.py',260),
  ('Relif -> openParen EL closedParen then B','Relif',5,'p_Relif','fort.py',265),
  ('Relif -> Relif elif openParen EL closedParen then B','Relif',7,'p_Relif','fort.py',266),
  ('ElseOrEmpty -> else B','ElseOrEmpty',2,'p_ElseOrEmpty','fort.py',271),
  ('ElseOrEmpty -> <empty>','ElseOrEmpty',0,'p_ElseOrEmpty','fort.py',272),
  ('IntOrEmpty -> coma int','IntOrEmpty',2,'p_IntOrEmpty','fort.py',277),
  ('IntOrEmpty -> <empty>','IntOrEmpty',0,'p_IntOrEmpty','fort.py',278),
  ('EA -> MultDiv','EA',1,'p_EA','fort.py',283),
  ('EA -> EA SumOrSub action_3 MultDiv action_4','EA',5,'p_EA','fort.py',284),
  ('SumOrSub -> plus','SumOrSub',1,'p_SumOrSub','fort.py',290),
  ('SumOrSub -> minus','SumOrSub',1,'p_SumOrSub','fort.py',291),
  ('MultDiv -> EAParens','MultDiv',1,'p_MultDiv','fort.py',297),
  ('MultDiv -> MultDiv MDSymbols action_5 EAParens action_6','MultDiv',5,'p_MultDiv','fort.py',298),
  ('MDSymbols -> mul','MDSymbols',1,'p_MDSymbols','fort.py',303),
  ('MDSymbols -> div','MDSymbols',1,'p_MDSymbols','fort.py',304),
  ('EAParens -> EItem','EAParens',1,'p_EAParens','fort.py',310),
  ('EAParens -> openParen EA closedParen','EAParens',3,'p_EAParens','fort.py',311),
  ('EL -> AND','EL',1,'p_EL','fort.py',316),
  ('EL -> EL or AND','EL',3,'p_EL','fort.py',317),
  ('AND -> Equality','AND',1,'p_AND','fort.py',322),
  ('AND -> AND and Equality','AND',3,'p_AND','fort.py',323),
  ('Equality -> EItem EQSymbols EItem','Equality',3,'p_Equality','fort.py',328),
  ('Equality -> openParen EL closedParen','Equality',3,'p_Equality','fort.py',329),
  ('Equality -> not EL','Equality',2,'p_Equality','fort.py',330),
  ('EItem -> Dimensional action_1','EItem',2,'p_EItem','fort.py',335),
  ('EItem -> int action_2','EItem',2,'p_EItem','fort.py',336),
  ('EItem -> rea action_2_rea','EItem',2,'p_EItem','fort.py',337),
  ('EQSymbols -> less','EQSymbols',1,'p_EQSymbols','fort.py',342),
  ('EQSymbols -> more','EQSymbols',1,'p_EQSymbols','fort.py',343),
  ('EQSymbols -> doubleEquals','EQSymbols',1,'p_EQSymbols','fort.py',344),
  ('EQSymbols -> notEquals','EQSymbols',1,'p_EQSymbols','fort.py',345),
  ('EQSymbols -> lessEquals','EQSymbols',1,'p_EQSymbols','fort.py',346),
  ('EQSymbols -> moreEquals','EQSymbols',1,'p_EQSymbols','fort.py',347),
  ('action_1 -> <empty>','action_1',0,'p_action_1','fort.py',352),
  ('action_2 -> <empty>','action_2',0,'p_action_2','fort.py',362),
  ('action_2_rea -> <empty>','action_2_rea',0,'p_action_2_rea','fort.py',367),
  ('action_3 -> <empty>','action_3',0,'p_action_3','fort.py',372),
  ('action_4 -> <empty>','action_4',0,'p_action_4','fort.py',376),
  ('action_5 -> <empty>','action_5',0,'p_action_5','fort.py',393),
  ('action_6 -> <empty>','action_6',0,'p_action_6','fort.py',398),
  ('action_7 -> <empty>','action_7',0,'p_action_7','fort.py',416),
  ('action_8 -> <empty>','action_8',0,'p_action_8','fort.py',426),
]
