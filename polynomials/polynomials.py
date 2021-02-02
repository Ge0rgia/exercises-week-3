from numbers import Number



def derivative(n):
    from polynomials import Polynomial
    return n.dx()


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            other2 = [-a for a in other.coefficients]
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other2))
            coefs += self.coefficients[common:] + tuple(a for a in other2[common:])

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __rsub__(self, other):
        new = self - other
        new2 = tuple(-a for a in new.coefficients)
        return Polynomial(new2)

    def __mul__(self,other):
        if isinstance(other, Polynomial):
            coefs = [0 for i in range(0, (self.degree()+other.degree()+1))]
            for i in range(0, self.degree()+1):
                for j in range(0, other.degree()+1):
                    term = i + j
                    coefs[term] += self.coefficients[i]*other.coefficients[j]
                    coefs2 = tuple(coefs)
            return Polynomial(coefs2)

        elif isinstance(other, Number):
            coefs = [a*other for a in self.coefficients]
            coefs2 = tuple(coefs)
            return Polynomial(coefs2)

        else:
            return NotImplemented

    def __rmul__(self,other):
        return self*other

    def __pow__(self,other):
        if isinstance(other, Number) and other>0:
            p = self
            for k in range(1,other):
                p = p*self
            return p

        else:
            return NotImplemented

    def __call__(self,other):
        if isinstance(other, Number):
            val = self.coefficients[0]
            for i in range (1, (self.degree()+1)):
                val += (other**i)*self.coefficients[i]
            return val
        else:
            return NotImplemented

    def dx(self):
        if isinstance(self, Polynomial):
            if self.degree() == 0:
                return Polynomial((0,))
            else:
                d = [0 for a in range(0, self.degree())]
                for i in range(0, (self.degree())):
                    d[i] = self.coefficients[i+1]*(i+1)  
            return Polynomial(tuple(d))

        elif isinstance(self, Number):
            return 0

        else:
            return NotImplemented
    

