from src.helpers.simple import simple_funciton
from src.helpers.linear import linear_function
from src.helpers.quadratic import quadratic_fuction

def solve(equation):
    if equation.degree == 0:
        simple_funciton(equation)
    elif equation.degree == 1:
        linear_function(equation)
    elif equation.degree == 2:
        quadratic_fuction(equation)
    elif equation.degree > 2:
        equation.info = 'The polynomial degree is strictly greater than 2, I cannot solve this.'
    else:
        equation.info = 'Beloved human, what are you giving me?'