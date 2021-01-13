import sys
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from src.parser import parse
from src.solver import solve

# INPUT FROM THE COMMAND LINE
def input_from_the_command_line(argv):
    if argv[0] == 'api.py' and len(argv) > 1:
        return bool(1)
    return bool(0)

if input_from_the_command_line(sys.argv):
    equation = parse(sys.argv[1])
    # print(equation.reduced_form())
    # equation.print_degree()
    solution = solve(equation)
    # equation.print_eq()
    print(solution)
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
        # 'time': time.time(),
        'degree': equation.degree,
        'reducedForm': equation.reduced_form()
    })