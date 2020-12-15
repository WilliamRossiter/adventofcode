
def GetInput(strFile):
    input = []
    with open(strFile) as f:
        for ch in f.read().split(','):
            input.append(int(ch))
    return input

def PlayGame(input, cTurnStop):
    cTurn = 0
    history = {}
    numberLast = 0
    while cTurn < cTurnStop:
        if cTurn < len(input):
            history[input[cTurn]] = [cTurn]
            numberLast = input[cTurn]
        else:
            numberCompute = 0
            historyNumber = history[numberLast]
            if (len(historyNumber) == 1):
                numberCompute = 0
            else:
                numberCompute = historyNumber[-1] - historyNumber[-2]
            if numberCompute in history:
                history[numberCompute].append(cTurn)
                if (len(history[numberCompute]) > 2):
                    history[numberCompute].pop(0)
            else:
                history[numberCompute] = [cTurn]
            numberLast = numberCompute
        cTurn += 1
    return numberLast

def Main(strFile):
    input = GetInput(strFile)
    print(PlayGame(input, 30000000))

Main('2020/input/day_15.txt')