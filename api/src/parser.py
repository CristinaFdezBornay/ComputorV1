from src.classes.equation import Equation
from src.classes.subequation import Subequation

def checkCorrectCharacters(str, set):
    for c in str:
        if set.count(c) == 0:
            return 'ERROR'

def check_errors(input):  
    if input.count('=') != 1 or checkCorrectCharacters(input, '0123456789xX*^= ') == 'ERROR':
        return 'ERROR'

# PARSING
def find_subequation(input, index):
    return input.split('=')[index].strip().replace('X', 'x').replace(' ', '')

def parse(input):
    check_errors(input)
    subequation1 = Subequation(find_subequation(input,0))
    subequation2 = Subequation(find_subequation(input,1))
    if subequation1.error == 0 and subequation2.error == 0:
        equation = Equation(subequation1, subequation2)
        if equation.error == 0:
            return equation
    else:
        return 'ERROR'