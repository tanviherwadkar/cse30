class Function():
    def __init__(self, coefs):
        num0 = 6 - len(coefs)
        for i in range(num0):
            coefs.append(0)
        self.coefs = coefs

    def __str__(self):
        return f"polynomial: {self.coefs[0]} + {self.coefs[1]}x + {self.coefs[2]}x^2 + {self.coefs[3]}x^3 + {self.coefs[4]}x^4 + {self.coefs[5]}x^5\npolynomial: {self.coefs[0]} + {self.coefs[1]}x + {self.coefs[2]}x^2 + {self.coefs[3]}x^3 + {self.coefs[4]}x^4 + {self.coefs[5]}x^5\npolynomial: {self.coefs[0]} + {self.coefs[1]}x + {self.coefs[2]}x^2 + {self.coefs[3]}x^3 + {self.coefs[4]}x^4 + {self.coefs[5]}x^5\npolynomial: {self.coefs[0]} + {self.coefs[1]}x + {self.coefs[2]}x^2 + {self.coefs[3]}x^3 + {self.coefs[4]}x^4 + {self.coefs[5]}x^5\npolynomial: {self.coefs[0]} + {self.coefs[1]}x + {self.coefs[2]}x^2 + {self.coefs[3]}x^3 + {self.coefs[4]}x^4 + {self.coefs[5]}x^5\nderivative: {self.coefs[1]} + {2*self.coefs[2]}x + {3*self.coefs[3]}x^2 + {4*self.coefs[4]}x^3 + {5*self.coefs[5]}x^4"

    def f(self, x):
        return self.coefs[0] + self.coefs[1]*x + self.coefs[2]*(x**2) + self.coefs[3]*(x**3) + self.coefs[4]*(x**4) + self.coefs[5]*(x**5)
    
    def fprime(self):
        return Function([self.coefs[1], 2*self.coefs[2], 3*self.coefs[3], 4*self.coefs[4], 5*self.coefs[5]])

"""def f(x, a = 0, b = 0, c = 1, d = 0, e = 0, f = 0):
    return a + b*(x) + c*(x**2) + d*(x**3) + e*(x**4) + f*(x**5)"""

def bisec_basic(poly, a, b, m = 0.0001):
    if not (poly.f(a) < 0 and poly.f(b) > 0):
        if poly.f(a) > 0 and poly.f(b) < 0:
            a, b = b, a
        else:
            return None
    #midpoint
    c = (a+b)/2
    #convergance
    if abs(c-a) <= m:
        return round(c, 3)
    #else, recurse
    else:
        if poly.f(c) > 0:
            return bisec_basic(poly, a, c)
        elif poly.f(c) < 0:
            return bisec_basic(poly, c, b)

    
def bisec(poly, a, b, r = 10**-2):
    a_orig = a
    x = a + r
    root_found = False
    while x <= b:
        #print("a = ", a, " || ", "x = ", x, " || ", "b = ", b)
        root = bisec_basic(poly, a, x)
        if root != None:
            root_found = True
            print("Root found at:", root)
        a = x
        x += r
    
    a = a_orig
    x = a + r
    roots = []
    while x <= b:
        #print("a = ", a, " || ", "x = ", x, " || ", "b = ", b)
        #print(poly.fprime())
        root = bisec_basic(poly.fprime(), a, x)
        if root != None:
            root_found = True
            roots.append(root)
        a = x
        x += r
    for root in roots:
        if poly.f(root) == 0:
            print("Root found at: ", root)

    if root_found == False:
        print("No Roots Found!")

#run code
func_args = input("Enter the polynomial coefficients:\n")
func_args = func_args.split()
func_args = [int(x) for x in func_args]

interval = input("Enter the interval:\n")
interval = interval.split()
interval = [int(x) for x in interval]

poly = Function(func_args)
bisec(poly, interval[0], interval[1])
