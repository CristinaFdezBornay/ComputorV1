## SOLVE LINEAR EQUATION --> DEGREE = 1 : A = 0 || B = 0
def simple_function(equation):
    if equation.c != 0:
        equation.info = 'Beloved human, your beloved number cannot be zero.'
    else:
        equation.info = 'Every real number is a possible solution of this equation.'
    return equation