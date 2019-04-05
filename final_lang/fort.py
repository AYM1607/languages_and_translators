import ply.lex as lex
import ply.yacc as yacc
import sys
from stack import Stack

resultQuadruplets = []
quadrupletIndex = 1

# Auxiliary stacks.
operandsStack = []
operatorsStack = []
jumpsStack = []
auxStack = []
avail = []
for i in range(50):
    avail.append('T' + str(i))

# Operations related to the table of symbols
symbolsNames = []
symbolsTypes = []
symbols = {}

# # Implementation using lists.
# def addSymbol(name, symbolType):
#     symbolsNames.append(name)
#     symbolsTypes.append(symbolType)

# Implementation using a dictionary
def addSymbol(name, symbolsTypes):
    initialValue = 0 if symbolsTypes == 'integer' else 0.0
    symbols[name] = [name, initialValue]
    
def peek(list):
    if (len(list) == 0):
        return None
    return list[len(list) - 1]

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
    S : Dimensional equals EA
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
          | rea action_2
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
    operandsStack.append(p[-1])


def p_action_2(p):
    "action_2 :"
    operandsStack.append(p[-1])

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
        temp = avail.pop(0)
        operandsStack.append(temp)
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
        temp = avail.pop(0)
        operandsStack.append(temp)
        resultQuadruplets.append(str(operator) + ' ' + str(operand1) + ' ' + str(operand2) + ' ' + str(temp) + '\n')
        quadrupletIndex += 1


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


