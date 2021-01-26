## Square root
def sqrt(number):
    return number ** 0.5

## DEGREE = 2 : A != 0 || B != 0 || C != 0
def solve_quadratic_complete(equation):
    if equation.discriminant > 0:
        equation.info = 'Discriminant is strictly positive, the two real solutions are:'
        equation.root1_r = (-equation.b + sqrt(equation.discriminant)) / (2 * equation.a)
        equation.root2_r = (-equation.b - sqrt(equation.discriminant)) / (2 * equation.a)
    elif equation.discriminant < 0:
        equation.info = 'Discriminant is negative, the two imaginary solutions are:'
        equation.root1_r = -equation.b / (2 * equation.a)
        equation.root1_i = sqrt(-equation.discriminant)
        equation.root2_r = -equation.b / (2 * equation.a)
        equation.root2_i = -sqrt(-equation.discriminant)
    else:
        equation.info = 'Discriminant is zero, the solution is:'
        equation.root1_r = (-equation.b) / (2 * equation.a)
        equation.root2_r = (-equation.b) / (2 * equation.a)
    return equation

## DEGREE = 2 : A != 0 || B == 0 || C != 0
def solve_quadratic_incomplete_b(equation):
    if equation.discriminant > 0:
        equation.info = 'Discriminant is strictly positive, the two real solutions are:'
        equation.root1_r = sqrt(equation.discriminant) / (2 * equation.a)
        equation.root2_r = -sqrt(equation.discriminant) / (2 * equation.a)
    elif equation.discriminant < 0:
        equation.info = 'Discriminant is negative, the two imaginary solutions are:'
        equation.root1_i = sqrt(-equation.discriminant)
        equation.root2_i = -sqrt(-equation.discriminant)
    return equation

## DEGREE = 2 : A != 0 || B != 0 || C == 0
def solve_quadratic_incomplete_c(equation):
    equation.info = 'Discriminant is strictly positive, the two real solutions are:'
    equation.root1_r = 0
    equation.root2_r = -1 * (equation.b / equation.a)
    return equation

## DEGREE = 2 : A != 0 || B == 0 || C == 0
def solve_quadratic_incomplete_b_and_c(equation):
    equation.info = 'Discriminant is strictly positive, the solution is:'
    equation.root1_r = 0
    return equation

## SOLVE QUADRATIC EQUATION --> DEGREE = 2 : A != 0
def quadratic_fuction(equation):
    if equation.b != 0 and equation.c != 0:
        return solve_quadratic_complete(equation)
    if equation.b == 0 and equation.c !=0:
        return solve_quadratic_incomplete_b(equation)
    if equation.b != 0 and equation.c ==0:
        return solve_quadratic_incomplete_c(equation)
    if equation.b == 0 and equation.c ==0:
        return solve_quadratic_incomplete_b_and_c(equation)