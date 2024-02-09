import sympy as sp

def is_diffeomorphism(surface1, surface2, transformation, domain):
    x, y = sp.symbols('x y')
    u, v = sp.symbols('u v')

   
    surface1_expr = sp.sympify(surface1)
    surface2_expr = sp.sympify(surface2)

    
    h1_expr, h2_expr = map(sp.sympify, transformation)

    
    try:
        
        sp.diff(surface1_expr, x)
        sp.diff(surface1_expr, y)
        sp.diff(surface2_expr, u)
        sp.diff(surface2_expr, v)

      
        sp.diff(h1_expr, x)
        sp.diff(h1_expr, y)
        sp.diff(h2_expr, x)
        sp.diff(h2_expr, y)
    except Exception as e:
        return False, f"Not all functions are differentiable: {e}"

    
    J = sp.Matrix([[sp.diff(h1_expr, x), sp.diff(h1_expr, y)], 
                   [sp.diff(h2_expr, x), sp.diff(h2_expr, y)]])
    J_det = J.det()

    if J_det == 0:
        return False, "Jacobian is zero, the function is not bijective."

    
    for point in domain:
        if J_det.subs({x: point[0], y: point[1]}) == 0:
            return False, f"Jacobian determinant is zero at point {point}."

    return True, "The function is a diffeomorphism."


surface1 = "x - y"
surface2 = "x + y**2"
transformation = transformation = ("sin(x)"), ("sin(y)")
domain = [(0, 0), (1, 1), (-1, -1)]  
result, message = is_diffeomorphism(surface1, surface2, transformation, domain)
print(message)
