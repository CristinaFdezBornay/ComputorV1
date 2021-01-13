from src.classes.equation import Equation

def simple_funciton(equation):
    print("simple")
    return equation

def linear_function(equation):
    print("linear")
    return equation

def quadratic_fuction(equation):
    print("quadratic")
    return equation

# SOLVER
def solve(equation):
    if equation.degree == 0:
        simple_funciton(equation)
    elif equation.degree == 1:
        linear_function(equation)
    elif equation.degree == 2:
        quadratic_fuction(equation)
    return 'degree: ' + str(equation.degree)


## EX

# python3 api.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0 + 2 * X^1 - 5 * X^2"
# python3 api.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0 + 2 * X^1 - 9.3 * X^2"
# python3 api.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0 + 4 * X^1 - 9.3 * X^2"