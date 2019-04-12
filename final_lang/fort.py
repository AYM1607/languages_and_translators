import ply.lex as lex
import ply.yacc as yacc
import sys
from typeValidation import resultingType

resultQuadruplets = []
quadrupletIndex = 1

# Auxiliary stacks.
operandsStack = []
operatorsStack = []
typesStack = []
jumpsStack = []
exitsStack = []
avail = []
for i in range(50):
    avail.append('$' + str(i))

# Operations related to the table of symbols
symbols = {}
# Our variables start at direction 50, the temps take the first 50 directions.
currentIndex = 50

# Implementation using a dictionary
def addSymbol(name, symbolType):
    global currentIndex
    initialValue = 0 if symbolType == 'integer' else 0.0
    symbols[name] = {
        'type': symbolType,
        'value': initialValue,
        'direction': currentIndex
    }
    currentIndex += 1

# Returns the last item of a list without deleting it.
def peek(list):
    if (len(list) == 0):
        return None
    return list[len(list) - 1]

# Checks whether or not a an operand is a temp variable.
def isTemp(operan):
    return


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
    'program' : 'program',
    'end' : 'end',
    'read' : 'read',
    'print' : 'print',
    'if' : 'if',
    'then' : 'then',
    'else' : 'else',
    'elif' : 'elif',
    'do' : 'do',
    'swap' : 'swap',
    'exit' : 'exit',
    'integer' : 'integer',
    'real' : 'real',
    'subroutine' : 'subroutine',
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
        t.type = reserved[ t.value ]
    else:  
        t.type = 'id'
    return t

def t_error(t):
    print("Illegal character!")
    print(t)
    t.lexer.skip(1)

lexer = lex.lex()

def p_programa(p):
    '''
    programa : program id V F B end program
    ''' 
    print('+++ Valid program')

def p_V(p):
    '''
    V : V Tipo Dim doubleColon Rid
      |
    '''
    # Adds all the variables for this production into the
    # symbols table.
    if (len(p) > 1):
        for name in p[5]:
            addSymbol(name, p[2])


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
    Dim : openBra int closedBra
        | openBra int closedBra openBra int closedBra
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
      | if Relif ElseOrEmpty end if
      | do id equals EA coma EA IntOrEmpty then B end do
      | do then B end do
      | swap Dimensional coma Dimensional
      | exit
    '''

# Adjust the action to support matrices
def p_Dimensional(p):
    '''
    Dimensional : id DimensionsOrEmpty
    '''
    p[0] = p[1]


def p_DimensionsOrEmpty(p):
    '''
    DimensionsOrEmpty : openParen EA ComaEAOrEmpty closedParen
                      |
    '''

def p_ComaEAOrEmpty(p):
    '''
    ComaEAOrEmpty : coma EA
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
    Relif : openParen EL closedParen then B
          | Relif elif openParen EL closedParen then B
    '''

def p_ElseOrEmpty(p):
    '''
    ElseOrEmpty : else B
                |
    '''

def p_IntOrEmpty(p):
    '''
    IntOrEmpty : coma int
               |
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
       | EL or AND
    '''

def p_AND(p):
    '''
    AND : Equality
        | AND and Equality
    '''

def p_Equality(p):
    '''
    Equality : EItem EQSymbols EItem
             | openParen EL closedParen
             | not EL
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


def p_action_1(p):
    "action_1 :"
    if p[-1] not in symbols:
        raise Exception(f'The variable {p[-1]} was not declared')
    direction = symbols[p[-1]]['direction']
    sType = symbols[p[-1]]['type']
    operandsStack.append(f'${direction}')
    typesStack.append(sType)


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
        operator = operatorsStack.pop()
        operand2 = operandsStack.pop()
        operand1 = operandsStack.pop()
        type2 = typesStack.pop()
        type1 = typesStack.pop()
        resultType = resultingType(operator, type1, type2)
        temp = avail.pop(0)
        operandsStack.append(temp)
        typesStack.append(resultType)
        resultQuadruplets.append(str(operator) + ' ' + str(operand1) + ' ' + str(operand2) + ' ' + str(temp) + '\n')
        quadrupletIndex += 1


def p_action_5(p):
    "action_5 :"
    operatorsStack.append(p[-1])


def p_action_6(p):
    "action_6 :"
    if (peek(operatorsStack) == '*' or peek(operatorsStack) == '/'):
        global quadrupletIndex
        operator = operatorsStack.pop()
        operand2 = operandsStack.pop()
        operand1 = operandsStack.pop()
        type2 = typesStack.pop()
        type1 = typesStack.pop()
        resultType = resultingType(operator, type1, type2)
        temp = avail.pop(0)
        operandsStack.append(temp)
        typesStack.append(resultType)
        resultQuadruplets.append(str(operator) + ' ' + str(operand1) + ' ' + str(operand2) + ' ' + str(temp) + '\n')
        quadrupletIndex += 1



def p_action_7(p):
    "action_7 :"
    if p[-1] not in symbols:
        raise Exception(f'The variable {p[-1]} was not declared')
    direction = symbols[p[-1]]['direction']
    sType = symbols[p[-1]]['type']
    operandsStack.append(f'${direction}')
    typesStack.append(sType)


def p_action_8(p):
    "action_8 :"
    operand2 = operandsStack.pop()
    operand1 = operandsStack.pop()
    type2 = typesStack.pop()
    type1 = typesStack.pop()
    # Result type only gets called to make sure the types are compatible.
    resultingType('=', type1, type2)
    resultQuadruplets.append('= ' + str(operand2) + '    ' + str(operand1) + '\n')


def p_error(p):
    print('XXX Invalid program')
    print(p)

parser = yacc.yacc()

if (len(sys.argv) > 1):
    programName = sys.argv[1]
    programFile = open(programName, "r")
    resultFile = open(programName + '.out', "w+")
    # This is neccessary because the read method parses literal ends
    # of lines as \\n instead of \n.
    program = programFile.read().replace('\\n', '\n')
    parser.parse(program)

    print(resultQuadruplets)
    print(symbols)
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


