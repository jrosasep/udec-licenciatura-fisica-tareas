# Encargo 01 — Teoría de Circuitos (510361)

Primer encargo del curso, dividido en dos partes: un circuito RLC equivalente y un circuito en DC, más una sección
de señales analizadas y graficadas en Python.

## Contenido del encargo

- **Parte 1 — Circuito RLC:**
  - Reducción paso a paso de una red con muchas resistencias, capacitores e inductancias hasta obtener un RLC
    serie equivalente.
  - Cálculo de $R_{\text{total}}$, $C_{\text{total}}$ y $L_{\text{total}}$.
  - Obtención de la impedancia compleja, la corriente alterna, valores eficaces de tensión y corriente, ángulo
    de desfase y frecuencia de resonancia con su factor de calidad.

- **Parte 2 — Potencia en régimen DC:**
  - Análisis de un circuito alimentado con una fuente de $40\ \text{V}$ en corriente continua.
  - Uso del régimen estacionario: inductores como cortocircuitos y el capacitor como circuito abierto.
  - Cálculo de la resistencia equivalente y de la potencia total disipada por el circuito.

- **Señales en el tiempo:**
  - Gráficas de $y_1(t) = e^{-0{,}1 t}\sin(2t)$ y su envolvente exponencial.
  - Gráfica de $y_2(t) = \sin(\omega_1 t)\sin(\omega_2 t)$ y ejemplo de convolución discreta, todo implementado
    en Python con `numpy`, `matplotlib` y `scipy`.

## Archivos

- `encargo1.tex` — Desarrollo completo en LaTeX.
- `encargo1.pdf` — Versión compilada.
- `UdeC_azul_centrado.png` — Logo usado en la portada.
- `img/` — Figuras exportadas desde las secciones de señales.
