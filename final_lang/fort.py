import ply.lex as lex
import ply.yacc as yacc
import sys
# Ignore unresolved import error if present.
from typeValidation import resultingType

# ----------------------------------------------------------------------------
# --------------------------------Globals-------------------------------------
# ----------------------------------------------------------------------------

kEqualityOperators = ['>', '<', '>=', '<=', '==', '/=', ]

resultQuadruplets = []
# The first quadruplet will be line 1, that way it will match the lines in
# the editor and will be easier to analyze.
quadrupletIndex = 1

# Auxiliary stacks.
operandsStack = []
operatorsStack = []
typesStack = []
jumpsStack = []
exitsStack = []
avail = []
for i in range(49):
    avail.append('$' + str(i))

indirectPointer = '$49'

# Operations related to the table of symbols
symbols = {}
# Our variables start at direction 50, the temps take the first 49 directions.
currentIndex = 50

# Multi dimensional variables dimensions just for declaration.
globalDimension1 = 0
globalDimension2 = 0
globalDimensionalSize = 1

# Multi dimensional variables dimensions just for accessing.
globalIndex1 = 0
globalIndex2 = 0

# ----------------------------------------------------------------------------
# ------------------------------Util methods----------------------------------
# ----------------------------------------------------------------------------

# Adds a symbol to the symbols table.


def addSymbol(name, symbolType):
    global currentIndex
    initialValue = 0 if symbolType == 'integer' else 0.0
    symbols[name] = {
        'type': symbolType,
        'value': initialValue,
        'direction': currentIndex,
        'dimension1': globalDimension1,
        'dimension2': globalDimension2,
    }
    currentIndex += globalDimensionalSize

# Returns the last item of a list without deleting it.


def peek(list):
    if (len(list) == 0):
        return None
    return list[len(list) - 1]

# Checks whether or not a an operand is a temp variable.


def isTemp(operand):
    if type(operand) is not str:
        return False
    operand = int(operand[1:])
    if (operand < 50):
        return True
    return False


def isDirection(operand):
    if type(operand) is not str:
        return False
    if "$" in operand:
        return True
    return False


def fillGoto(position, fillValue):
    global resultQuadruplets
    # Using position - 1  because the quadruplets start at 1 and not 0.
    resultQuadruplets[position-1] = resultQuadruplets[position -
                                                      1].replace('_', str(fillValue))
    return

# ----------------------------------------------------------------------------
# ---------------------------------LEXER--------------------------------------
# ----------------------------------------------------------------------------


tokens = [
    'doubleColon',
    'coma',
    'openBra',
    'closedBra',
    'int',
    'rea',
    'parens',
    'openParen',
    'closedParen',
    'string',
    'plus',
    'minus',
    'mul',
    'div',
    'or',
    'and',
    'not',
    'equals',
    'doubleEquals',
    'notEquals',
    'less',
    'more',
    'lessEquals',
    'moreEquals',
    'id',
    'program',
    'end',
    'read',
    'print',
    'if',
    'then',
    'else',
    'elif',
    'do',
    'swap',
    'exit',
    'integer',
    'real',
    'subroutine',
]

reserved = {
    'program': 'program',
    'end': 'end',
    'read': 'read',
    'print': 'print',
    'if': 'if',
    'then': 'then',
    'else': 'else',
    'elif': 'elif',
    'do': 'do',
    'swap': 'swap',
    'exit': 'exit',
    'integer': 'integer',
    'real': 'real',
    'subroutine': 'subroutine',
}

t_doubleColon = r'::'
t_coma = r','
t_openBra = r'\['
t_closedBra = r'\]'
t_parens = r'\(\)'
t_openParen = r'\('
t_closedParen = r'\)'
t_plus = r'\+'
t_minus = r'-'
t_mul = r'\*'
t_string = r'\'[a-zA-Z0-9 \t\r\n\f()\[\]\&\!\@\#\$\%\^\-\=\+\/\,]*\''
t_or = r'\.or\.'
t_and = r'\.and\.'
t_not = r'\.not\.'
t_doubleEquals = r'\=\='
t_equals = r'\='
t_notEquals = r'\/\='
t_div = r'\/'
t_lessEquals = r'\<\='
t_less = r'\<'
t_moreEquals = r'\>\='
t_more = r'\>'
t_ignore = ' \t\r\n\f\v'


def t_rea(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_int(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_id(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = 'id'
    return t


def t_error(t):
    print("Illegal character!")
    print(t)
    t.lexer.skip(1)


lexer = lex.lex()


# ----------------------------------------------------------------------------
# ---------------------------------PARSER-------------------------------------
# ----------------------------------------------------------------------------


def p_programa(p):
    '''
    programa : program id V F B end program
    '''
    print('+++ Valid program')


def p_V(p):
    '''
    V : V Tipo Dim doubleColon Rid action_addSymbols action_32
      |
    '''


def p_Rid(p):
    '''
    Rid : id
       | Rid coma id
    '''
    # p[0] will contain an list with all the variable
    # names for this production in string format.
    if (len(p) == 2):
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_Tipo(p):
    '''
    Tipo : integer
         | real
    '''
    # p[0] will contain the type in string format
    p[0] = p[1]


def p_Dim(p):
    '''
    Dim : openBra int action_30 closedBra
        | openBra int action_30 closedBra openBra int action_31 closedBra
        |
    '''


def p_F(p):
    '''
    F : F subroutine id B end subroutine
      |
    '''


def p_B(p):
    '''
    B : B S
      |
    '''

def p_S(p):
    '''
    S : Dimensional action_7 equals EA action_8
      | id parens
      | read RDimensional
      | print RDimOrString
      | if action_16 Relif ElseOrEmpty end if action_20
      | do id action_24 equals EA action_25 coma EA action_26 IntOrEmpty then B action_29 end do
      | do then action_21 B action_22 end do
      | swap Dimensional coma Dimensional
      | exit action_23 
      | id openParen closedParen
    '''

# Adjust the action to support matrices


def p_Dimensional(p):
    '''
    Dimensional : id DimensionsOrEmpty
    '''
    p[0] = p[1]


def p_DimensionsOrEmpty(p):
    '''
    DimensionsOrEmpty : openParen EA action_setDim1 ComaEAOrEmpty closedParen
                      |
    '''


def p_ComaEAOrEmpty(p):
    '''
    ComaEAOrEmpty : coma EA action_setDim2
                  |
    '''


def p_RDimensional(p):
    '''
    RDimensional : Dimensional
                 | RDimensional coma Dimensional
    '''


def p_RDimOrString(p):
    '''
    RDimOrString : DimOrString
                 | RDimOrString coma DimOrString
    '''


def p_DimOrString(p):
    '''
    DimOrString : Dimensional
                | string
    '''


def p_Relif(p):
    '''
    Relif : openParen EL closedParen action_17 then B
          | Relif elif action_18 openParen EL closedParen action_17 then B
    '''


def p_ElseOrEmpty(p):
    '''
    ElseOrEmpty : else action_19 B
                |
    '''


def p_IntOrEmpty(p):
    '''
    IntOrEmpty : coma int action_28
               | action_27
    '''


def p_EA(p):
    '''
    EA : MultDiv
       | EA SumOrSub action_3 MultDiv action_4
    '''


def p_SumOrSub(p):
    '''
    SumOrSub : plus
             | minus
    '''
    p[0] = p[1]


def p_MultDiv(p):
    '''
    MultDiv : EAParens
            | MultDiv MDSymbols action_5 EAParens action_6
    '''


def p_MDSymbols(p):
    '''
    MDSymbols : mul
              | div
    '''
    p[0] = p[1]


def p_EAParens(p):
    '''
    EAParens : EItem
             | openParen EA closedParen
    '''


def p_EL(p):
    '''
    EL : AND
       | EL or action_10 AND action_9
    '''


def p_AND(p):
    '''
    AND : Equality
        | AND and action_12 Equality action_11
    '''


def p_Equality(p):
    '''
    Equality : EItem EQSymbols action_13 EItem action_14
             | openParen EL closedParen
             | not EL action_15
    '''


def p_EItem(p):
    '''
    EItem : Dimensional action_1
          | int action_2
          | rea action_2_rea
    '''


def p_EQSymbols(p):
    '''
    EQSymbols : less
              | more
              | doubleEquals
              | notEquals
              | lessEquals
              | moreEquals
    '''
    p[0] = p[1]

# ----------------------------------------------------------------------------
# -----------------------------PARSER ACTIONS---------------------------------
# ----------------------------------------------------------------------------

def p_action_addSymbols(p):
    "action_addSymbols :"
    for name in p[-1]:
        addSymbol(name, p[-4])

###############################################################################
###############################################################################
#WARNING DON'T USE MULTIDIM VARIABLES ELEMENTS ON AE TO CALCULATE ANOTHER INDEX
###############################################################################
###############################################################################

def p_action_1(p):
    "action_1 :"
    global globalIndex1
    global globalIndex2
    global quadrupletIndex
    global resultQuadruplets
    global avail
    if p[-1] not in symbols:
        raise Exception(f'The variable {p[-1]} was not declared')
    direction = symbols[p[-1]]['direction']
    dimension1 = symbols[p[-1]]['dimension1']
    dimension2 = symbols[p[-1]]['dimension2']
    if dimension2 is not 0:
        if isDirection(globalIndex1) or isDirection(globalIndex2):
            resultQuadruplets.append(f'* {globalIndex1} {dimension1} {indirectPointer}\n')
            quadrupletIndex += 1
            resultQuadruplets.append(f'+ {globalIndex2} {indirectPointer} {indirectPointer}\n')
            quadrupletIndex += 1
            resultQuadruplets.append(f'+ {direction} {indirectPointer} {indirectPointer}\n')
            quadrupletIndex += 1
            operandsStack.append(indirectPointer.replace('$', '*'))
        else:
            direction += globalIndex2 + (globalIndex1 * dimension1)
            operandsStack.append(f'${direction}')
    elif dimension1 is not 0:
        if isDirection(globalIndex1):
            resultQuadruplets.append(f'+ {direction} {globalIndex1} {indirectPointer}\n')
            quadrupletIndex += 1
            operandsStack.append(indirectPointer.replace('$', '*'))
        else:
            direction += globalIndex1
            operandsStack.append(f'${direction}')
    else:
        operandsStack.append(f'${direction}')
    sType = symbols[p[-1]]['type']
    #operandsStack.append(f'${direction}')
    typesStack.append(sType)
    globalIndex1 = 0
    globalIndex2 = 0


def p_action_2(p):
    "action_2 :"
    operandsStack.append(p[-1])
    typesStack.append('integer')


def p_action_2_rea(p):
    "action_2_rea :"
    operandsStack.append(p[-1])
    typesStack.append('real')


def p_action_3(p):
    "action_3 :"
    operatorsStack.append(p[-1])


def p_action_4(p):
    "action_4 :"
    if (peek(operatorsStack) == '+' or peek(operatorsStack) == '-'):
        global quadrupletIndex
        global avail
        operator = operatorsStack.pop()
        operand2 = operandsStack.pop()
        operand1 = operandsStack.pop()
        type2 = typesStack.pop()
        type1 = typesStack.pop()
        resultType = resultingType(operator, type1, type2)
        temp = avail.pop(0)
        operandsStack.append(temp)
        typesStack.append(resultType)
        resultQuadruplets.append(str(
            operator) + ' ' + str(operand1) + ' ' + str(operand2) + ' ' + str(temp) + '\n')
        quadrupletIndex += 1
        if (isTemp(operand2)):
            avail = [operand2] + avail
        if (isTemp(operand1)):
            avail = [operand1] + avail


def p_action_5(p):
    "action_5 :"
    operatorsStack.append(p[-1])


def p_action_6(p):
    "action_6 :"
    if (peek(operatorsStack) == '*' or peek(operatorsStack) == '/'):
        global quadrupletIndex
        global avail
        operator = operatorsStack.pop()
        operand2 = operandsStack.pop()
        operand1 = operandsStack.pop()
        type2 = typesStack.pop()
        type1 = typesStack.pop()
        resultType = resultingType(operator, type1, type2)
        temp = avail.pop(0)
        operandsStack.append(temp)
        typesStack.append(resultType)
        resultQuadruplets.append(str(
            operator) + ' ' + str(operand1) + ' ' + str(operand2) + ' ' + str(temp) + '\n')
        quadrupletIndex += 1
        if (isTemp(operand2)):
            avail = [operand2] + avail
        if (isTemp(operand1)):
            avail = [operand1] + avail


def p_action_7(p):
    "action_7 :"
    global globalIndex1
    global globalIndex2
    global quadrupletIndex
    global resultQuadruplets
    global avail
    if p[-1] not in symbols:
        raise Exception(f'The variable {p[-1]} was not declared')
    direction = symbols[p[-1]]['direction']
    dimension1 = symbols[p[-1]]['dimension1']
    dimension2 = symbols[p[-1]]['dimension2']
    if dimension2 is not 0:
        if isDirection(globalIndex1) or isDirection(globalIndex2):
            resultQuadruplets.append(f'* {globalIndex1} {dimension1} {indirectPointer}\n')
            quadrupletIndex += 1
            resultQuadruplets.append(f'+ {globalIndex2} {indirectPointer} {indirectPointer}\n')
            quadrupletIndex += 1
            resultQuadruplets.append(f'+ {direction} {indirectPointer} {indirectPointer}\n')
            quadrupletIndex += 1
            operandsStack.append(indirectPointer.replace('$', '*'))
        else:
            direction += globalIndex2 + (globalIndex1 * dimension1)
            operandsStack.append(f'${direction}')
    elif dimension1 is not 0:
        if isDirection(globalIndex1):
            resultQuadruplets.append(f'+ {direction} {globalIndex1} {indirectPointer}\n')
            quadrupletIndex += 1
            operandsStack.append(indirectPointer.replace('$', '*'))
        else:
            direction += globalIndex1
            operandsStack.append(f'${direction}')
    else:
        operandsStack.append(f'${direction}')
    sType = symbols[p[-1]]['type']
    #operandsStack.append(f'${direction}')
    typesStack.append(sType)
    globalIndex1 = 0
    globalIndex2 = 0


def p_action_8(p):
    "action_8 :"
    global quadrupletIndex
    global avail
    operand2 = operandsStack.pop()
    operand1 = operandsStack.pop()
    type2 = typesStack.pop()
    type1 = typesStack.pop()
    # Result type only gets called to make sure the types are compatible.
    resultingType('=', type1, type2)
    resultQuadruplets.append('= ' + str(operand2) +
                             '    ' + str(operand1) + '\n')
    quadrupletIndex += 1
    # Return the operand to the availbale if it is a temporal.
    if (isTemp(operand2)):
        avail = [operand2] + avail


def p_action_9(p):
    "action_9 :"
    if (peek(operatorsStack) == '.or.'):
        global quadrupletIndex
        global avail
        operator = operatorsStack.pop()
        operand2 = operandsStack.pop()
        operand1 = operandsStack.pop()
        type2 = typesStack.pop()
        type1 = typesStack.pop()
        resultType = resultingType(operator, type1, type2)
        temp = avail.pop(0)
        operandsStack.append(temp)
        typesStack.append(resultType)
        resultQuadruplets.append(str(
            operator) + ' ' + str(operand1) + ' ' + str(operand2) + ' ' + str(temp) + '\n')
        quadrupletIndex += 1
        if (isTemp(operand2)):
            avail = [operand2] + avail
        if (isTemp(operand1)):
            avail = [operand1] + avail


def p_action_10(p):
    "action_10 :"
    operatorsStack.append(p[-1])


def p_action_11(p):
    "action_11 :"
    if (peek(operatorsStack) == '.and.'):
        global quadrupletIndex
        global avail
        operator = operatorsStack.pop()
        operand2 = operandsStack.pop()
        operand1 = operandsStack.pop()
        type2 = typesStack.pop()
        type1 = typesStack.pop()
        resultType = resultingType(operator, type1, type2)
        temp = avail.pop(0)
        operandsStack.append(temp)
        typesStack.append(resultType)
        resultQuadruplets.append(str(
            operator) + ' ' + str(operand1) + ' ' + str(operand2) + ' ' + str(temp) + '\n')
        quadrupletIndex += 1
        if (isTemp(operand2)):
            avail = [operand2] + avail
        if (isTemp(operand1)):
            avail = [operand1] + avail


def p_action_12(p):
    "action_12 :"
    operatorsStack.append(p[-1])


def p_action_13(p):
    "action_13 :"
    operatorsStack.append(p[-1])


def p_action_14(p):
    "action_14 :"
    if (peek(operatorsStack) in kEqualityOperators):
        global quadrupletIndex
        global avail
        operator = operatorsStack.pop()
        operand2 = operandsStack.pop()
        operand1 = operandsStack.pop()
        type2 = typesStack.pop()
        type1 = typesStack.pop()
        resultType = resultingType(operator, type1, type2)
        temp = avail.pop(0)
        operandsStack.append(temp)
        typesStack.append(resultType)
        resultQuadruplets.append(str(
            operator) + ' ' + str(operand1) + ' ' + str(operand2) + ' ' + str(temp) + '\n')
        quadrupletIndex += 1
        if (isTemp(operand2)):
            avail = [operand2] + avail
        if (isTemp(operand1)):
            avail = [operand1] + avail


def p_action_15(p):
    "action_15 :"
    if (peek(typesStack) is not 'bool'):
        raise Exception("Cannot use .not. with non boolean")
    global quadrupletIndex
    # It is not necessary to pop the types stack since the result will also
    # be bool.
    operand1 = operandsStack.pop()
    temp = avail.pop(0)
    operandsStack.append(temp)
    resultQuadruplets.append('.not. ' + str(operand1) +
                             '    ' + str(temp) + '\n')
    quadrupletIndex += 1


def p_action_16(p):
    "action_16 :"
    jumpsStack.append('$')


def p_action_17(p):
    "action_17 :"
    global quadrupletIndex
    global avail
    operand1 = operandsStack.pop()
    type1 = typesStack.pop()
    if (type1 is not 'bool'):
        raise Exception(
            'Can\'t use non logical expression as conditional for if')
    jumpsStack.append(quadrupletIndex)
    resultQuadruplets.append('gotoF ' + str(operand1) + '   _\n')
    quadrupletIndex += 1
    if (isTemp(operand1)):
        avail = [operand1] + avail


def p_action_18(p):
    "action_18 :"
    global quadrupletIndex
    resultQuadruplets.append('goto  _\n')
    quadrupletIndex += 1
    Dir = jumpsStack.pop()
    fillGoto(Dir, quadrupletIndex)
    jumpsStack.append(quadrupletIndex - 1)


def p_action_19(p):
    "action_19 :"
    global quadrupletIndex
    resultQuadruplets.append('goto  _\n')
    quadrupletIndex += 1
    Dir = jumpsStack.pop()
    fillGoto(Dir, quadrupletIndex)
    jumpsStack.append(quadrupletIndex - 1)


def p_action_20(p):
    "action_20 :"
    while(peek(jumpsStack) is not '$'):
        Dir = jumpsStack.pop()
        fillGoto(Dir, quadrupletIndex)
    jumpsStack.pop()


def p_action_21(p):
    "action_21 :"
    jumpsStack.append(quadrupletIndex)
    exitsStack.append('$')


def p_action_22(p):
    "action_22 :"
    global resultQuadruplets
    global quadrupletIndex
    Dir = jumpsStack.pop()
    resultQuadruplets.append(f'goto   {Dir}\n')
    quadrupletIndex += 1
    while(peek(exitsStack) != '$'):
        Dir = exitsStack.pop()
        fillGoto(Dir, quadrupletIndex)
    exitsStack.pop()


def p_action_23(p):
    "action_23 :"
    global quadrupletIndex
    global quadrupletIndex
    exitsStack.append(quadrupletIndex)
    resultQuadruplets.append('goto   _\n')
    quadrupletIndex += 1


def p_action_24(p):
    "action_24 :"
    if p[-1] not in symbols:
        raise Exception(f'The variable {p[-1]} was not declared')
    direction = symbols[p[-1]]['direction']
    sType = symbols[p[-1]]['type']
    operandsStack.append(f'${direction}')
    operandsStack.append(f'${direction}')
    operandsStack.append(f'${direction}')
    typesStack.append(sType)
    typesStack.append(sType)
    typesStack.append(sType)


def p_action_25(p):
    "action_25 :"
    global quadrupletIndex
    global avail
    operand2 = operandsStack.pop()
    operand1 = operandsStack.pop()
    type2 = typesStack.pop()
    type1 = typesStack.pop()
    # Result type only gets called to make sure the types are compatible.
    resultingType('=', type1, type2)
    resultQuadruplets.append('= ' + str(operand2) +
                             '    ' + str(operand1) + '\n')
    quadrupletIndex += 1
    # Return the operand to the availbale if it is a temporal.
    if (isTemp(operand2)):
        avail = [operand2] + avail


def p_action_26(p):
    "action_26 :"
    global quadrupletIndex
    global avail
    operand2 = operandsStack.pop()
    operand1 = operandsStack.pop()
    type2 = typesStack.pop()
    type1 = typesStack.pop()
    # call function just to make sure types are compatible
    resultingType('<=', type1, type2)
    temp = avail.pop(0)
    # push to the jumps stack so the program can return to this quadruplet after each cycle.
    jumpsStack.append(quadrupletIndex)
    resultQuadruplets.append(
        '<=' + ' ' + str(operand1) + ' ' + str(operand2) + ' ' + str(temp) + '\n')
    quadrupletIndex += 1
    # push to the jumps stack so this gotoF can be filled later.
    jumpsStack.append(quadrupletIndex)
    resultQuadruplets.append(f'gotoF {str(temp)} _\n')
    quadrupletIndex += 1
    if (isTemp(operand2)):
        avail = [operand2] + avail
    if (isTemp(operand1)):
        avail = [operand1] + avail


def p_action_27(p):
    "action_27 :"
    operandsStack.append("1")
    typesStack.append("integer")


def p_action_28(p):
    "action_28 :"
    operandsStack.append(p[-1])
    typesStack.append("integer")


def p_action_29(p):
    "action_29 :"
    global quadrupletIndex
    global avail
    incrementOperand = operandsStack.pop()
    counterOperand = operandsStack.pop()
    incrementType = typesStack.pop()
    counterType = typesStack.pop()
    temp = avail.pop(0)
    # function call just to make sure that the types are compatible
    resultingType('+', counterType, incrementType)
    resultQuadruplets.append(f'+ {counterOperand} {incrementOperand} {temp}\n')
    quadrupletIndex += 1
    resultQuadruplets.append(f'= {temp}    {counterOperand}\n')
    quadrupletIndex += 1
    # return the temp used to the avail vector
    avail = [temp] + avail
    gotoFPosition = jumpsStack.pop()
    conditionPosition = jumpsStack.pop()
    resultQuadruplets.append(f'goto {conditionPosition}\n')
    quadrupletIndex += 1
    fillGoto(gotoFPosition, quadrupletIndex)

def p_action_30(p):
    "action_30 :"
    global globalDimension1
    global globalDimensionalSize
    globalDimension1 = p[-1]
    globalDimensionalSize *= p[-1]


def p_action_31(p):
    "action_31 :"
    global globalDimension2
    global globalDimensionalSize
    globalDimension2 = p[-1]
    globalDimensionalSize *= p[-1]

def p_action_32(p):
    "action_32 :"
    global globalDimension1
    global globalDimension2
    global globalDimensionalSize
    globalDimension1 = 0
    globalDimension2 = 0
    globalDimensionalSize = 1


def p_action_setDim1(p):
    "action_setDim1 :"
    global globalIndex1
    operand1 = operandsStack.pop()
    type1 = typesStack.pop()
    print(f'Tipo del index {type1}')
    if (type1 == 'integer'):
        globalIndex1 = operand1
    else:
        raise Exception("Cannot use floating point number as index")


def p_action_setDim2(p):
    "action_setDim2 :"
    global globalIndex2
    operand1 = operandsStack.pop()
    type1 = typesStack.pop()
    print(f'Tipo del index {type1}')
    if (type1 == 'integer'):
        globalIndex2 = operand1
    else:
        raise Exception("Cannot use floating point number as index")


def p_error(p):
    print('XXX Invalid program')
    print(p)


parser = yacc.yacc()


# ----------------------------------------------------------------------------
# --------------------INTERMEDIATE CODE FILE GENERATION-----------------------
# ----------------------------------------------------------------------------

if (len(sys.argv) > 1):
    programName = sys.argv[1]
    programFile = open(programName, "r")
    resultFile = open(programName + '.out', "w+")
    # This is neccessary because the read method parses literal ends
    # of lines as \\n instead of \n.
    program = programFile.read().replace('\\n', '\n')
    parser.parse(program)

    resultFile.writelines(resultQuadruplets)
    # Close the files.
    programFile.close()
    resultFile.close()
else:
    raise Exception('''
    No file name was provided.
    Please add the file name as a command line argument

    Example: fort.py test.fort
    ''')
