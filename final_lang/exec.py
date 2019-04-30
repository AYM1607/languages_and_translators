import ast
import sys

normalOperators = ['+', '-', '*', '/', '>', '<',
                   '<=', '>=', '==', '/=', '.and.', '.or.']

programStack = []

class VarTable:
    def __init__(self):
        self.symbols = {}

    def setVar(self, direction, value):
        realDic = 0
        if direction[0] == '$':
            realDic = int(direction[1:])
        elif direction[0] == '*':
            realDic = int(self.getVar(direction.replace('*', '$')))

        self.symbols[realDic] = value

    def getVar(self, direction):
        realDic = 0
        if direction[0] == '$':
            realDic = int(direction[1:])
        elif direction[0] == '*':
            indirectDic = int(direction[1:])
            if indirectDic in self.symbols:
                realDic = self.symbols[indirectDic]
            else:
                raise Exception(f'''
                The value at direction {indirectDic} is accessed before initialization.
                ''')

        if realDic in self.symbols:
            return self.symbols[realDic]
        else:
            raise Exception(f'''
            The value at direction {realDic} is accessed before initialization.
            ''')


# An instance of the [VarTable] class.
variables = VarTable()


def isDirection(operand):
    if type(operand) is not str:
        return False
    if len(operand) > 1 and (operand[0] == '$' or operand[0] == '*'):
        return True
    return False


def isStringLiteral(string):
    return string[0] == '\'' and string[len(string) - 1] == '\''


def splitQuad(string):
    result = []
    buffer = ''
    isStringOpen = False
    skip = False
    tokens = string.split()
    for token in tokens:
        if skip:
            skip = False
            continue
        if isStringOpen:
            buffer += ' '
            buffer += token
            if token[len(token) - 1] == '\'':
                result.append(buffer)
                isStringOpen = False
        else:
            if token[0] == '\'':
                if token == "'":
                    result.append("' '")
                    skip = True
                    continue
                if token[len(token) - 1] == '\'':
                    result.append(token)
                else:
                    buffer = token
                    isStringOpen = True
            else:
                result.append(token)
    return result


def evalOperation(operator, operand1, operand2):
    value1 = 0
    value2 = 0
    if isDirection(operand1):
        value1 = variables.getVar(operand1)
    else:
        value1 = ast.literal_eval(operand1)

    if isDirection(operand2):
        value2 = variables.getVar(operand2)
    else:
        value2 = ast.literal_eval(operand2)

    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    elif operator == '>':
        return value1 > value2
    elif operator == '<':
        return value1 < value2
    elif operator == '>=':
        return value1 >= value2
    elif operator == '<=':
        return value1 <= value2
    elif operator == '==':
        return value1 == value2
    elif operator == '/=':
        return value1 != value2
    elif operator == '.and.':
        return value1 and value2
    elif operator == '.or.':
        return value1 or value2


def execute(quads):
    # Index of the quadruplet currently being executes.
    currentQuad = 1

    while currentQuad <= len(quads):
        tokens = splitQuad(quads[currentQuad - 1])
        # ---------- print operation
        if tokens[0] == 'print':
            if tokens[1] == 'endline':
                # adding a new line
                print('')
            elif isStringLiteral(tokens[1]):
                print(tokens[1].replace('\'', ''), end='')
            else:
                value = variables.getVar(tokens[1])
                print(value, end='')
        # ---------- read operation
        elif tokens[0] == 'read':
            value = input()
            variables.setVar(tokens[1], ast.literal_eval(value))
        # ---------- arithmetic and logical operations
        elif tokens[0] in normalOperators:
            result = evalOperation(tokens[0], tokens[1], tokens[2])
            variables.setVar(tokens[3], result)
        # ---------- assign operation
        elif tokens[0] == '=':
            newValue = 0
            if isDirection(tokens[1]):
                newValue = variables.getVar(tokens[1])
            else:
                newValue = ast.literal_eval(tokens[1])
            variables.setVar(tokens[2], newValue)
        # ---------- .not. operation
        elif tokens[0] == '.not.':
            value = variables.getVar(tokens[1])
            variables.setVar(tokens[2], not value)
        # ---------- gotoF operation
        elif tokens[0] == 'gotoF':
            value = variables.getVar(tokens[1])
            if value == False:
                currentQuad = int(tokens[2])
                continue
        # ---------- gotoF operation
        elif tokens[0] == 'goto':
            currentQuad = int(tokens[1])
            continue
        elif tokens[0] == 'call':
            programStack.append(currentQuad + 1)
            currentQuad = int(tokens[1])
            continue
        elif tokens[0] == 'goback':
            newQuad = programStack.pop()
            currentQuad = newQuad
            continue
        currentQuad += 1


if (len(sys.argv) > 1):
    programName = sys.argv[1]
    programFile = open(programName, "r")
    quads = programFile.readlines()
    quads = list(map(lambda quad: quad.replace('\n', ''), quads))
    execute(quads)
    programFile.close()

else:
    raise Exception('''
    No file name was provided.
    Please add the file name as a command line argument

    Example: exec.py test.fort.out
    ''')
