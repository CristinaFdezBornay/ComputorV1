try:
    import sys
    from flask import Flask, request, jsonify
    from flask_cors import CORS, cross_origin
    from src.parser import parse
    from src.solver import solve
    from src.displayer import display
except:
    print('===============================================')
    print('')
    print('Import error, please run:')
    print('python3 -m venv venv && \\')
    print('venv/bin/pip3 install -r requirements.txt && \\')
    print('source venv/bin/activate')
    print('')
    print('===============================================')
    exit()

# INPUT FROM THE COMMAND LINE
def input_from_the_command_line(argv):
    try:
        if argv[0] == 'api.py' and len(argv) > 1:
            return bool(1)
        return bool(0)
    except:
        return bool(0)

if input_from_the_command_line(sys.argv):
    try:
        equation = parse(sys.argv[1])
        if equation == 'ERROR':
            print('\n[ERROR]: There has been an error while processing the input.')
            print('Please verify:')
            print('\t- There are no negative exponents')
            print('\t- All the terms are well formatted\n')
        else:
            solution = solve(equation)
            display(equation)
    except:
        print('\n[ERROR]\n')
    exit()

# INPUT FROM THE FRONT
app = Flask(__name__)
cors = CORS(app)

@app.route('/api/', methods = ['POST'])
def input_from_pos_request():
    try:
        data = request.get_json()
        equation = parse(data['rawEquation'])
        if equation == 'ERROR':
            return jsonify({ 'error': 'ERROR'})
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
    except:
        return jsonify({ 'error': 'ERROR'})