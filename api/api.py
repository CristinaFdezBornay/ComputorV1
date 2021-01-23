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
    equation = parse(sys.argv[1])
    if equation == 'ERROR':
        print('INPUT ERROR')
    elif equation == 'DEGREE HIGHER THAN 2 ERROR':
        print('\nThe polynomial degree is strictly greater than 2, I can\'t solve.\n')
    else:
        solution = solve(equation)
        if solution == 'ERROR':
            print('PROCESS ERROR')
        else:
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
        return jsonify({ 'error': 'INPUT ERROR'})
    solution = solve(equation)
    root1_r = 'null' if solution.root1_r == 'null' else '  {:+.3f}'.format(solution.root1_r).rstrip('0').rstrip('.')
    root1_i = 'null' if solution.root1_i == 'null' else '  {:+.3f}'.format(solution.root1_i).rstrip('0').rstrip('.')
    root2_r = 'null' if solution.root2_r == 'null' else '  {:+.3f}'.format(solution.root2_r).rstrip('0').rstrip('.')
    root2_i = 'null' if solution.root2_i == 'null' else '  {:+.3f}'.format(solution.root2_i).rstrip('0').rstrip('.')
    return jsonify({
        'a': solution.a,
        'b': solution.b,
        'c': solution.c,
        'reducedForm': solution.reduced_form,
        'degree': solution.degree,
        'discriminant': solution.discriminant,
        'info': solution.info,
        'root1_r': root1_r,
        'root1_i': root1_i,
        'root2_r': root2_r,
        'root2_i': root2_i,
    })