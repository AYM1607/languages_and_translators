import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'program',
    'id',
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
]