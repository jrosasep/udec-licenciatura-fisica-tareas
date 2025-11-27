# cavidad_esferica_plot.py
# Campo y equipotenciales dentro de una cavidad esférica conductora a tierra,
# con una carga puntual q ubicada a una distancia d del centro (método de las imágenes).
# Requiere: numpy, matplotlib
# Uso: python cavidad_esferica_plot.py

import numpy as np
import matplotlib.pyplot as plt

EPS0 = 8.8541878128e-12
k = 1.0/(4.0*np.pi*EPS0)

# --------------------------------
# Parámetros del problema
# --------------------------------
R = 1.0   # Radio de la cavidad
q = 1.0   # Magnitud de la carga real (unidades arbitrarias)
d = 0.4   # Desplazamiento de la carga real (0 < d < R)

# Carga imagen y posición (sobre el eje z)
q_img = -q*R/d
z0    = d          # posición de la carga real (0, z0)
zimg  = R**2/d     # posición de la imagen (0, zimg)

# --------------------------------
# Potencial y campo en el plano x-z (y=0)
# --------------------------------
def V_inside(x, z):
    r1 = np.sqrt((x)**2 + (z - z0)**2)
    r2 = np.sqrt((x)**2 + (z - zimg)**2)
    return k*( q/np.maximum(r1,1e-12) + q_img/np.maximum(r2,1e-12) )

def E_inside(x, z):
    # Campo debido a q
    rx1, rz1 = x, (z - z0)
    r1 = np.sqrt(rx1**2 + rz1**2); r1_cuad = np.maximum(r1**3, 1e-12)
    Ex1 = k*q*rx1/r1_cuad
    Ez1 = k*q*rz1/r1_cuad
    # Campo debido a q' (imagen)
    rx2, rz2 = x, (z - zimg)
    r2 = np.sqrt(rx2**2 + rz2**2); r2_cuad = np.maximum(r2**3, 1e-12)
    Ex2 = k*q_img*rx2/r2_cuad
    Ez2 = k*q_img*rz2/r2_cuad
    # Superposición
    return Ex1 + Ex2, Ez1 + Ez2

def main():
    # Malla cuadrada en el disco r<R
    Nx, Nz = 300, 300
    x = np.linspace(-R, R, Nx)
    z = np.linspace(-R, R, Nz)
    X, Z = np.meshgrid(x, z)
    mask = (X**2 + Z**2) < R**2

    V = np.full_like(X, np.nan, dtype=float)
    Ex = np.zeros_like(X); Ez = np.zeros_like(X)
    V[mask] = V_inside(X[mask], Z[mask])
    Ex[mask], Ez[mask] = E_inside(X[mask], Z[mask])

    # Submuestreo para flechas
    step = 6
    Xs, Zs = X[::step, ::step], Z[::step, ::step]
    Exs, Ezs = Ex[::step, ::step], Ez[::step, ::step]
    masks = mask[::step, ::step]

    # Normalización suave de flechas
    E_mag = np.sqrt(Exs**2 + Ezs**2)
    scale = np.nanpercentile(E_mag[masks], 90.0)
    Exs = np.where(masks, Exs/np.maximum(scale,1e-12), 0.0)
    Ezs = np.where(masks, Ezs/np.maximum(scale,1e-12), 0.0)

    # Figura (un solo gráfico)
    fig, ax = plt.subplots(figsize=(6,6))

    # Equipotenciales dentro de la cavidad
    try:
        levels = np.linspace(np.nanmin(V[mask]), np.nanmax(V[mask]), 20)
    except ValueError:
        levels = 20
    cs = ax.contour(X, Z, V, levels=levels)
    ax.clabel(cs, inline=True, fontsize=8, fmt="%.2e")

    # Flechas del campo eléctrico
    ax.quiver(Xs[masks], Zs[masks], Exs[masks], Ezs[masks], angles='xy', scale=20)

    # Borde de la cavidad
    theta = np.linspace(0, 2*np.pi, 400)
    ax.plot(R*np.cos(theta), R*np.sin(theta), '-', linewidth=1)

    # Marca la posición de la carga real
    ax.plot(0.0, z0, 'o', markersize=6)

    # Estética
    ax.set_aspect('equal', 'box')
    ax.set_xlabel('x')
    ax.set_ylabel('z')
    ax.set_title('Campo y equipotenciales dentro de la cavidad esférica (a tierra)')
    ax.set_xlim(-R, R); ax.set_ylim(-R, R)
    ax.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
