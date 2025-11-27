import numpy as np
import matplotlib.pyplot as plt

# Parámetros físicos (valores normalizados)
mu0 = 1.0  # Permeabilidad del vacío
R = 1.0    # Radio de la esfera
sigma = 1.0 # Densidad de carga superficial
omega = 1.0 # Velocidad angular

# Constante de normalización
C = mu0 * R**4 * sigma * omega / 3

def campo_magnetico_cartesianas(y, z):
    """
    Calcula el campo magnético en coordenadas cartesianas usando la expresión dipolar
    """
    r = np.sqrt(y**2 + z**2)
    
    # Solo calculamos para r > R
    mask = r > R
    
    # Inicializar componentes
    By = np.zeros_like(y)
    Bz = np.zeros_like(z)
    
    # Componentes del campo dipolar en el plano zy (x=0)
    # Para un dipolo m = (4π/3)R^4 σ ω en dirección z
    r5 = r[mask]**5
    By[mask] = (3 * C * y[mask] * z[mask]) / r5
    Bz[mask] = (C * (2 * z[mask]**2 - y[mask]**2)) / r5
    
    return By, Bz

# Crear malla más densa para mejor visualización de líneas de campo
y_dense = np.linspace(-3*R, 3*R, 60)
z_dense = np.linspace(-3*R, 3*R, 60)
Y_dense, Z_dense = np.meshgrid(y_dense, z_dense)

# Calcular campo magnético en malla densa
By_dense, Bz_dense = campo_magnetico_cartesianas(Y_dense, Z_dense)

# Crear la figura
plt.figure(figsize=(12, 10))

# Streamplot para líneas de campo
plt.streamplot(Y_dense, Z_dense, By_dense, Bz_dense, color='blue', 
               density=2, linewidth=1.2, arrowsize=1.2)

# Dibujar la esfera
circle = plt.Circle((0, 0), R, color='red', alpha=0.4, label='Esfera')
plt.gca().add_patch(circle)

# Configuración del gráfico
plt.xlabel('y [m]', fontsize=12)
plt.ylabel('z [m]', fontsize=12)
plt.title('Líneas de Campo Magnético Dipolar - Plano zy\nEsfera Cargada Rotante', fontsize=14)
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.xlim(-3*R, 3*R)
plt.ylim(-3*R, 3*R)

# Líneas de referencia
plt.axhline(y=0, color='k', linestyle='--', alpha=0.5)
plt.axvline(x=0, color='k', linestyle='--', alpha=0.5)

# Flecha para indicar dirección de rotación
plt.arrow(0, 1.5*R, 0, 0.3*R, head_width=0.1, head_length=0.1, 
          fc='red', ec='red', label='Eje de rotación (ω)')
plt.text(0.1, 1.8*R, 'ω', fontsize=14, color='red')

# Añadir anotaciones para identificar los polos
plt.text(0, 1.1*R, 'Polo Norte', fontsize=10, ha='center', color='darkred')
plt.text(0, -1.1*R, 'Polo Sur', fontsize=10, ha='center', color='darkred')

plt.legend()
plt.tight_layout()
plt.show()