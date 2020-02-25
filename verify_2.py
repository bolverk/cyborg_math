def verify_1a(answer):
    
    import sympy
    
    S = sympy.Symbol('S', positive=True)
    return answer == 2*S/9

def solve_1b():
    
    import sympy
    
    m = sympy.Symbol('m', positive=True) # Particle mass
    h = sympy.Symbol('h', positive=True) # Planck constant
    E = sympy.Symbol('E', positive=True) # Particle energy
    V_0 = sympy.Symbol('V_0', positive=True) # Potential step
    R = sympy.Symbol('R') # Reflection coefficient
    T = sympy.Symbol('T') # Transmission coefficient
    x = sympy.Symbol('x',real=True) # Position
    left_wave = sympy.exp(sympy.I*x*sympy.sqrt(2*m*E)/h) + R*sympy.exp(-sympy.I*x*sympy.sqrt(2*m*E)/h)
    right_wave = T*sympy.exp(sympy.I*x*sympy.sqrt(2*m*(E-V_0))/h)    
    
    continuity = sympy.Eq(left_wave.subs(x,0), right_wave.subs(x,0))
    differentiability = sympy.Eq(left_wave.diff(x).subs(x,0), right_wave.diff(x).subs(x,0))
    sol = sympy.solve([continuity,differentiability],[R,T])
    return sol

def verify_1bI(answer):
    
    import sympy
    
    sol = solve_1b()
    return sol[sympy.Symbol('R')]==answer

def verify_1bII(answer):
    
    import sympy
    
    sol = solve_1b()
    return sol[sympy.Symbol('T')]==answer

def verify_2a(answer):
    
    import sympy
    
    G = sympy.Symbol('G', positive=True) # Gravitation constant
    M = sympy.Symbol('M', positive=True) # Mass
    t = sympy.Symbol('t', positive=True) # Time
    b = sympy.Symbol('b', positive=True) # Impact parameter
    v = sympy.Symbol('v', positive=True) # Particle velocity
    
    acceleration = G*M*b/(v**2*t**2+b**2)**sympy.Rational(3,2)
    
    solution = sympy.integrate(acceleration,(t,-sympy.oo,sympy.oo))
    
    return solution == answer

def verify_3a(answer):
    
    import sympy
    
    s = sympy.Symbol('s', positive=True) # Separation
    Q = sympy.Symbol('Q', positive=True) # Charge
    r = sympy.Symbol('r', positive=True) # Radius
    q = sympy.Symbol('theta', positive=True) # Angle
    
    potential = 2*Q/r-Q/sympy.sqrt(r**2+s**2+2*s*r*sympy.cos(q))-Q/sympy.sqrt(r**2+s**2-2*s*r*sympy.cos(q))
    
    temp = sympy.series(potential,s,0,3).removeO().simplify()
    
    return (temp/answer).simplify() == 1

def verify_4a(answer):
    
    return answer==1

def verify_5a(answer):
    
    import sympy
    
    x = sympy.Symbol('x', real=True)
    k = sympy.Symbol('k', real=True)
    func = sympy.exp(-x**2)
    
    solution = sympy.fourier_transform(func,x,k)
    return answer == solution

def verify_6a(answer):
    
    import sympy
    
    x = sympy.Function('x', real=True)
    t = sympy.Symbol('t', real=True)
    
    eqn = sympy.Eq(x(t).diff(t,2), -x(t)+sympy.sin(2*t))
    init_cond = {x(0):0,
                x(t).diff(t).subs(t,0):0}
    sol = sympy.dsolve(eqn,x(t),ics=init_cond)
    if not type(sol)==type(answer):
        print('wrong type')
        return False
    return sol == answer
