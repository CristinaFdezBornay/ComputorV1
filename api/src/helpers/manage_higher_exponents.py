import re
from src.classes.subequation import Subequation
from src.classes.equation import Equation

REGEX_EQUATION=r'(([+-][0-9]*(\.[0-9]+)?)(\*?x{1}\^?([0-9]*))?)'

class Coeficients():
    def __init__(self, coeficient, exponent):
        self.coeficient = coeficient
        self.exponent = exponent

def find_all_coeficients(equation):
    try:
        matches = re.findall(REGEX_EQUATION, equation)
        coeficients = []
        for match in matches:
            if match[3] == '':
                coeficients.append(Coeficients(float(match[1]), 0))
            elif match[3] == '*x' or match[3] == 'x':
                coeficients.append(Coeficients(float(match[1]), 1))
            else:
                coeficients.append(Coeficients(float(match[1]), int(match[4])))
        return coeficients
    except:
        return []

def find_final_coeficients(coeficients):
    try:
        final_coeficients = []
        for coef in coeficients:
            for final_coef in final_coeficients:
                if coef.exponent == final_coef.exponent:
                    final_coef.coeficient = final_coef.coeficient + coef.coeficient
                    coef.exponent = 'null'
            if coef.exponent != 'null':
                final_coeficients.append(Coeficients(coef.coeficient, coef.exponent))
        return final_coeficients
    except:
        return []

def find_degree(final_coeficients):
    try:
        degree = 0
        for final_coef in final_coeficients:
            if final_coef.coeficient != 0 and final_coef.exponent > degree:
                degree = final_coef.exponent
        return degree
    except:
        return 3

def sort_coefinicients(final_coeficients):
    try:
        exponents = []
        for final_coef in final_coeficients:
            exponents.append(final_coef.exponent)
        min_exponent = min(exponents)
        exponents.sort()
        sorted_coefinicients = []
        for i in exponents:
            for final_coef in final_coeficients:
                if final_coef.exponent == i:
                    sorted_coefinicients.append(final_coef)
        return sorted_coefinicients
    except:
        return []

def manage_higher_exponent(subequation1, subequation2):
    try:
        subequation2.subequation = subequation2.subequation.replace('+', '$').replace('-', '+').replace('$', '-')
        equation = subequation1.subequation + subequation2.subequation
        coeficients = find_all_coeficients(equation)
        final_coeficients = find_final_coeficients(coeficients)
        final_degree = find_degree(final_coeficients)
        sorted_coefinicients = sort_coefinicients(final_coeficients)
        subequation_str = ''
        if final_degree > 2:
            degree = 0
            for coef in sorted_coefinicients:
                if coef.coeficient != 0:
                    subequation_str += ' {:+.4f}'.format(coef.coeficient).rstrip('0').rstrip('.')
                    subequation_str += 'x{}'.format(int(coef.exponent))
                    degree = coef.exponent
            subequation_str += ' = 0'
            print('\nReduced form\t:'+subequation_str)
            print('Degree\t\t: '+str(degree))
            print('\n[INFO]: The polynomial degree is strictly greater than 2, I can\'t solve.')
            return 'ERROR'
        else:
            for coef in sorted_coefinicients:
                if coef.coeficient != 0:
                    subequation_str += '{:+f}*x^{}'.format(coef.coeficient, int(coef.exponent))
            return Equation(Subequation(subequation_str), Subequation('0'))
    except:
        return 'ERROR'
