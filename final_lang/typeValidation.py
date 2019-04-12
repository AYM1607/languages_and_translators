typeValidationMap = {
    '*': {
        'integer': {
            'integer': 'integer',
            'real': 'real',
        },
        'real': {
            'integer': 'real',
            'real': 'real'
        },
    },
    '+': {
        'integer': {
            'integer': 'integer',
            'real': 'real',
        },
        'real': {
            'integer': 'real',
            'real': 'real'
        },
    },
    '-': {
        'integer': {
            'integer': 'integer',
            'real': 'real',
        },
        'real': {
            'integer': 'real',
            'real': 'real'
        },
    },
    '/': {
        'integer': {
            'integer': 'integer',
            'real': 'real',
        },
        'real': {
            'integer': 'real',
            'real': 'real'
        },
    },
    '>': {
        'integer': {
            'integer': 'bool',
            'real': 'bool',
        },
        'real': {
            'integer': 'bool',
            'real': 'bool'
        },
    },
    '<': {
        'integer': {
            'integer': 'bool',
            'real': 'bool',
        },
        'real': {
            'integer': 'bool',
            'real': 'bool'
        },
    },
    '>=': {
        'integer': {
            'integer': 'bool',
            'real': 'bool',
        },
        'real': {
            'integer': 'bool',
            'real': 'bool'
        },
    },
    '<=': {
        'integer': {
            'integer': 'bool',
            'real': 'bool',
        },
        'real': {
            'integer': 'bool',
            'real': 'bool'
        },
    },
    '==': {
        'integer': {
            'integer': 'bool',
            'real': 'bool',
        },
        'real': {
            'integer': 'bool',
            'real': 'bool'
        },
    },
    '/=': {
        'integer': {
            'integer': 'bool',
            'real': 'bool',
        },
        'real': {
            'integer': 'bool',
            'real': 'bool'
        },
    },
    '=': {
        'integer': {
            'integer': 'integer',
        },
        'real': {
            'integer': 'real',
            'real': 'real',
        },
        'bool': {
            'bool': 'bool',
        }
    },
    '.and.': {
        'bool': {
            'bool': 'bool',
        }
    },
    '.or.': {
        'bool': {
            'bool': 'bool',
        }
    },
}

def resultingType(operator, type1, type2):
    operatorMap = typeValidationMap[operator]
    if type1 in operatorMap:
        type1Map = operatorMap[type1]
        if type2 in type1Map:
            return type1Map[type2]
        else:
            raise Exception(f'''
            Operation not suppoerted:
            
            operator {operator} can't be used with types: {type1} and {type2}
            ''')
    else:
        raise Exception(f'''
        Operation not supported:

        operator {operator} can't be used with types: {type1} and {type2}
        ''')