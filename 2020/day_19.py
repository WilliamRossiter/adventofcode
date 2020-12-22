
import re

class Input:
    def __init__(self, strFile):
        with open(strFile) as f:
            inputParts = f.read().split("\n\n")
            self.messages = inputParts[1].split('\n')
            inputRules = inputParts[0].split('\n')
            self.rules = {}
            for inputRule in inputRules:
                match = re.match("(\d+): (\d+) (\d+) \| (\d+) (\d)+", inputRule)
                if match != None:
                    self.rules[int(match[1])] = [(int(match[2]), int(match[3])), (int(match[4]), int(match[5]))]
                    continue
                match = re.match("(\d+): (\d+) (\d+) (\d+)", inputRule)
                if match != None:
                    self.rules[int(match[1])] = (int(match[2]), int(match[3]), int(match[4]))
                    continue  
                match = re.match("(\d+): (\d+) (\d+)", inputRule)
                if match != None:
                    self.rules[int(match[1])] = (int(match[2]), int(match[3]))
                    continue
                match = re.match("(\d+): (\d+)", inputRule)
                if match != None:
                    self.rules[int(match[1])] = int(match[2])
                    continue
                match = re.match("(\d+): \"(\w)\"", inputRule)
                if match != None:
                    self.rules[int(match[1])] = match[2]
                    continue

    def IsValidMessageForRuleIndex(self, message, ruleIndex):
        rule = self.rules[0]
        self.IsValidMessageForRule(message, rule)
    
    def MatchRule(self, message, messageIndex, rule):
        if (messageIndex >= len(message)):
            return 0
        elif type(rule) is str:
            if (message[messageIndex] == rule):
                return 1
            else:
                return 0
        elif type(rule) is int:
            ruleIndex = rule
            return self.MatchRule(message, messageIndex, self.rules[ruleIndex])
        elif type(rule) is tuple:
            messageIndexRecursive = messageIndex
            for ruleIndexRecursive in rule:
                matchCount = self.MatchRule(message, messageIndexRecursive, self.rules[ruleIndexRecursive])
                if matchCount == 0:
                    return 0
                messageIndexRecursive += matchCount
            return messageIndexRecursive - messageIndex
        elif type(rule) is list:
            matchCount = 0
            for ruleOption in rule:
                matchCount = self.MatchRule(message, messageIndex, ruleOption)
                if matchCount != 0:
                    break
            return matchCount

input = Input('2020/input/day_19.txt')
numValid = 0
for message in input.messages:
    if input.MatchRule(message, 0, input.rules[0]) == len(message):
        numValid += 1
print(numValid)