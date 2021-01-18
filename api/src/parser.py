from src.classes.equation import Equation
from src.classes.subequation import Subequation

# FLAGS / DEFINES
ERROR = -1
FORMAT_ERROR = -1

# ERROR MANAGEMENT
def exit_error(error_type):
    print(error_type + ':(')
    exit()

def check_errors(input):
    if input.find('=') == ERROR:
        exit_error(FORMAT_ERROR)

# PARSING
def find_subequation(input, index):
    return input.split('=')[index].strip().replace('X', 'x').replace(' ', '')

def parse(input):
    # check_errors(input)
    subequation1 = Subequation(find_subequation(input,0))
    subequation2 = Subequation(find_subequation(input,1))
    equation = Equation(subequation1, subequation2)
    return equation