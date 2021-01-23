def display_reduced_form(equation):
    print('Reduced form\t\t: '+equation.reduced_form)

def display_degree(equation):
    print('Polynomial degree\t: '+str(equation.degree))

def display_discriminant(equation):
    if equation.degree == 2:
        print('Δ = b² - 4ac\t\t: {:+.2f}'.format(equation.discriminant).rstrip('0').rstrip('.'))

def display_solution(equation):
    print(equation.info)
    solution = ''
    if equation.root1_r != 'null' or equation.root1_i != 'null':
        solution += '\tx₁:'
        if equation.root1_r != 'null':
            solution += ' {:+.4f}'.format(equation.root1_r).rstrip('0').rstrip('.')
        if equation.root1_i != 'null':
            solution += ' {:+.4f}i'.format(equation.root1_i).rstrip('0').rstrip('.')
        solution += '\n'
    if equation.root2_r != 'null' or equation.root2_i != 'null':
        solution += '\tx₂:'
        if equation.root2_r != 'null':
            solution += ' {:+.4f}'.format(equation.root2_r).rstrip('0').rstrip('.')
        if equation.root2_i != 'null':
            solution += ' {:+.4f}i'.format(equation.root2_i).rstrip('0').rstrip('.')
    print(solution)

def display(equation):
    print()
    display_reduced_form(equation)
    display_degree(equation)
    display_discriminant(equation)
    print()
    display_solution(equation)