from src.helpers.simple import simple_function
from src.helpers.linear import linear_function
from src.helpers.quadratic import quadratic_fuction

def solve(equation):
    try:
        if equation.degree == 0:
            return simple_function(equation)
        elif equation.degree == 1:
            return linear_function(equation)
        elif equation.degree == 2:
            return quadratic_fuction(equation)
    except:
        print('\nERROR\n')