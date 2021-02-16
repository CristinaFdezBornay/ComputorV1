from src.classes.equation import Equation
from src.classes.subequation import Subequation
from src.helpers.manage_higher_exponents import manage_higher_exponent

def checkCorrectCharacters(input):
    admitedCharacters = '0123456789xX*^=+-. '
    for c in input:
        if admitedCharacters.count(c) == 0:
            return 'ERROR'

def check_errors(input):
    try:
        if input.count('=') == 0:
            return input + ' = 0'
        if input.count('=') > 1:
            return 'ERROR'
        if checkCorrectCharacters(input) == 'ERROR':
            return 'ERROR'
        if input.count('^-') != 0 or input.count('^ -') != 0:
            print('\n[INFO]: The exponent is negative, I can\'t solve\n')
            return 'ERROR'
        return input
    except:
        return 'ERROR'

# PARSING
def find_subequation(input, index):
    return input.split('=')[index].strip().replace('X', 'x').replace(' ', '').replace('^+', '^')

def parse(input):
    try:
        input = check_errors(input)
        if input == 'ERROR':
            return 'ERROR'
        subequation1 = Subequation(find_subequation(input,0))
        subequation2 = Subequation(find_subequation(input,1))
        if subequation1.degree_higher_than_2 == 1 or subequation2.degree_higher_than_2 == 1:
            return manage_higher_exponent(subequation1, subequation2)
        elif subequation1.error != 0 or subequation2.error != 0:
            return 'ERROR'
        equation = Equation(subequation1, subequation2)
        if equation.error != 0:
            return 'ERROR'
        return equation
    except:
        return 'ERROR'