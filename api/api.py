import sys
import time
import re
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# FLAGS / DEFINES
ERROR = -1
FORMAT_ERROR = -1
REGEX_QUADRATIC_EQUATION_MATCHER = r'([+-]?\d*.?\d+)\*[xX]\^0([+-]\d*.?\d+)\*[xX]\^1([+-]\d*.?\d+)\*[xX]\^2'

# CLASS
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

class Equation:
    def __init__(self, subequation1, subequation2):
        self.find_coeficients(subequation1, subequation2)
        self.find_degree()

    def find_coeficients(self, subequation1, subequation2):
        self.a0 = float(subequation1.a0 - subequation2.a0)
        self.a1 = float(subequation1.a1 - subequation2.a1)
        self.a2 = float(subequation1.a2 - subequation2.a2)

    def reduced_form(self):
        coef0 = '{:+.2f}'.format(self.a0)
        coef1 = '{:+.2f}'.format(self.a1)
        coef2 = '{:+.2f}'.format(self.a2)
        return 'Reduced form: '+coef0+' * X^0 '+coef1+' * X^1 '+coef2+' * X^2 = 0'

    def find_degree(self):
        self.degree = 0
        self.degree = 1 if self.a1 != 0 else 0
        self.degree = 2 if self.a2 != 0 else self.degree

    def print_degree(self):
        print('Degree: '+str(self.degree))

# ERROR MANAGEMENT
def exit_error(error_type):
    print(error_type + ':(')
    exit()

def check_errors(input):
    if input.find('=') == ERROR:
        exit_error(FORMAT_ERROR)

# PARSING
def find_subequation(input, index):
    return input.split('=')[index].strip().replace(' ', '')

def parse(input):
    # check_errors(input)
    subequation1 = Subequation(find_subequation(input,0))
    subequation2 = Subequation(find_subequation(input,1))
    equation = Equation(subequation1, subequation2)
    return equation

# SOLVER
def solve(equation):
    return 'equation: ' + equation

# INPUT FROM THE COMMAND LINE
def input_from_the_command_line(argv):
    if argv[0] == 'api.py' and len(argv) > 1:
        return bool(1)
    return bool(0)

if input_from_the_command_line(sys.argv):
    equation = parse(sys.argv[1])
    print(equation.reduced_form())
    equation.print_degree()
    # solution = solve(equation.sub1)
    # equation.print_eq()
    exit()

# INPUT FROM THE FRONT
app = Flask(__name__)
cors = CORS(app)

@app.route('/api/', methods = ['POST'])
def input_from_pos_request():
    data = request.get_json()
    equation = parse(data['rawEquation'])
    print(equation.reduced_form())
    equation.print_degree()
    return jsonify({
        'time': time.time(),
        'degree': equation.degree,
        'reducedForm': equation.reduced_form()
    })