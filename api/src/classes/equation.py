class Equation:
    def __init__(self, subequation1, subequation2):
        try:
            self.find_coeficients(subequation1, subequation2)
            self.find_reduced_form()
            self.find_degree()
            self.find_discriminant()
            self.error = 0
            self.info = ''
            self.root1_r = 'null'
            self.root1_i = 'null'
            self.root2_r = 'null'
            self.root2_i = 'null'
        except:
            self.error = 1

    def find_coeficients(self, subequation1, subequation2):
        self.a = float(subequation1.a - subequation2.a)
        self.b = float(subequation1.b - subequation2.b)
        self.c = float(subequation1.c - subequation2.c)

    def find_reduced_form(self):
        try:
            reduced_form = ''
            if self.a != 0:
                reduced_form += '{:+.2f}'.format(self.a).rstrip('0').rstrip('.')+'x² '
            if self.b != 0:
                reduced_form += '{:+.2f}'.format(self.b).rstrip('0').rstrip('.')+'x '
            if self.c != 0:
                reduced_form += '{:+.2f}'.format(self.c).rstrip('0').rstrip('.')+' '
            if reduced_form == '':
                reduced_form += '0 '
            reduced_form += '= 0'
            self.reduced_form = reduced_form
        except:
            self.reduced_form = ''
            self.error = 1

    def find_degree(self):
        self.degree = 0
        self.degree = 1 if self.b != 0 else 0
        self.degree = 2 if self.a != 0 else self.degree

    def find_discriminant(self):
        self.discriminant = (self.b * self.b) - (4 * self.c * self.a)