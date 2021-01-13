import sys
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from src.parser import parse
from src.solver import solve
from src.displayer import display

# INPUT FROM THE COMMAND LINE
def input_from_the_command_line(argv):
    if argv[0] == 'api.py' and len(argv) > 1:
        return bool(1)
    return bool(0)

if input_from_the_command_line(sys.argv):
    parse(sys.argv[1])
    equation = parse(sys.argv[1])
    solution = solve(equation)
    display(equation)
    exit()

# INPUT FROM THE FRONT
app = Flask(__name__)
cors = CORS(app)

@app.route('/api/', methods = ['POST'])
def input_from_pos_request():
    data = request.get_json()
    equation = parse(data['rawEquation'])
    solution = solve(equation)
    return jsonify({
        'a': equation.a,
        'b': equation.b,
        'c': equation.c,
        'reducedForm': equation.reducedForm,
        'degree': equation.degree,
        'discriminant': equation.discriminant,
        'info': equation.info,
        'root1_r': equation.root1_r,
        'root1_i': equation.root1_i,
        'root2_r': equation.root2_r,
        'root2_i': equation.root2_i,
    })