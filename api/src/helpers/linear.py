## SOLVE LINEAR EQUATION --> DEGREE = 1 : A = 0 || B != 0
def linear_function(equation):
    equation.info = 'The solution is:'
    if equation.c == 0:
        equation.root1_r = 0
    else:
        equation.root1_r = (-1) * (equation.c / equation.b)