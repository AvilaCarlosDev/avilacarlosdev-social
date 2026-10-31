# Guiones para grabar (lunes)

**Cómo grabar**
- Celular en vertical, apoyado o en trípode, a la altura de los ojos.
- Luz de frente (ventana o aro), fondo simple. Sin música ni ruido.
- Una toma por guion, 30 a 45 s. Si te equivocas, repite la frase y sigue: yo corto las tomas fallidas y los silencios.
- Habla como hablas siempre. No hace falta memorizar palabra por palabra.
- No digas dónde vives ni muestres pantallas con IPs, correos o contraseñas.

## 1 · IA local en una RX 580

No necesitas una 4090 para tener IA en casa. Yo uso una RX 580 de 8 gigas, una tarjeta del 2017. Con ella corro modelos de texto, visión e imagen, todo local, sin pagar API y sin que mis datos salgan de mi red. El truco fue montar un servidor compatible con la API de OpenAI que corre sobre Vulkan. El modelo más rápido da 99 tokens por segundo, y hasta uno de 30 mil millones de parámetros corre a 21. Para resumir, clasificar y escribir borradores, me sobra. Comenta RX580 y te paso el repositorio con los benchmarks.

## 2 · Automatizaciones en casa

Mis automatizaciones no corren en la nube. Corren en un servidor en mi casa. Uso n8n para los flujos, ListMonk para los correos y Postiz para programar publicaciones, todo autoalojado con Docker. Para entrar desde fuera uso Tailscale, una red privada entre mis equipos. ¿Por qué no pagar un servicio? Porque quiero entender cada pieza y poder arreglarla yo, y porque cada dólar en suscripciones pesa. Sígueme y te muestro cómo armé cada flujo.

## 3 · Permisos de Forja

Un solo error de permisos puede mostrarle a un cliente los datos de todos los demás. Por eso Forja, mi app para entrenadores personales, tiene 109 pruebas solo de permisos. Cada prueba intenta algo que no debería poder hacer, como un entrenador leyendo los clientes de otro. Si lo consigue, la prueba falla y me entero antes que cualquier usuario. La regla vive en la base de datos, con Supabase y seguridad por fila. Cuando construyo algo para un cliente, empiezo por aquí.
