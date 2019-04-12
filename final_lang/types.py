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
}

def resultingType(operator, type1, type2):
    operatorMap = typeValidationMap[operator]
    if type1 in operatorMap:
        type1Map = operatorMap[type1]
        if type2 in type1Map:
            return type1Map[type2]
        else:
            raise Exception('Operation not suppoerted')
    else:
        raise Exception('Operation not supported')