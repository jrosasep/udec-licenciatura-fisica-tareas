# Certamen 1 — Mecánica Clásica I

Certamen 1 del curso **Mecánica Clásica I** (UdeC, 2025-1).  
Incluye tres problemas: uno sobre un sistema de coordenadas no cartesiano en ℝ³, otro de mecánica orbital en un campo gravitacional central, y un tercero sobre el movimiento de una partícula en un potencial central con análisis energético y cinemático.

---

## Problema 1 — Coordenadas oblatas esferoidales y operadores diferenciales

En este problema se estudia la transformación
\[
(x,y,z) \mapsto (v,\varphi,\theta)
\]
correspondiente a **coordenadas oblatas esferoidales**, analizando la geometría de las líneas coordenadas y la estructura métrica asociada. :contentReference[oaicite:1]{index=1}  

### Enfoque

- Se describen las **líneas coordenadas** para $v$, $\varphi$ y $\theta$ y su interpretación geométrica:
  hiperboloides de una hoja, elipsoides de revolución y planos que rotan alrededor del eje $z$.
- Se construyen los **vectores base** $\vec e_v$, $\vec e_\varphi$, $\vec e_\theta$ como derivadas parciales de
  $\vec x(v,\varphi,\theta)$ y se identifican los puntos donde se anulan.
- A partir de los productos escalares $\vec e_i\cdot\vec e_j$ se obtiene la **métrica diagonal** del sistema y su inversa.
- Usando la métrica se deducen las expresiones generales del **gradiente**, la **divergencia** y el **Laplaciano** en coordenadas oblatas esferoidales.
  

---

## Problema 2 — Maniobra orbital alrededor de Marte

Se analiza una nave de masa $m$ que llega a Marte (masa $M$) en una órbita parabólica y, al frenar en el periastro $B$, pasa a una órbita elíptica cuidadosamente elegida para **amartizar tangencialmente** en un punto opuesto $C$. :contentReference[oaicite:2]{index=2}  

### Enfoque

- Uso de las leyes de **conservación de energía mecánica** y **momento angular** en campos centrales.
- Cálculo de la **velocidad en B** para la órbita parabólica (energía total nula).
- Construcción de la órbita elíptica posterior (periastro en $r_B$ y apoastro en $R_M$), determinando el **semieje mayor** y la energía total $E<0$.
- Obtención de la **rapidez en C** mediante conservación de la energía, expresada en términos de $G$, $M$, $r_B$ y $R_M$.
- Resumen final con las expresiones que permiten diseñar la maniobra de frenado y descenso.

---

## Problema 3 — Movimiento en un campo central y análisis energético

En este problema se estudia el movimiento de una partícula en un **campo central** con simetría axial, analizando la forma de la fuerza radial, la energía total y la evolución del movimiento en función del ángulo. :contentReference[oaicite:3]{index=3}  

### Enfoque

- Revisión de los **preliminares teóricos** de campos centrales: energía, momento angular y ecuación efectiva radial.
- Determinación de la **dependencia de la fuerza con la distancia** a partir del potencial dado.
- Cálculo de la **energía total** y discusión de las órbitas resultantes (vínculo entre energía, signo de la fuerza y tipo de trayectoria).
- Obtención del **período del movimiento** y estudio de cómo depende de los parámetros del potencial.
- Análisis de la **rapidez en función del ángulo** y del comportamiento de la partícula al acercarse al centro de fuerza.

---

- ### Archivos

- `certamen1.tex` — Desarrollo completo en LaTeX.
- `certamen1.pdf` — Versión compilada del certamen.
- `UdeC_azul_centrado.png` — Logo utilizado en la portada.
- `3.1_fig1.png`, `3.1_fig2.png`, `oblatas_general.png`, `tangentes_punto.png`, `curva_v.png`, `curva_phi.png`, `curva_theta.png`, `fig_1.png`  — Figuras utilizadas en el desarrollo de los problemas 2 y 3.
- `P1/` — Figuras del Problema 1:
