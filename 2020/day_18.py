

class Input:
    def __init__(self, strFile):
        self.equations = []
        with open(strFile) as f:
            self.equations = f.read().split('\n')

class Static:
    indexCur = 0
    sum = 0

def GetNextResult(equation):
    if Static.indexCur >= len(equation):
        return 0
    elif equation[Static.indexCur] == '(':
        return EvaluateEquation(equation)
    else:
        token = equation[Static.indexCur]
        Static.indexCur += 1
        return int(token)

def GetNextOperation(equation):
    token = equation[Static.indexCur]
    Static.indexCur += 1
    return token

def EvaluateEquation(equation):
    Static.indexCur += 1
    resultLeft = GetNextResult(equation)
    while equation[Static.indexCur] != ')':
        operation = GetNextOperation(equation)
        resultRight = GetNextResult(equation)
        if (operation == '+'):
            resultLeft = resultLeft + resultRight
        else:
            resultLeft = resultLeft * resultRight
    Static.indexCur += 1
    return resultLeft

def ParenthesizeEquation(equation, operator):
    iCh = 0
    while iCh < len(equation):
        ch = equation[iCh]
        if (ch == operator):
            iChFirst = iCh - 1
            iChLast = iCh + 1
            cParen = 0
            while iChFirst >= 0:
                ch = equation[iChFirst]
                if (ch == ')'):
                    cParen += 1
                elif (ch == '('):
                    cParen -= 1
                if (cParen == 0):
                    break
                iChFirst -= 1
            cParen = 0
            while iChLast < len(equation):
                ch = equation[iChLast]
                if (ch == '('):
                    cParen += 1
                elif (ch == ')'):
                    cParen -= 1
                if (cParen == 0):
                    break
                iChLast += 1
            equation.insert(iChLast + 1, ')')
            equation.insert(iChFirst, '(')
            iCh += 1
        iCh += 1

input = Input('2020/input/day_18.txt')

for equation in input.equations:
    Static.indexCur = 0
    equationStripped = '(' + "".join(equation.split()) + ')'
    equationListified = list(equationStripped)
    ParenthesizeEquation(equationListified, '+')
    Static.sum += GetNextResult(equationListified)
print(Static.sum)