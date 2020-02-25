def verify_1a(answer):
    
    import sympy
    
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    
    return answer == sympy.Matrix([x,y])

def verify_2a(answer):
    
    import sympy
    
    q = sympy.Symbol('theta', positive=True)# Rotation angle
    b = sympy.Matrix([1,0])
    R = sympy.Matrix([[sympy.cos(q), -sympy.sin(q)],[sympy.sin(q), sympy.cos(q)]])
    
    solution = R*b
    return solution == answer

def verify_3a(answer):
    
    import sympy
    
    A = sympy.Matrix([[1,2],[3,4]])
    b = sympy.Matrix([5,6])
    
    sol = A.inv()*b
    
    return sol==answer

def verify_4a(answer):
    
    import sympy
    
    x = sympy.Symbol('x', positive=True)
    matrix = sympy.Matrix([[1,2-x],[3,4]])
    sol = sympy.solve(matrix.det(),x)[0]
    return answer==sol

def verify_5a(answer):
    
    import sympy
    
    M = sympy.Matrix([[-1,1,0],
                      [1,-2,1],
                      [0,1,-1]])
    return answer == M.eigenvects()

def verify_6a(answer):
    
    import sympy
    
    psi = sympy.Symbol('psi', positive=True) # Rapidity
    gen = sympy.Matrix([[0,-1],[-1,0]])
    
    return sympy.exp(psi*gen).simplify() == answer.simplify()

    
    