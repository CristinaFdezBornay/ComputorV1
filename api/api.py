import sys
import time
import re
from flask import Flask

# FLAGS
ERROR = -1
FORMAT_ERROR = -1

# CLASS
class Equation:
    sub1 = ''
    sub2 = ''
    sub1_a0 = 0
    sub1_a1 = 0
    sub1_a2 = 0
    sub2_a0 = 0
    sub2_a1 = 0
    sub2_a2 = 0
    a0 = 0
    a1 = 0
    a2 = 0

    def reduce_equation(self):
        self.a0 = float(self.sub1_a0 - self.sub2_a0)
        self.a1 = float(self.sub1_a1 - self.sub2_a1)
        self.a2 = float(self.sub1_a2 - self.sub2_a2)

    def print_eq(self):
        print('sub1: ' + self.sub1)
        print('sub1 a0: ' + str(self.sub1_a0))
        print('sub1 a1: ' + str(self.sub1_a1))
        print('sub1 a2: ' + str(self.sub1_a2))
        print('sub2: ' + self.sub2)
        print('sub2 a0: ' + str(self.sub2_a0))
        print('sub2 a1: ' + str(self.sub2_a1))
        print('sub2 a2: ' + str(self.sub2_a2))
        print('a0: ' + str(self.a0))
        print('a1: ' + str(self.a1))
        print('a2: ' + str(self.a2))

# ERROR MANAGEMENT
def exit_error(error_type):
    print(error_type + ':(')
    exit()

def check_errors(input):
    if input.find('=') == ERROR:
        exit_error(FORMAT_ERROR)

# PARSING
def find_subequations(input, equation):
    equation.sub1 = input.split('=')[0].strip()
    equation.sub2 = input.split('=')[1].strip()

def format_subequations(equation):
    equation.sub1 = equation.sub1.replace(' ', '')
    if (equation.sub1.count('+') + equation.sub1.count('-') < equation.sub1.count('X')):
        equation.sub1 = '+ ' + equation.sub1
    equation.sub2 = equation.sub2.replace(' ', '')
    if (equation.sub2.count('+') + equation.sub2.count('-') < equation.sub2.count('X')):
        equation.sub2 = '+' + equation.sub2

def find_coeficients(subequation):
    quadratic_equation_matcher = re.compile(r'([+-]? ?\d*.?\d+) ?\* ?X\^0 ?([+-] ?\d*.?\d+) ?\* ?X\^1 ?([+-] ?\d*.?\d+) ?\* ?X\^2')
    matches = quadratic_equation_matcher.match(subequation)
    return matches

def find_coeficients_subequations(equation):
    coef = find_coeficients(equation.sub1)
    equation.sub1_a0 = float(coef.group(1))
    equation.sub1_a1 = float(coef.group(2))
    equation.sub1_a2 = float(coef.group(3))
    coef = find_coeficients(equation.sub2)
    equation.sub2_a0 = float(coef.group(1))
    equation.sub2_a1 = float(coef.group(2))
    equation.sub2_a2 = float(coef.group(3))

def parse(input):
    # check_errors(input)
    equation = Equation()
    find_subequations(input, equation)
    format_subequations(equation)
    find_coeficients_subequations(equation)
    return equation

# PRINT REDUCED EQUATION
def print_reduced_equation(equation):
    coef0 = '{:+.2f}'.format(equation.a0)
    coef1 = '{:+.2f}'.format(equation.a1)
    coef2 = '{:+.2f}'.format(equation.a2)
    print('Reduced form: '+coef0+' * X^0 '+coef1+' * X^1 '+coef2+' * X^2 = 0')

# SOLVER
def solve(equation):
    return 'equation: ' + equation

# CHECK INPUT COMMAND LINE
if len(sys.argv) > 1 :
    equation = parse(sys.argv[1])
    equation.reduce_equation()
    print_reduced_equation(equation)
    # solution = solve(equation.sub1)
    # equation.print_eq()
    exit()

# CHECK INPUT FRONT
app = Flask(__name__)
@app.route('/time')
def get_current_time():
    return {'time': time.time()}
