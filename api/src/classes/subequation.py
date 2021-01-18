import re

REGEX_EQUATION=r'(([+-]\d*\.?\d+)(\*?x{1}\^?([0-9])?)?)' # 5.x WRONG
# REGEX_EQUATION=r'(([+-]\d*\.?\d+)*(\*?x{1}(\^([0-9]))?)?)'
# REGEX_EQUATION=r'(([+-]?\d+(\.\d+)?)\*?((x{1}\^[0-9])|(x)))|([+-]?\d+(\.\d+)?)|(([+-])?(x{1}(\^([0-9]))?))'
# REGEX_QUADRATIC_EQUATION_MATCHER = r'([+-]?\d*.?\d+\*x\^0)?([+-]\d*.?\d+\*x\^1)?([+-]\d*.?\d+\*x\^2)?([+-]\d*.?\d+\*x\^\d)?'
# REGEX_QUADRATIC_EQUATION_MATCHER = r'([+-]?\d*.?\d+\*x\^0)?([+-]\d*.?\d+\*x\^1)?([+-]\d*.?\d+\*x\^2)?'

class Subequation:
    def __init__(self, subequation):
        self.subequation = subequation
        self.find_coeficients2()
        self.error = 0

    def find_coeficients2(self):
        if (self.subequation != '-*' and self.subequation != '+*'):
            self.subequation = '+'+self.subequation
        print(self.subequation)
        matches = re.findall(REGEX_EQUATION, self.subequation)
        self.a = 0
        self.b = 0
        self.c = 0
        for match in matches:
            if match[2] == '':
                self.c += float(match[1])
            elif match[2] == '*x' or match[2] == 'x':
                self.b += float(match[1])
            elif match[2] == '*x^0' or match[2] == '*x0' or match[2] == 'x^0' or match[2] == 'x0':
                self.c += float(match[1])
            elif match[2] == '*x^1' or match[2] == '*x1' or match[2] == 'x^1' or match[2] == 'x1':
                self.b += float(match[1])
            elif match[2] == '*x^2' or match[2] == '*x2' or match[2] == 'x^2' or match[2] == 'x2':
                self.a += float(match[1])
            print(match)
        # CRISTINA YOU HAVE TO MANAGE HIGHER DEGREES
        self.print_subequation()
        exit()        
    
    def find_coeficients(self):
        matcher = re.compile(REGEX_QUADRATIC_EQUATION_MATCHER)
        coeficients = matcher.match(self.subequation)
        self.a = 0
        self.b = 0
        self.c = 0
        for x in range (1, self.subequation.count('x') + 1):
            if coeficients.group(x).count('*x^2'):
                self.a += float(coeficients.group(x).replace('*x^2', ''))
            elif coeficients.group(x).count('*x^1'):
                self.b += float(coeficients.group(x).replace('*x^1', ''))
            elif coeficients.group(x).count('*x^0'):
                self.c += float(coeficients.group(x).replace('*x^0', ''))
            else:
                print('FORMAT ERROR:\tThis term ('+coeficients.group(x)+') is badly formated or the degree is not 0, 1 or 2')
                print('\t\tI am gonna continue calculating with the valid terms because I am very nice :D')
    
    def print_subequation(self):
        print('sub: ' + self.subequation)
        print('sub a: ' + str(self.a))
        print('sub b: ' + str(self.b))
        print('sub c: ' + str(self.c))
