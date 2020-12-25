
import re

class Input:
    def __init__(self, strFile):
        with open(strFile) as f:
            inputParts = f.read().split("\n\n")
            self.messages = inputParts[1].split('\n')
            inputRules = inputParts[0].split('\n')
            self.rules = {}
            self.regex = ""
            # ugh, this is gross and is a result of being impatient. Tokenization would make more sense
            for inputRule in inputRules:
                match = re.match("(\d+): (\d+) (\d+) \| (\d+) (\d+)", inputRule)
                if match != None:
                    self.rules[int(match[1])] = ([int(match[2]), int(match[3])], [int(match[4]), int(match[5])])
                    continue
                match = re.match("(\d+): (\d+) \| (\d+)", inputRule)
                if match != None:
                    self.rules[int(match[1])] = (int(match[2]), int(match[3]))
                    continue
                match = re.match("(\d+): (\d+) (\d+) (\d+)", inputRule)
                if match != None:
                    self.rules[int(match[1])] = [int(match[2]), int(match[3]), int(match[4])]
                    continue  
                match = re.match("(\d+): (\d+) (\d+)", inputRule)
                if match != None:
                    self.rules[int(match[1])] = [int(match[2]), int(match[3])]
                    continue
                match = re.match("(\d+): (\d+)", inputRule)
                if match != None:
                    self.rules[int(match[1])] = int(match[2])
                    continue
                match = re.match("(\d+): \"(\w)\"", inputRule)
                if match != None:
                    self.rules[int(match[1])] = match[2]
                    continue
    
    def PrintRuleToRegex(self, rule):
        if type(rule) is str:
            self.regex += rule
        elif type(rule) is int:
            self.PrintRuleToRegex(self.rules[rule])
        elif type(rule) is list:
            self.regex += "(?:"
            for rulePart in rule:
                self.PrintRuleToRegex(rulePart)
            self.regex += ")"
        elif type(rule) is tuple:
            self.regex += '(?:'
            self.PrintRuleToRegex(rule[0])
            self.regex += '|'
            self.PrintRuleToRegex(rule[1])
            self.regex += ')'

input = Input('2020/input/day_19.txt')
for key in input.rules.keys():
    print(key)
    print(input.rules[key])
numValid = 0
input.PrintRuleToRegex(0)
print(input.regex)
for message in input.messages:
    regex = re.compile("^" + input.regex + "$")
    if regex.match(message):
        numValid += 1
print(numValid)