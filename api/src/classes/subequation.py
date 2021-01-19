import re

REGEX_EQUATION=r'(([+-][0-9]*(\.[0-9]+)?)(\*?x{1}\^?([0-9])?)?)'

class Subequation:
    def __init__(self, subequation):
        self.subequation = subequation
        self.error = 0
        self.find_coeficients()

    def find_coeficients(self):
        if (self.subequation[0] != '-' and self.subequation[0] != '+'):
            self.subequation = '+'+self.subequation
        matches = re.findall(REGEX_EQUATION, self.subequation)
        self.a = 0
        self.b = 0
        self.c = 0
        error_check = ''
        for match in matches:
            error_check += match[0]
            if match[3] == '':
                self.c += float(match[1])
            elif match[3] == '*x' or match[3] == 'x':
                self.b += float(match[1])
            elif match[3] == '*x^0' or match[3] == '*x0' or match[3] == 'x^0' or match[3] == 'x0':
                self.c += float(match[1])
            elif match[3] == '*x^1' or match[3] == '*x1' or match[3] == 'x^1' or match[3] == 'x1':
                self.b += float(match[1])
            elif match[3] == '*x^2' or match[3] == '*x2' or match[3] == 'x^2' or match[3] == 'x2':
                self.a += float(match[1])
            elif float(match[4]) > 2:
                self.error = 1
        if error_check != self.subequation:
            self.error = 1
   
    def print_subequation(self):
        print('sub: ' + self.subequation)
        print('sub a: ' + str(self.a))
        print('sub b: ' + str(self.b))
        print('sub c: ' + str(self.c))
