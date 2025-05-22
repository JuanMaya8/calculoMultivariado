# Interfaz y control general mejorada

import tkinter as tk
from tkinter import messagebox
from integracion import calcular_integral
from visualizacion import graficar_funcion

def ejecutar():
    funcion = entry_funcion.get()
    try:
        x1 = float(entry_x1.get())
        x2 = float(entry_x2.get())
        y1 = float(entry_y1.get())
        y2 = float(entry_y2.get())
        resultado = calcular_integral(funcion, x1, x2, y1, y2)
        label_resultado.config(text=f"Resultado: {resultado}")
        graficar_funcion(funcion, x1, x2, y1, y2)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Interfaz
root = tk.Tk()
root.title("Integración Doble")
root.configure(bg='white')

# Título
titulo = tk.Label(root, text="Calculadora de Integrales Dobles", font=("Arial", 14, "bold"), bg='white', fg='navy')
titulo.grid(row=0, column=0, columnspan=5, pady=10)

# Función
tk.Label(root, text="f(x, y) =", bg='white', font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_funcion = tk.Entry(root, width=35, font=("Arial", 10))
entry_funcion.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

# Límites de integración
frame_limites = tk.Frame(root, bg='white')
frame_limites.grid(row=2, column=0, columnspan=5, pady=10)

# x límites
tk.Label(frame_limites, text="x desde:", bg='white').grid(row=0, column=0, padx=5)
entry_x1 = tk.Entry(frame_limites, width=5)
entry_x1.grid(row=0, column=1)
tk.Label(frame_limites, text="hasta:", bg='white').grid(row=0, column=2, padx=5)
entry_x2 = tk.Entry(frame_limites, width=5)
entry_x2.grid(row=0, column=3)

# y límites
tk.Label(frame_limites, text="y desde:", bg='white').grid(row=1, column=0, padx=5)
entry_y1 = tk.Entry(frame_limites, width=5)
entry_y1.grid(row=1, column=1)
tk.Label(frame_limites, text="hasta:", bg='white').grid(row=1, column=2, padx=5)
entry_y2 = tk.Entry(frame_limites, width=5)
entry_y2.grid(row=1, column=3)

# Botón
btn = tk.Button(root, text="Calcular y Graficar", command=ejecutar, bg='navy', fg='white', font=("Arial", 10, "bold"))
btn.grid(row=3, column=0, columnspan=5, pady=10)

# Resultado
label_resultado = tk.Label(root, text="Resultado:", bg='white', font=("Arial", 10))
label_resultado.grid(row=4, column=0, columnspan=5, pady=5)

root.mainloop()
