import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'HOLA',
    'COMA',
    'QUE',
    'TAL',
]

t_HOLA = r'hola'
t_COMA = r','
t_QUE = r'que'
t_TAL = r'tal'
t_ignore = r' '


def t_error(t):
    print("Illegal character!")
    t.lexer.skip(1)


lexer = lex.lex()


def p_phrase(p):
    '''
    phrase : a QUE TAL
    '''
    print('✓✓✓ Valid phrase')


def p_a(p):
    '''
    a : HOLA COMA a
      | HOLA
    '''


def p_error(p):
    print('xxx Invalid phrase')


parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)
