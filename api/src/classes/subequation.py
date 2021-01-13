import re

REGEX_QUADRATIC_EQUATION_MATCHER = r'([+-]?\d*.?\d+)\*[xX]\^0([+-]\d*.?\d+)\*[xX]\^1([+-]\d*.?\d+)\*[xX]\^2'

class Subequation:
    def __init__(self, subequation):
        self.subequation = subequation
        self.find_coeficients()
    
    def find_coeficients(self):
        matcher = re.compile(REGEX_QUADRATIC_EQUATION_MATCHER)
        coeficients = matcher.match(self.subequation)
        self.a0 = float(coeficients.group(1))
        self.a1 = float(coeficients.group(2))
        self.a2 = float(coeficients.group(3))
    
    def print_subequation(self):
        print('sub: ' + self.subequation)
        print('sub a0: ' + str(self.a0))
        print('sub a1: ' + str(self.a1))
        print('sub a2: ' + str(self.a2))
