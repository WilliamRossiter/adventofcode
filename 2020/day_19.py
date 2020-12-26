
import regex

class Input:
    def __init__(self, strFile):
        with open(strFile) as f:
            inputParts = f.read().split("\n\n")
            self.messages = inputParts[1].split('\n')
            inputRules = inputParts[0].split('\n')
            self.rules = {}
            for inputRule in inputRules:
                ruleParts = inputRule.split(':')
                ruleIndex = int(ruleParts[0])
                if '|' in ruleParts[1]:
                    ruleOptions = ruleParts[1].split('|')
                    ruleOption1 = ruleOptions[0]
                    ruleOption2 = ruleOptions[1]
                    self.rules[ruleIndex] = ([int(i) for i in ruleOption1.split()], [int(i) for i in ruleOption2.split()])
                elif '"' in ruleParts[1]:
                    self.rules[ruleIndex] = regex.match(r' "(\w)"', ruleParts[1])[1]
                else:
                    self.rules[ruleIndex] = [int(i) for i in ruleParts[1].split()]
    
    def GetRegex(self, rule):
        if type(rule) is str:
            return rule
        elif type(rule) is int:
            if rule == 8:
                return self.GetRegex(self.rules[rule]) + '+'
            elif rule == 11:
                regex42 = self.GetRegex(self.rules[42])
                regex31 = self.GetRegex(self.rules[31])
                return '(?P<testing>' + regex42 + regex31 + '|' + regex42 + "(?&testing)" + regex31 + ')'
            else:
                return self.GetRegex(self.rules[rule])
        elif type(rule) is list:
            regexCur = ''
            for rulePart in rule:
                regexCur += self.GetRegex(rulePart)
            return '(?:' + regexCur + ')'
        elif type(rule) is tuple:
            return '(?:' + self.GetRegex(rule[0]) + '|' + self.GetRegex(rule[1]) + ')'

input = Input('2020/input/day_19.txt')
numValid = 0
regexString = input.GetRegex(0)
print(regexString)
regexCompiled = regex.compile("^" + regexString + "$")
for message in input.messages:
    if regexCompiled.match(message):
        numValid += 1
print(numValid)