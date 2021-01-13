class Equation:
    def __init__(self, subequation1, subequation2):
        self.find_coeficients(subequation1, subequation2)
        self.find_degree()

    def find_coeficients(self, subequation1, subequation2):
        self.a0 = float(subequation1.a0 - subequation2.a0)
        self.a1 = float(subequation1.a1 - subequation2.a1)
        self.a2 = float(subequation1.a2 - subequation2.a2)

    def reduced_form(self):
        coef0 = '{:+.2f}'.format(self.a0)
        coef1 = '{:+.2f}'.format(self.a1)
        coef2 = '{:+.2f}'.format(self.a2)
        return 'Reduced form: '+coef0+' * X^0 '+coef1+' * X^1 '+coef2+' * X^2 = 0'

    def find_degree(self):
        self.degree = 0
        self.degree = 1 if self.a1 != 0 else 0
        self.degree = 2 if self.a2 != 0 else self.degree

    def print_degree(self):
        print('Degree: '+str(self.degree))