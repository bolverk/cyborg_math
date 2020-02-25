def check_1a(answer):
    
    import sympy
    
    return answer == sympy.Rational(1,3)

def check_2a(answer):
    
    import sympy
    
    return answer == sympy.Symbol('y')

def check_2b(answer):
    
    import sympy
    
    return answer == sympy.Symbol('chi')

def check_2c(answer):
    
    import sympy
    
    return answer == sympy.Symbol('alpha3')

def check_2d(answer):
    
    import sympy
    
    return answer == sympy.Symbol(r'\mathcal{L}')

def check_3a(answer):
    
    import sympy
    a = sympy.Symbol('a')
    b = sympy.Symbol('b')
    c = sympy.Symbol('c')
    d = sympy.Symbol('d')
    z = sympy.Symbol('z')
    return answer == (a*z+b)/(c*z+d)

def check_3b(answer):
    
    import sympy
    n = sympy.Symbol('n')
    return answer == 2**n-1

def check_3c(answer):
    
    import sympy
    temp = sympy.Rational(1)
    for i in range(19):
        temp = 1+1/temp
    return answer == sympy.fraction(temp)[0]

def check_4a(answer):
    
    import sympy
    
    temp = (sympy.sqrt(3)+sympy.sqrt(2))/(sympy.sqrt(3)-sympy.sqrt(2))
    temp = sympy.fraction(temp)
    temp = (temp[0]*temp[0],temp[1]*temp[0])
    temp = (temp[0].simplify(), temp[1].simplify())
    temp = temp[0]/temp[1]
    return answer == temp

def check_5a(answer):
    
    import sympy
    
    temp = 3+4*sympy.I
    temp = temp**2
    temp = sympy.im(temp)
    return answer == temp

def check_6a(answer):
    
    import sympy
    
    x = sympy.Symbol('x')
    rec = (3/x+x)/2
    x_cur = 1
    for i in range(9):
        x_cur = rec.subs(x, x_cur)
    return answer == x_cur

def check_8a(answer):
    
    import sympy
    
    return answer == (1+sympy.sqrt(5))/2