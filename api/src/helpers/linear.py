## SOLVE LINEAR EQUATION --> DEGREE = 1 : A = 0 || B != 0
def linear_function(equation):
    equation.info = 'There is one real solution:'
    if equation.c == 0:
        equation.root1_r = 0
    else:
        equation.root1_r = (-1) * (equation.c / equation.b)
    return equation