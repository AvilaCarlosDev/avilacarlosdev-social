# Semana del 6 al 13 de noviembre de 2026 (hora de Caracas)

Estado: borrador para revisar. Nada programado todavía.

| Cuándo | Red | Pieza |
|---|---|---|
| Vie 6 · 19:00 | instagram + facebook | reel ya editado · sale del borrador |
| Lun 9 · 12:30 | linkedin | documento PDF |
| Lun 9 · 19:00 | instagram + facebook | carrusel |
| Mar 10 · 12:30 | linkedin | solo texto |
| Mié 11 · 12:30 | linkedin | documento PDF · falta confirmar UPS |
| Mié 11 · 19:00 | instagram + facebook | falta confirmar UPS |
| Jue 12 · 19:00 | instagram + facebook | reel ya editado · texto ajustado |
| Vie 13 · 19:00 | instagram + facebook + linkedin | reel ya editado · se mueve del lun 9 |

## Vie 6 · 19:00 · instagram + facebook

Mis automatizaciones no corren en la nube. n8n para los flujos, ListMonk para los correos y Postiz para programar publicaciones, todo autoalojado con Docker en un servidor en mi casa.

¿Qué automatizarías tú si no tuvieras que pagar suscripción? Te leo en los comentarios.

Video con mi avatar y mi voz clonada con IA.

#n8n #selfhosting #homelab #automatizacion #docker #opensource

## Lun 9 · 12:30 · linkedin

El viernes actualicé las apps de mi homelab y se reiniciaron 40 contenedores sin que yo lo pidiera.

Iba servicio por servicio a propósito: respaldo primero, imagen descargada antes de parar nada, comprobación después de cada cambio y vuelta a la versión anterior si algo fallaba. El reinicio vino del paso que parecía inofensivo. Al actualizar el sistema del contenedor, apt también actualizó Docker, y el servicio se reinició con todo adentro. Los 40 volvieron solos, pero entre ellos había tres Nextcloud que yo hubiera preferido no tocar.

El trabajo lo ejecutó un agente de IA y las decisiones las tomé yo. Al revisar el respaldo apareció otro fallo: la base de Vaultwarden se había copiado con el servicio encendido, así que se repitió con el servicio parado.

Mi nota para la próxima es mirar si Docker está en la lista de paquetes antes de actualizar. ¿Tú separas esa actualización del resto del sistema?

#homelab #docker #devops #selfhosting

## Lun 9 · 19:00 · instagram + facebook

Iba con cuidado, servicio por servicio, y aun así se reiniciaron 40 contenedores. Actualizar el sistema también actualizó Docker. Todos volvieron solos, pero el susto me dejó tres cambios para la próxima.

En el carrusel está el método completo y los dos fallos. Lo ejecutó un agente de IA y las decisiones fueron mías.

¿Vas servicio por servicio o lo lanzas todo de una?

#homelab #docker #selfhosting #linux #devops

## Mar 10 · 12:30 · linkedin

Mi tablero marcaba en rojo un DNS que funcionaba perfectamente.

Era el DNS público de respaldo de mi red. La prueba abría una conexión TCP al puerto 53 y en 24 horas falló 69 veces, siempre un muestreo suelto. Bastaba un fallo para pintar la tarjeta de rojo, así que el tablero avisaba de una caída que nadie podía notar.

Hice dos cambios. La prueba ahora hace una consulta DNS real por UDP, igual que un cliente. Y la tarjeta solo se pone roja si falla el minuto completo, con max_over_time sobre probe_success en Prometheus.

Un monitor que avisa sin motivo termina ignorado, y ahí es cuando una caída real pasa de largo. Por eso reviso las alertas falsas con la misma seriedad que las verdaderas.

#prometheus #grafana #homelab #observabilidad

## Mié 11 · 12:30 · linkedin

Un Galaxy Note 9 vigila mis servidores.

Cada minuto comprueba 28 servicios y me avisa por Telegram a la segunda falla. Cuando se va la luz, su batería lo mantiene despierto: si pasa 120 segundos sin cargar, apaga los servidores uno detrás del otro por SSH. Los cortes cortos no cuentan.

Lo que más cuidé fue la clave. Solo puede ejecutar un script, y ese script solo acepta dos órdenes: prueba y apagar. No sirve para abrir una consola en el servidor.

La orden de prueba responde en los dos servidores. Todavía me falta verlo funcionar en un corte real, así que acepto ideas de lo que le agregarías.

#homelab #linux #ssh #selfhosting

## Mié 11 · 19:00 · instagram + facebook

Le di trabajo a un Note 9: vigila 28 servicios cada minuto y, si se va la luz, apaga mis servidores en orden.

La clave que usa solo sabe hacer eso. Todavía me falta probarlo en un corte real. ¿Qué le agregarías?

#homelab #selfhosting #android #termux #linux

## Jue 12 · 19:00 · instagram + facebook

No necesitas una 4090 para tener IA en casa. Lo medí en una RX 580 de 8 GB del 2017: 99 tokens por segundo en el modelo más rápido y 21 en uno de 30B.

Comenta RX580 y te paso el repositorio con todos los benchmarks.

Video con mi avatar y mi voz clonada con IA.

#ialocal #inteligenciaartificial #homelab #amd #llamacpp #opensource

## Vie 13 · 19:00 · instagram + facebook + linkedin

Un solo error de permisos puede mostrarle a un cliente los datos de todos los demás. Por eso Forja, mi app para entrenadores personales, tiene 109 pruebas solo de permisos, sobre Supabase con seguridad por fila.

Cuando construyo algo para un cliente, empiezo por aquí.

Video con mi avatar y mi voz clonada con IA.

#supabase #ciberseguridad #react #testing #desarrolloweb
