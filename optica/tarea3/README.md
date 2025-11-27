# Tarea 03 — Óptica ondulatoria

Tarea enfocada en la descripción ondulatoria de la luz: ecuación de onda, pulsos viajantes e interferencia por
lámina delgada. Incluye ejemplos resueltos y un script en Python para las gráficas.

## Contenido

- **Problema 1 — Ecuación de onda 1D:**
  - Partiendo de $u(z,t) = f(z', t)$ con $z' = z \mp vt$, se demuestra que
    $$\\frac{\\partial^2 u}{\\partial z^2} = \\frac{1}{v^2} \\frac{\\partial^2 u}{\\partial t^2}.$$
  - Se verifica la ecuación de onda para un pulso específico
    $$u(z,t) = \\frac{3}{10(z - vt)^2 + 1},$$
    y se analiza su interpretación física como pulso no dispersivo.
  - Se grafica el pulso para $t = 0, 1, 2, 3\\ \\text{s}$ en el intervalo $z \\in [-5, 7]$, mostrando cómo se
    traslada sin cambiar de forma.

- **Problema 2 — Interferencia en lámina delgada:**
  - Lámina de espesor $t$ e índice $n'$ iluminada desde un medio de índice $n$ con ángulo $\\theta$.
  - Derivación de la diferencia de camino óptico $\\Delta \\ell$ entre el rayo reflejado en la cara superior y el
    que se refleja en la cara inferior.
  - Expresión final de $\\Delta \\ell$ como función de $n'$, $t$ y $\\theta'$ y discusión de las condiciones de
    interferencia constructiva y destructiva.

## Archivos

- `tarea3.tex` — Desarrollo completo en LaTeX.
- `tarea3.pdf` — Versión compilada.
- `UdeC_azul_centrado.png` — Logo UdeC.
- `img/` — Figuras usadas en los problemas (perfiles de onda e interferencia).
