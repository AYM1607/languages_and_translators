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

def resultingType(operator, operand1, operand2):
    operatorMap = typeValidationMap[operator]
    if operand1 in operatorMap:
        operand1Map = operatorMap[operand1]
        if operand2 in operand1Map:
            return operand1Map[operand2]
        else:
            raise Exception('Operation not suppoerte')
    else:
        raise Exception('Operation not supported')