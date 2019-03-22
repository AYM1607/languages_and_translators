import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'program',
    'end',
    'doubleColon',
    'coma',
    'integer',
    'real',
    'openBra',
    'closedBra',
    'int',
    'rea',
    'subroutine',
    'parens',
    'openParen',
    'closedParen',
    'read',
    'print',
    'if',
    'then',
    'else',
    'elif',
    'do',
    'swap',
    'exit',
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
]

t_program = r'program'
t_end = r'end'
t_read = r'read'
t_print = r'print'
t_if = r'if'
t_then = r'then'
t_else = r'else'
t_elif = r'elif'
t_do = r'do'
t_swap = r'swap'
t_exit = r'exit'
t_integer = r'integer'
t_real = r'real'
t_subroutine = r'subroutine'
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
t_string = r'".*"'
t_or = r'or'
t_and = r'and'
t_not = r'not'
t_doubleEquals = r'=='
t_equals = r'='
t_notEquals = r'/='
t_div = r'/'
t_lessEquals = r'<='
t_less = r'<'
t_moreEquals = r'>='
t_more = r'>'
t_ignore = ' \n'

def t_int(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_rea(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_id(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'id'
    return t

def t_error(t):
    print("Illegal character!")
    t.lexer.skip(1)

lexer = lex.lex()

def p_programa(p):
    '''
    programa : program id V F B end program
    ''' 
    print('✓✓✓ Valid program')

def p_V(p):
    '''
    V : V Tipo Dim doubleColon Rid
      |
    '''

def p_Rid(p):
    '''
    Rid : id
       | Rid coma id
    '''

def p_Tipo(p):
    '''
    Tipo : integer
         | real
    '''

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
      | do id equals EA coma EA IntOrEmpty B end do
      | do B end do
      | swap Dimensional coma Dimensional
      | exit
    '''

def p_Dimensional(p):
    '''
    Dimensional : id DimensionsOrEmpty
    '''

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
       | EA SumOrSub MultDiv
    '''

def p_SumOrSub(p):
    '''
    SumOrSub : plus
             | minus
    '''

def p_MultDiv(p):
    '''
    MultDiv : EAParens
            | MultDiv MDSymbols EAParens
    '''

def p_MDSymbols(p):
    '''
    MDSymbols : mul
              | div
    '''

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
    EItem : Dimensional
          | int
          | rea
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

def p_error(p):
    print('xxx Invalid program')


parser = yacc.yacc()

fort_program = '''
program _matrix 
end program
'''


#parser.parse(fort_program)

lexer.input(fort_program)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)


