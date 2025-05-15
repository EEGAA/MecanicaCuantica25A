import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#FUNCIONES ASOCIADAS DE LEGENDRE
#definir el eje polar theta, es un vector
theta = np.linspace(-np.pi, np.pi, 1000)

#definir las ecuaciones, tomadas de la Diapositiva correspondiente 
# Los grados son P_^
p11 = np.sin(theta)
p10 = np.cos(theta)

p22 = 3 * np.sin(theta)**2
p21 = 3 * np.sin(theta) * np.cos(theta)
p20 = 0.5 * (3 * np.cos(theta)**2 - 1)

p33 = 15 * np.sin(theta) * (1 - np.cos(theta)**2)
p32 = 15 * np.sin(theta)**2 * np.cos(theta)
p31 = 1.5 * np.sin(theta) * (5 * np.cos(theta)**2 - 1)
p30 = 0.5 * (5 * np.cos(theta)**3 - 3 * np.cos(theta))


#aqui se crea la grafica y se personaliza
fig1, axs = plt.subplots(3, 3, subplot_kw={'projection': 'polar'})
fig1.suptitle('Funciones de Legendre - Representación Polar')
#la siguiente matriz contiene las ecuacones y su titulo
polar_data = [
    (p11, 'P₁¹'), (p10, 'P₁⁰'), (p22, 'P₂²'),
    (p21, 'P₂¹'), (p20, 'P₂⁰'), (p33, 'P₃³'),
    (p32, 'P₃²'), (p31, 'P₃¹'), (p30, 'P₃⁰'),
]
for ax, (data, title) in zip(axs.flat, polar_data):
    ax.plot(theta, data)
    ax.set_title(title, fontsize=10)
# graficas polares sin etiquetas para no saturar de datos la figura
fig2, axs2 = plt.subplots(3, 3, subplot_kw={'projection': 'polar'})
fig2.suptitle('Funciones de Legendre - Sin Etiquetas')
for ax, (data, title) in zip(axs2.flat, polar_data):
    ax.plot(theta, data)
    ax.set_title(title, fontsize=10)
    ax.set_xticklabels([])
    ax.set_yticklabels([])



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Esta parte corresponde a la FORMULA DE RODRIGUEZ
# l = 1, 2, 3, ... 10
# Configuración inicial
x = sp.symbols('x') # esta x es una variable simbolica, despues toma los valores para cada punto de X
n = 1
N = 10
PlxG = {}  # Diccionario para almacenar los polinomios evaluados

# Cálculo de los polinomios de Legendre
for i in range(n, N + 2):
    l = i - 1
    Plx = 1/(2**l * sp.factorial(l)) * sp.diff((x**2 - 1)**l, x, l)#aqui es necesaria x, variable simboica
    
    X = np.arange(-1, 1.001, 0.01)
    # Evaluamos el polinomio en cada punto del array X
    PlxG[i] = np.array([float(Plx.subs(x, val)) for val in X])

# Gráfico de todos los polinomios
plt.figure()
for i in range(n, N + 2):
    plt.plot(X, PlxG[i], label=f'l = {i-1}')
plt.title('Todos los polinomios de Legendre')
plt.legend()
plt.grid(True)

# Gráfico dividido en dos subplots, para mejor visualizacion
plt.figure()
# Primer subplot (primeros 5 polinomios)
plt.subplot(211)
plt.title('Primeros 5 valores de "l"')
for i in range(n, int(N/2) + 1):
    plt.plot(X, PlxG[i], label=f'l = {i-1}')
plt.legend()
plt.grid(True)
# Segundo subplot (últimos 5 polinomios)
plt.subplot(212)
plt.title('Valores de "l" del 5 al 10')
for i in range(int(N/2) + 1, N + 1):
    plt.plot(X, PlxG[i], label=f'l = {i-1}')
plt.legend()
plt.grid(True)


#muestra las figuras con las graficas
plt.tight_layout()
plt.show()
