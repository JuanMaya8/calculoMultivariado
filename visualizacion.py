# Gráficas 2D y 3D

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, sympify
from mpl_toolkits.mplot3d import Axes3D

def graficar_funcion(funcion_str, x1, x2, y1, y2):
    from matplotlib import cm
    x, y = symbols('x y')
    try:
        funcion = sympify(funcion_str)
        f_lambd = lambdify((x, y), funcion, 'numpy')

        # Dominio amplio para visualización general
        x_vals = np.linspace(-2, 2, 100)
        y_vals = np.linspace(-2, 2, 100)
        X, Y = np.meshgrid(x_vals, y_vals)
        Z = f_lambd(X, Y)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Gráfico completo de la función
        ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='white', alpha=0.7)

        # Región de integración resaltada en rojo
        Xr = np.linspace(x1, x2, 30)
        Yr = np.linspace(y1, y2, 30)
        Xr, Yr = np.meshgrid(Xr, Yr)
        Zr = f_lambd(Xr, Yr)
        ax.plot_surface(Xr, Yr, Zr, cmap='autumn', edgecolor='red', alpha=0.9)

        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        ax.set_zlabel('Eje Z')
        ax.set_title(f'Gráfica de f(x,y) = {funcion_str}')

        plt.show()

    except Exception as e:
        raise ValueError(f"Error al graficar la función: {e}")
