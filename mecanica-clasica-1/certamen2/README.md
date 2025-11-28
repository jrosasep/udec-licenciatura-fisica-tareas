# Certamen 2 — Mecánica Clásica I

Certamen 2 del curso **Mecánica Clásica I** (UdeC).  
Incluye una serie de problemas sobre formulación lagrangiana y hamiltoniana, constantes del movimiento y transformaciones canónicas, con énfasis en técnicas formales y su interpretación física. :contentReference[oaicite:4]{index=4}  

---

## Problema 1 — Péndulo con longitud efectiva variable y soporte oscilante

Se estudia un péndulo cuyo hilo pasa por un orificio en un tablero que se mueve verticalmente según $s(t)=A\sin(\omega t)$. La longitud efectiva del péndulo es $r(t)=L_0-s(t)$, de modo que el movimiento del soporte acopla la dinámica radial y angular. :contentReference[oaicite:5]{index=5}  

### Enfoque

- Elección de **coordenadas generalizadas**: ángulo $\theta$ y longitud efectiva $r(t)$ impuesta por el vínculo.
- Cálculo de las **velocidades generalizadas** y de la energía cinética en términos de $\theta$, $\dot\theta$ y las funciones prescritas $s(t)$, $\dot s(t)$.
- Construcción del **Lagrangiano** $L=T-U$ e interpretación del término cruzado que acopla el movimiento del soporte con el péndulo.
- Obtención de la **ecuación de Lagrange**, donde aparecen:
  - un término proporcional a $-2\dot s(t)\dot\theta$ tipo fuerza de Coriolis efectiva,
  - un término $(g+\ddot s(t))\sin\theta$ asociado a un campo gravitacional efectivo.
- Cálculo del **Hamiltoniano** del sistema en términos de la coordenada $\theta$ y su momento conjugado $p_\theta$.

### Archivos

- `certamen2.tex` — Desarrollo completo en LaTeX.
- `certamen2.pdf` — Versión compilada del certamen.
- `pendulo_orificio.png` — Esquema del sistema masa–hilo–tablero.
- `fig1.png`–`fig11.png` — Figuras auxiliares usadas en las distintas secciones del informe.
- `UdeC_azul_centrado.png` — Logo utilizado en la portada.

---

## Problema 2 — Constante del movimiento en un potencial anisotrópico

Se demuestra un resultado general sobre constantes del movimiento en sistemas hamiltonianos y se aplica a una partícula en dos dimensiones bajo el potencial
\[
V(\vec r) = \frac{\vec a\cdot\vec r}{r^3},
\]
donde $\vec a$ es un vector constante. :contentReference[oaicite:6]{index=6}  

### Enfoque

- Prueba general: si el Hamiltoniano puede escribirse como
  \[
  H(q_i,p_i)=H(f(q_1,p_1),q_2,\dots,q_f,p_2,\dots,p_f),
  \]
  entonces $f(q_1,p_1)$ es una **constante del movimiento**, usando corchetes de Poisson.
- Reformulación del problema de la partícula en **coordenadas polares** y análisis del carácter no isotrópico del potencial.
- Elección de un sistema de referencia rotado donde $\vec a=(a,0)$ para simplificar el potencial.
- Escritura del Hamiltoniano como
  \[
  H(r,p_r,\varphi,p_\varphi)
  = \frac{p_r^2}{2m} + \frac{1}{r^2} f(\varphi,p_\varphi),
  \]
  identificando explícitamente la función
  \[
  f(\varphi,p_\varphi)=\frac{p_\varphi^2}{2m}+a\cos\varphi,
  \]
  y mostrando que $f$ es la **constante de movimiento** asociada.

---

## Problema 3 — Transformación canónica hacia un oscilador armónico (Goldstein 9-25)

Se considera el Hamiltoniano
\[
H(q,p) = \frac{1}{2}\left(p^2 q^4 + \frac{1}{q^2}\right),
\]
y se pide: (i) obtener la ecuación de movimiento para $q(t)$ y (ii) encontrar una **transformación canónica** que reduzca el Hamiltoniano a la forma de un oscilador armónico estándar. :contentReference[oaicite:7]{index=7}  

### Enfoque

- Derivación de las **ecuaciones de Hamilton** y eliminación de $p$ para obtener una ecuación de segundo orden no lineal para $q(t)$.
- Construcción de nuevas variables canónicas $(Q,P)$ mediante una transformación que reescala $q$ y $p$ para absorber los factores de $q$ en la energía.
- Demostración de que el Hamiltoniano en las nuevas variables toma la forma
  \[
  K(Q,P) = \frac{1}{2}\left(P^2 + \Omega^2 Q^2\right),
  \]
  con $\Omega$ constante, por lo que el sistema es **equivalente a un oscilador armónico**.
- Verificación explícita de que la solución en $(Q,P)$, al volver a $(q,p)$, satisface la ecuación de movimiento obtenida inicialmente.

---

## Problema 4 — Ejercicio complementario

El certamen incluye además un **cuarto problema** breve que sirve como complemento teórico a los anteriores, reforzando las técnicas de formulación lagrangiana/hamiltoniana presentadas en el curso. :contentReference[oaicite:8]{index=8}  

---

## Estructura de la carpeta

- `certamen2.tex`, `certamen2.pdf`
- `pendulo_orificio.png`
- `fig1.png`–`fig11.png`
- `UdeC_azul_centrado.png`
