import numpy as np
import matplotlib.pyplot as plt

import matplotlib.colors as colors
from matplotlib.patches import Patch

# ============================
# Parámetros del disco
# ============================
R = 1.0                   # Radio del disco
Q_over_2pi_eps0 = 1.0     # Constante Q/(2πϵ0) para normalización (escala)

# ============================
# Mallado 3D alrededor del disco
# ============================
x = np.linspace(-2.5, 2.5, 15)
y = np.linspace(-2.5, 2.5, 15)
z = np.linspace(-2.5, 2.5, 15)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# Inicializar componentes del campo y magnitud
Ex = np.zeros_like(X, dtype=float)
Ey = np.zeros_like(X, dtype=float)
Ez = np.zeros_like(X, dtype=float)
E_magnitude = np.zeros_like(X, dtype=float)

# ============================
# Cálculo del campo (aprox. n=0 y n=1)
# ============================
for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(z)):
            rx, ry, rz = X[i, j, k], Y[i, j, k], Z[i, j, k]
            r = np.sqrt(rx**2 + ry**2 + rz**2)
            if r <= R or r == 0:
                continue

            # Coordenadas esféricas
            cos_theta = rz / r
            # Evitar problemas numéricos por redondeo
            cos_theta = np.clip(cos_theta, -1.0, 1.0)
            theta = np.arccos(cos_theta)
            sin_theta = np.sqrt(1.0 - cos_theta**2)

            # Aproximación con términos n=0 y n=1
            E_r = (1.0 / r**2) + (3.0 * R**2 / (4.0 * r**4)) * (3.0 * cos_theta**2 - 1.0)
            E_theta = (3.0 * R**2 / (2.0 * r**4)) * cos_theta * sin_theta

            # Ángulo azimutal φ
            if sin_theta > 0:
                cos_phi = rx / (r * sin_theta)
                sin_phi = ry / (r * sin_theta)
            else:
                # Sobre el eje: tomar φ=0 sin pérdida de generalidad
                cos_phi = 1.0
                sin_phi = 0.0

            # Transformación a cartesianas
            Ex[i, j, k] = Q_over_2pi_eps0 * (E_r * sin_theta * cos_phi + E_theta * cos_theta * cos_phi)
            Ey[i, j, k] = Q_over_2pi_eps0 * (E_r * sin_theta * sin_phi + E_theta * cos_theta * sin_phi)
            Ez[i, j, k] = Q_over_2pi_eps0 * (E_r * cos_theta - E_theta * sin_theta)

            # Magnitud
            E_magnitude[i, j, k] = np.sqrt(Ex[i, j, k]**2 + Ey[i, j, k]**2 + Ez[i, j, k]**2)

# ============================
# FIGURA 1: Campo 3D
# ============================
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Reducir densidad para visualización
skip = 2
X_plot = X[::skip, ::skip, ::skip]
Y_plot = Y[::skip, ::skip, ::skip]
Z_plot = Z[::skip, ::skip, ::skip]
Ex_plot = Ex[::skip, ::skip, ::skip]
Ey_plot = Ey[::skip, ::skip, ::skip]
Ez_plot = Ez[::skip, ::skip, ::skip]
E_mag_plot = E_magnitude[::skip, ::skip, ::skip]

# Filtrar sólo r > R
mask3d = np.sqrt(X_plot**2 + Y_plot**2 + Z_plot**2) > R
X_m = X_plot[mask3d]
Y_m = Y_plot[mask3d]
Z_m = Z_plot[mask3d]
Ex_m = Ex_plot[mask3d]
Ey_m = Ey_plot[mask3d]
Ez_m = Ez_plot[mask3d]
E_mag_m = E_mag_plot[mask3d]

# Normalizar vectores para quiver
vec_len = np.sqrt(Ex_m**2 + Ey_m**2 + Ez_m**2)
vec_len = np.maximum(vec_len, 1e-12)
scale_factor = 0.4
Ex_n = Ex_m / vec_len * scale_factor
Ey_n = Ey_m / vec_len * scale_factor
Ez_n = Ez_m / vec_len * scale_factor

# Colores por magnitud
norm3d = colors.Normalize(vmin=E_mag_m.min(), vmax=E_mag_m.max())
cmap3d = plt.cm.viridis(norm3d(E_mag_m))

# Quiver 3D
ax.quiver(X_m, Y_m, Z_m, Ex_n, Ey_n, Ez_n,
          colors=cmap3d, alpha=0.8, arrow_length_ratio=0.3, linewidth=1.2)

# Disco en z=0
theta_disk = np.linspace(0, 2*np.pi, 80)
r_disk = np.linspace(0, R, 40)
Theta, Rg = np.meshgrid(theta_disk, r_disk)
X_d = Rg * np.cos(Theta)
Y_d = Rg * np.sin(Theta)
Z_d = np.zeros_like(X_d)
ax.plot_surface(X_d, Y_d, Z_d, color='red', alpha=0.4)

# Ejes y límites
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_title('Campo eléctrico 3D de un disco cargado (r > R)\nColores indican magnitud del campo')
ax.set_xlim([-2.5, 2.5]); ax.set_ylim([-2.5, 2.5]); ax.set_zlim([-2.5, 2.5])

# Leyenda y barra de color
ax.legend(handles=[Patch(facecolor='red', alpha=0.4, label='Disco cargado')])
sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=norm3d); sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, shrink=0.5, aspect=20)
cbar.set_label('Magnitud del Campo Eléctrico')

plt.tight_layout()
plt.savefig('1.5_fig1.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================
# FIGURA 2: Plano XZ (y = 0)
# ============================
fig_xz, ax_xz = plt.subplots(figsize=(8, 7))

y_idx = np.argmin(np.abs(y))  # índice con y≈0
X_plane = X[:, y_idx, :]
Z_plane = Z[:, y_idx, :]
Ex_plane = Ex[:, y_idx, :]
Ez_plane = Ez[:, y_idx, :]
E_mag_plane = E_magnitude[:, y_idx, :]

mask_xz = np.sqrt(X_plane**2 + Z_plane**2) > R
X_m = X_plane[mask_xz]; Z_m = Z_plane[mask_xz]
Ex_m = Ex_plane[mask_xz]; Ez_m = Ez_plane[mask_xz]
E_mag_m = E_mag_plane[mask_xz]

veclen_xz = np.sqrt(Ex_m**2 + Ez_m**2); veclen_xz = np.maximum(veclen_xz, 1e-12)
Ex_n = Ex_m / veclen_xz * 0.3
Ez_n = Ez_m / veclen_xz * 0.3

norm_xz = colors.Normalize(vmin=E_mag_m.min(), vmax=E_mag_m.max())
cmap_xz = plt.cm.viridis(norm_xz(E_mag_m))

ax_xz.quiver(X_m, Z_m, Ex_n, Ez_n, color=cmap_xz, alpha=0.7,
             scale=1, scale_units='xy', width=0.005, headwidth=3, headlength=4)

# Disco como banda roja en z=0
ax_xz.add_patch(plt.Rectangle((-R, -0.1), 2*R, 0.2, color='red', alpha=0.4, label='Disco'))

ax_xz.set_xlabel('X'); ax_xz.set_ylabel('Z')
ax_xz.set_title('Campo eléctrico en el plano XZ (y=0)')
ax_xz.axhline(0, color='k', linewidth=0.5); ax_xz.axvline(0, color='k', linewidth=0.5)
ax_xz.grid(True); ax_xz.axis('equal'); ax_xz.legend()

sm1 = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=norm_xz); sm1.set_array([])
cbar1 = plt.colorbar(sm1, ax=ax_xz, shrink=0.85); cbar1.set_label('Magnitud del Campo Eléctrico')

plt.tight_layout()
plt.savefig('1.5_fig2_xz.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================
# FIGURA 3: Plano XY (z = 0)
# ============================
fig_xy, ax_xy = plt.subplots(figsize=(8, 7))

z_idx = np.argmin(np.abs(z))  # índice con z≈0
X_plane2 = X[:, :, z_idx]
Y_plane2 = Y[:, :, z_idx]
Ex_plane2 = Ex[:, :, z_idx]
Ey_plane2 = Ey[:, :, z_idx]
E_mag_plane2 = E_magnitude[:, :, z_idx]

mask_xy = np.sqrt(X_plane2**2 + Y_plane2**2) > R
X_m2 = X_plane2[mask_xy]; Y_m2 = Y_plane2[mask_xy]
Ex_m2 = Ex_plane2[mask_xy]; Ey_m2 = Ey_plane2[mask_xy]
E_mag_m2 = E_mag_plane2[mask_xy]

veclen_xy = np.sqrt(Ex_m2**2 + Ey_m2**2); veclen_xy = np.maximum(veclen_xy, 1e-12)
Ex_n2 = Ex_m2 / veclen_xy * 0.3
Ey_n2 = Ey_m2 / veclen_xy * 0.3

norm_xy = colors.Normalize(vmin=E_mag_m2.min(), vmax=E_mag_m2.max())
cmap_xy = plt.cm.viridis(norm_xy(E_mag_m2))

ax_xy.quiver(X_m2, Y_m2, Ex_n2, Ey_n2, color=cmap_xy, alpha=0.7,
             scale=1, scale_units='xy', width=0.005, headwidth=3, headlength=4)

# Disco como círculo rojo en z=0
ax_xy.add_patch(plt.Circle((0, 0), R, color='red', alpha=0.4, label='Disco'))

ax_xy.set_xlabel('X'); ax_xy.set_ylabel('Y')
ax_xy.set_title('Campo eléctrico en el plano XY (z=0)')
ax_xy.axhline(0, color='k', linewidth=0.5); ax_xy.axvline(0, color='k', linewidth=0.5)
ax_xy.grid(True); ax_xy.axis('equal'); ax_xy.legend()

sm2 = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=norm_xy); sm2.set_array([])
cbar2 = plt.colorbar(sm2, ax=ax_xy, shrink=0.85); cbar2.set_label('Magnitud del Campo Eléctrico')

plt.tight_layout()
plt.savefig('1.5_fig2_xy.png', dpi=300, bbox_inches='tight')
plt.show()
