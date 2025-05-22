# Lógica de cálculo de integrales

from sympy import symbols, integrate, sympify

def calcular_integral(funcion_str, x1, x2, y1, y2):
    x, y = symbols('x y')
    try:
        funcion = sympify(funcion_str)
        integral_y = integrate(funcion, (y, y1, y2))
        integral_xy = integrate(integral_y, (x, x1, x2))
        return float(integral_xy.evalf())
    except Exception as e:
        raise ValueError(f"Error en el cálculo de la integral: {e}")