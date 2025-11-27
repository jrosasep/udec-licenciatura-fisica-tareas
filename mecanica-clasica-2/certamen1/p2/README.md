# Problema 2 — Cadena de péndulos y límite continuo

Aquí se estudia una cadena de péndulos de masa $m$ acoplados por resortes de constante $k$, separados una
distancia $h$ y de longitud $r$.

## Enfoque

- Se escriben las ecuaciones de movimiento discretas para el desplazamiento horizontal $q_i(t)$ en el régimen
  de oscilaciones pequeñas, incluyendo el término restaurador debido a la gravedad.
- Se construye el **Lagrangiano discreto** y luego se toma el límite al continuo, identificando:
  - la densidad lineal de masa $\lambda = m/h$,
  - la tensión efectiva $T = \lim_{h\to 0} kh$.
- En el continuo se obtiene un campo $q(t,x)$ que obedece una ecuación tipo **Klein–Gordon 1+1D**, con velocidad
  de propagación $v_p = \sqrt{T/\lambda}$ y frecuencia propia $\omega_0 = \sqrt{g/r}$.
- Se deriva la densidad lagrangiana $\mathcal{L}(q, q_t, q_x)$ y las ecuaciones de campo mediante el principio de
  mínima acción.

## Archivos

- `fig_p2.png` — Esquema de la cadena de péndulos acoplados que se usa en el desarrollo.
