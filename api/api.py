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
    if equation == 'ERROR':
        print('INPUT ERROR')
        exit()
    solution = solve(equation)
    if solution == 'ERROR':
        print('PROCESS ERROR')
        exit()
    display(equation)
    exit()

# INPUT FROM THE FRONT
app = Flask(__name__)
cors = CORS(app)

@app.route('/api/', methods = ['POST'])
def input_from_pos_request():
    data = request.get_json()
    equation = parse(data['rawEquation'])
    if equation == 'ERROR':
        return jsonify({error: 'INPUT ERROR'})
    solution = solve(equation)
    return jsonify({
        'a': solution.a,
        'b': solution.b,
        'c': solution.c,
        'reducedForm': solution.find_reduced_form(),
        'degree': solution.find_degree(),
        'discriminant': solution.find_discriminant(),
        'info': solution.info,
        'root1_r': solution.root1_r,
        'root1_i': solution.root1_i,
        'root2_r': solution.root2_r,
        'root2_i': solution.root2_i,
    })