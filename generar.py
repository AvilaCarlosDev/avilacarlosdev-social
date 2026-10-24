#!/usr/bin/env python3
"""Genera los carruseles (1080x1350) de las redes de Avilacarlosdev.

Cada carrusel es una lista de diapositivas; cada diapositiva se arma en HTML
con la paleta de avilacarlosdev.com y se captura con Chromium headless.
Uso: python3 generar.py [nombre-carrusel]
"""
import html
import pathlib
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent
OUT = RAIZ / "out"
WA = "+1 346 491 9344"

CSS = f"""
@font-face {{ font-family: 'Serif'; src: url('{RAIZ}/fonts/instrument-serif-latin-400-normal.woff2'); }}
@font-face {{ font-family: 'Inter'; src: url('{RAIZ}/fonts/inter-latin-wght-normal.woff2'); font-weight: 100 900; }}
@font-face {{ font-family: 'Mono'; src: url('{RAIZ}/fonts/jetbrains-mono-latin-400-normal.woff2'); font-weight: 400; }}
@font-face {{ font-family: 'Mono'; src: url('{RAIZ}/fonts/jetbrains-mono-latin-700-normal.woff2'); font-weight: 700; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ width: 1080px; height: 1350px; overflow: hidden; }}
body {{ font-family: 'Inter', sans-serif; position: relative; padding: 96px 88px 150px; display: flex; flex-direction: column; }}
body.centro {{ justify-content: center; padding-bottom: 190px; }}
.claro {{ background: #f6f5f1; color: #111214; }}
.oscuro {{ background: #0f1628; color: #f6f5f1; }}
.ceja {{ font-family: 'Mono'; font-size: 30px; letter-spacing: .04em; text-transform: uppercase; color: #2b4bff; margin-bottom: 36px; }}
.oscuro .ceja {{ color: #58e1ff; }}
h1 {{ font-family: 'Serif'; font-weight: 400; font-size: 118px; line-height: 1.0; letter-spacing: -.01em; }}
h2 {{ font-family: 'Serif'; font-weight: 400; font-size: 92px; line-height: 1.04; }}
em {{ font-style: italic; color: #2b4bff; }}
.oscuro em {{ color: #58e1ff; }}
p.cuerpo {{ font-size: 42px; line-height: 1.38; color: #3d4048; margin-top: 40px; max-width: 880px; }}
.oscuro p.cuerpo {{ color: #c9cdd8; }}
.num {{ font-family: 'Mono'; font-weight: 700; font-size: 150px; color: #2b4bff; line-height: 1; margin-bottom: 30px; }}
.arreglo {{ margin-top: 64px; background: #fff; border: 2px solid #e3e1da; border-left: 10px solid #2b4bff; border-radius: 18px; padding: 38px 44px; font-size: 38px; line-height: 1.38; }}
.arreglo b {{ font-family: 'Mono'; font-size: 28px; letter-spacing: .05em; text-transform: uppercase; color: #2b4bff; display: block; margin-bottom: 12px; }}
ul.lista {{ list-style: none; margin-top: 52px; display: flex; flex-direction: column; gap: 30px; }}
ul.lista li {{ font-size: 40px; line-height: 1.3; padding-left: 62px; position: relative; }}
ul.lista li::before {{ content: ''; position: absolute; left: 0; top: 14px; width: 26px; height: 26px; border-radius: 6px; background: #2b4bff; }}
.oscuro ul.lista li::before {{ background: #58e1ff; }}
ol.pasos {{ list-style: none; margin-top: 56px; display: flex; flex-direction: column; gap: 34px; counter-reset: p; }}
ol.pasos li {{ counter-increment: p; font-size: 42px; line-height: 1.32; padding-left: 104px; position: relative; min-height: 76px; }}
ol.pasos li::before {{ content: counter(p); position: absolute; left: 0; top: -4px; width: 76px; height: 76px; border-radius: 50%; background: #2b4bff; color: #fff; font-family: 'Mono'; font-weight: 700; font-size: 38px; display: grid; place-items: center; }}
.oscuro ol.pasos li::before {{ background: #58e1ff; color: #0f1628; }}
.mascota {{ position: absolute; right: 70px; bottom: 120px; height: 560px; }}
.navegador {{ margin-top: 56px; border-radius: 22px; overflow: hidden; border: 2px solid #e3e1da; background: #fff; box-shadow: 0 30px 60px -30px rgba(15,22,40,.35); }}
.navegador .barra {{ height: 52px; background: #ecebe6; display: flex; align-items: center; gap: 12px; padding: 0 22px; }}
.navegador .barra i {{ width: 16px; height: 16px; border-radius: 50%; background: #c9c7bf; display: block; }}
.navegador .barra span {{ margin-left: 18px; font-family: 'Mono'; font-size: 22px; color: #565a63; }}
.navegador img {{ display: block; width: 100%; }}
.telefonos {{ margin-top: 40px; display: flex; gap: 26px; justify-content: center; }}
.telefonos img {{ width: 252px; border-radius: 30px; border: 8px solid #111214; }}
.cifras {{ margin-top: 40px; display: flex; gap: 22px; }}
.cifras div {{ flex: 1; background: #fff; border: 2px solid #e3e1da; border-radius: 18px; padding: 26px 24px; font-size: 28px; color: #565a63; }}
.cifras b {{ display: block; font-family: 'Mono'; font-weight: 700; font-size: 56px; color: #2b4bff; }}
.pie {{ position: absolute; left: 88px; right: 88px; bottom: 56px; display: flex; justify-content: space-between; align-items: center; font-family: 'Mono'; font-size: 26px; color: #565a63; }}
.oscuro .pie {{ color: #8b93a7; }}
.pie b {{ color: #111214; font-weight: 700; }}
.oscuro .pie b {{ color: #f6f5f1; }}
.wa {{ margin-top: 56px; display: inline-flex; align-items: center; gap: 22px; background: #25d366; color: #0b2a17; font-weight: 700; font-size: 44px; padding: 30px 46px; border-radius: 999px; align-self: flex-start; }}
.wa.chip {{ background: #58e1ff; color: #0f1628; font-family: 'Mono'; letter-spacing: .04em; }}
.nota {{ font-family: 'Mono'; font-size: 28px; color: #8b93a7; margin-top: 28px; }}
"""


def img(nombre):
    return f"file://{RAIZ}/assets/{nombre}"


def esc(t):
    # Permite *texto* para resaltar en cursiva con el color de acento
    partes = html.escape(t).split("*")
    return "".join(f"<em>{p}</em>" if i % 2 else p for i, p in enumerate(partes))


def portada(ceja, titulo, cuerpo="", mascota=None, oscuro=True):
    m = f'<img class="mascota" src="{img(mascota)}">' if mascota else ""
    c = f'<p class="cuerpo" style="max-width:560px">{esc(cuerpo)}</p>' if cuerpo else ""
    return oscuro, f'<div class="ceja">{esc(ceja)}</div><h1 style="max-width:{620 if mascota else 900}px">{esc(titulo)}</h1>{c}{m}'


def punto(num, titulo, cuerpo, arreglo):
    return False, (f'<!--centro--><div class="num">{num:02d}</div><h2>{esc(titulo)}</h2>'
                   f'<p class="cuerpo">{esc(cuerpo)}</p>'
                   f'<div class="arreglo"><b>Cómo lo resuelvo</b>{esc(arreglo)}</div>')


def lista(ceja, titulo, items, oscuro=False):
    lis = "".join(f"<li>{esc(i)}</li>" for i in items)
    return oscuro, f'<!--centro--><div class="ceja">{esc(ceja)}</div><h2>{esc(titulo)}</h2><ul class="lista">{lis}</ul>'


def pasos(ceja, titulo, items, oscuro=False):
    lis = "".join(f"<li>{esc(i)}</li>" for i in items)
    return oscuro, f'<!--centro--><div class="ceja">{esc(ceja)}</div><h2>{esc(titulo)}</h2><ol class="pasos">{lis}</ol>'


def demo(ceja, titulo, cuerpo, captura, url):
    return False, (f'<div class="ceja">{esc(ceja)}</div><h2>{esc(titulo)}</h2>'
                   f'<p class="cuerpo" style="font-size:38px;margin-top:28px">{esc(cuerpo)}</p>'
                   f'<div class="navegador"><div class="barra"><i></i><i></i><i></i><span>{html.escape(url)}</span></div>'
                   f'<img src="{img(captura)}"></div>')


def telefonos(ceja, titulo, capturas, cifras=(), oscuro=False):
    ims = "".join(f'<img src="{img(c)}">' for c in capturas)
    cf = "".join(f"<div><b>{html.escape(n)}</b>{html.escape(t)}</div>" for n, t in cifras)
    return oscuro, (("<!--centro-->" if not capturas else "") + f'<div class="ceja">{esc(ceja)}</div><h2>{esc(titulo)}</h2>' + (f'<div class="telefonos">{ims}</div>' if ims else "")
                    + (f'<div class="cifras">{cf}</div>' if cf else ""))


def cierre(titulo, cuerpo, mascota="laptop.png", nota="", chip=None):
    n = f'<div class="nota">{esc(nota)}</div>' if nota else ""
    boton = f'<div class="wa chip">{html.escape(chip)}</div>' if chip else f'<div class="wa">WhatsApp {WA}</div>'
    return True, (f'<h2 style="max-width:640px">{esc(titulo)}</h2>'
                  f'<p class="cuerpo" style="max-width:560px">{esc(cuerpo)}</p>'
                  f'{boton}{n}'
                  f'<img class="mascota" src="{img(mascota)}" style="height:520px">')


CARRUSELES = {
    "01-presentacion": [
        portada("Hola, soy Carlos · Punto Fijo, Venezuela",
                "Hago webs para que tus clientes te *escriban por WhatsApp.*",
                "Developer full stack. Trabajo con negocios de aquí y de afuera.", "parado.png"),
        lista("Qué hago", "Dos tipos de trabajo",
              ["Webs para negocios que reciben pedidos, reservas y cotizaciones por WhatsApp",
               "Apps a la medida que se instalan en el teléfono, como Forja, mi app para entrenadores personales",
               "Desarrollo remoto con React, Node.js y Supabase para empresas"]),
        lista("Qué trae cada web", "Pensada para que *te escriban*",
              ["Botón de WhatsApp para pedidos, reservas, citas o cotizaciones",
               "Formulario que guarda cada contacto y te avisa por correo",
               "Medición de tus anuncios de Meta, para saber cuáles te traen clientes",
               "Protección contra spam en el formulario",
               "Diseño a la medida de tu marca, rápido en cualquier teléfono"]),
        pasos("Cómo trabajamos", "Tres pasos", [
            "Me cuentas por WhatsApp tu negocio y qué quieres lograr",
            "Te muestro una propuesta y la ajustamos juntos",
            "La publicamos, conectamos tu WhatsApp y te explico cómo ver los contactos que llegan"]),
        cierre("¿Tienes un negocio?", "Cuéntamelo por WhatsApp y te digo qué haría. El precio te lo doy después de escucharte."),
    ],
    "02-errores": [
        portada("Para dueños de negocio",
                "5 cosas que hacen que tu web *no te traiga clientes.*",
                "Si tu web tiene dos o más, estás perdiendo mensajes.", "pensando.png"),
        punto(1, "El cliente no encuentra cómo escribirte",
              "Tiene que bajar hasta el final o copiar un número a mano. Muchos se cansan antes.",
              "Un botón de WhatsApp visible en cada sección, con el mensaje ya escrito."),
        punto(2, "El formulario llega a un correo que nadie revisa",
              "Alguien te escribió hace tres días y todavía no lo sabes.",
              "Cada contacto queda guardado y te llega un aviso al momento."),
        punto(3, "Tarda en abrir en el teléfono",
              "Casi todos tus clientes te buscan desde el celular. Si la página no carga rápido, se van a la de al lado.",
              "Imágenes livianas y una web hecha primero para el teléfono."),
        punto(4, "Pagas anuncios sin saber cuáles funcionan",
              "Inviertes en Meta y no sabes qué anuncio trajo a cada cliente.",
              "Una página de gracias y la medición de Meta conectada, para ver qué anuncio convierte."),
        punto(5, "El formulario se llena de spam",
              "Entre tanto mensaje basura, el cliente real se pierde.",
              "Protección antispam invisible: el cliente no tiene que resolver acertijos."),
        cierre("¿Cuántas tiene la tuya?", "Guárdalo y revisa tu web con calma. Más casos y proyectos en mi web.", chip="avilacarlosdev.com"),
    ],
    "03-demos": [
        portada("Webs de ejemplo",
                "6 webs, una por rubro. ¿Cuál se parece a *tu negocio?*",
                "Todas reciben pedidos o reservas por WhatsApp.", "carteles.png"),
        demo("Barbería", "Reservas sin llamadas", "Servicios filtrables, barberos, membresías y reservas por WhatsApp.",
             "barberia.jpg", "agencia-web-barberia-demo.vercel.app"),
        demo("Delivery", "Pedidos directos", "Restaurantes, combos, seguimiento del pedido y pedidos por WhatsApp.",
             "delivery.jpg", "agencia-web-delivery-demo.vercel.app"),
        demo("Ferretería", "Cotizaciones rápidas", "Catálogo técnico, paquetes de obra y cotización por WhatsApp.",
             "ferreteria.jpg", "agencia-web-ferreteria-demo.vercel.app"),
        demo("Floristería", "Flores por ocasión", "Colección por ocasión, servicios y pedidos por WhatsApp.",
             "floristeria.jpg", "agencia-web-floristeria-demo.vercel.app"),
        demo("Tienda deportiva", "Catálogo con asesoría", "Catálogo filtrable, ofertas y asesoría por WhatsApp.",
             "deportes.jpg", "agencia-web-deportes-demo.vercel.app"),
        demo("Taxi y transfer", "Cotiza el viaje al momento", "Cotizador, tarifas, conductores y reservas por WhatsApp.",
             "taxi.jpg", "agencia-web-taxi-demo.vercel.app"),
        cierre("¿Tu rubro no está?", "Escríbeme igual. Todas las demos están en avilacarlosdev.com para que las recorras.",
               mascota="celebrando.png"),
    ],
    "04-caso-dr-eddy": [
        portada("Caso · Dr. Eddy Hernández, cirujano bariátrico",
                "Pacientes por WhatsApp *sin publicar su número.*",
                "Así funciona el flujo de su nueva web.", "laptop.png"),
        lista("El problema", "Un número publicado en la web se copia", [
            "Lo toman bots y llega spam",
            "Te escriben sin contexto y hay que preguntar todo desde cero",
            "No sabes qué anuncio trajo a cada paciente"]),
        pasos("La solución", "El paciente llena primero un formulario corto", [
            "Deja su nombre y su consulta en un formulario con protección antispam",
            "El contacto queda guardado y al doctor le llega un aviso por correo",
            "Se abre WhatsApp con su mensaje listo, sin mostrar el número en la página"]),
        lista("Además", "Lo que trae la web", [
            "Página de gracias para medir los anuncios de Meta",
            "Calculadora de IMC para los pacientes",
            "Migración de WordPress a React"]),
        cierre("¿Recibes clientes por WhatsApp?", "Este mismo flujo sirve para consultorios, abogados, talleres y cualquier negocio que agenda citas.",
               mascota="cv-entrega.png", nota="Web en migración · próximo lanzamiento", chip="avilacarlosdev.com"),
    ],
    "06-homelab": [
        portada("Homelab · Venezuela",
                "Qué corre de verdad *en mi casa.*",
                "2 servidores, 12 servicios. Desliza.", "laptop.png"),
        lista("Los servidores", "Dos máquinas, dos trabajos", [
            "*Venator:* Proxmox, Ryzen 5 5600G, 32 GB de RAM y una RX 580 de 8 GB. Aquí vive la IA local",
            "*r2d2:* CasaOS con Docker. Aquí viven las apps del día a día",
            "Pi-hole en los dos: si uno se apaga, el otro sigue filtrando"]),
        lista("Productividad", "Mi Google Drive y mi Notion, en casa", [
            "*Nextcloud:* archivos y sincronización",
            "*OnlyOffice:* documentos y hojas de cálculo",
            "*AppFlowy:* notas, mi alternativa open source a Notion",
            "*Focalboard:* tareas y proyectos",
            "*Docuseal:* firmas electrónicas privadas"]),
        lista("Automatización", "Mi agencia de marketing, autoalojada", [
            "*n8n:* flujos de trabajo y automatizaciones",
            "*ListMonk:* newsletters y listas de correo",
            "*Postiz:* programación de publicaciones"]),
        lista("Red e IA", "Lo que más uso", [
            "*Pi-hole:* bloqueo de anuncios y rastreadores en toda la red",
            "*Tailscale:* entro a mis servidores desde fuera de casa",
            "*IA local:* modelos de texto, visión e imagen en la RX 580, sin mandar datos a la nube",
            "*Floci:* mi laboratorio para practicar AWS",
            "*Servidor de música:* mi biblioteca, sin suscripción"]),
        cierre("¿Tienes homelab?", "Comenta HOMELAB y te paso la lista con el enlace de cada proyecto. Y cuéntame qué corres tú.",
               mascota="celebrando.png", chip="Comenta HOMELAB"),
    ],
    "07-rx580": [
        portada("IA local · benchmarks reales",
                "Un modelo de 30B en una tarjeta *de 8 GB.*",
                "Mi RX 580 del 2017 todavía trabaja. Estos son los números.", "pensando.png"),
        lista("El equipo", "Nada de 4090", [
            "AMD RX 580 de 8 GB",
            "Ryzen 5 5600G y 32 GB de RAM",
            "llama.cpp sobre Vulkan, porque ROCm ya no soporta esta tarjeta",
            "Un router compatible con la API de OpenAI: cualquier app que habla con OpenAI habla con mi servidor"]),
        lista("Velocidad medida", "Tokens por segundo", [
            "*99* · Qwen 2.5 Coder 1.5B",
            "*66* · Qwen 2.5 VL 3B, con visión",
            "*34* · Qwen 2.5 7B",
            "*28* · Ornith 1.5 9B",
            "*21* · Qwen3 30B A3B"]),
        lista("El truco", "18,6 GB de pesos en 8 GB de VRAM", [
            "El modelo de 30B es MoE: solo activa 3B por token",
            "Lo que no cabe en la tarjeta lo sirve la RAM. Por eso los 32 GB",
            "21 tokens por segundo se leen cómodos"]),
        lista("Lo malo", "No todo es bonito", [
            "Cambiar de modelo cuesta entre 8 y 38 segundos",
            "Con textos muy largos, leer el contexto tarda minutos",
            "La uso para resumir, clasificar, traducir y borradores. Lo pesado lo hago en la nube"]),
        cierre("Todo está en GitHub", "polaris-local-ai, con sus pruebas y benchmarks. Comenta RX580 y te paso el enlace.",
               mascota="laptop.png", chip="Comenta RX580"),
    ],
    "08-forja-permisos": [
        portada("Forja · app en producción",
                "109 pruebas para una sola regla: *tus datos son tuyos.*",
                "", "pensando.png"),
        telefonos("Qué es Forja", "La app que hice para entrenadores personales",
                  ["movil-12-rutinas.jpg", "movil-13-evolucion.jpg", "movil-15-finanzas.jpg"]),
        lista("La regla", "Cada persona ve solo lo suyo", [
            "El coach carga peso, medidas, dieta y cobros de sus clientes",
            "Un coach nunca ve los clientes de otro",
            "Si un cliente cambia de entrenador, su historial lo acompaña y el anterior deja de verlo"]),
        lista("Cómo lo garantizo", "Las pruebas intentan romperla", [
            "La regla vive en la base de datos: Supabase con seguridad por fila (RLS)",
            "Cada prueba intenta leer o escribir algo prohibido",
            "Si lo consigue, la prueba falla y me entero antes que un usuario"]),
        telefonos("En números", "Lo que no se ve en la pantalla", [],
                  [("160", "pruebas automáticas"), ("109", "de ellas, de permisos"), ("13", "migraciones de base de datos")]),
        cierre("Pruébala", "Forja está en producción: forja-trainer.vercel.app. Se instala en el teléfono como una app.",
               mascota="celebrando.png", chip="forja-trainer.vercel.app"),
    ],
    "05-forja": [
        telefonos("Forja · mi app en producción", "Rutinas, evolución y cobros del coach",
                  ["movil-12-rutinas.jpg", "movil-13-evolucion.jpg", "movil-15-finanzas.jpg"],
                  [("160", "pruebas automáticas"), ("109", "de ellas, de permisos"), ("13", "migraciones de base de datos")]),
    ],
}


def pie(i, total, oscuro):
    sig = "Desliza →" if i < total - 1 else "avilacarlosdev.com"
    return f'<div class="pie"><span><b>&lt;CA/&gt;</b> avilacarlosdev</span><span>{sig} · {i + 1}/{total}</span></div>'


def generar(nombre):
    slides = CARRUSELES[nombre]
    destino = OUT / nombre
    destino.mkdir(parents=True, exist_ok=True)
    for i, (oscuro, cuerpo) in enumerate(slides):
        p = pie(i, len(slides), oscuro) if len(slides) > 1 else '<div class="pie"><span><b>&lt;CA/&gt;</b> avilacarlosdev</span><span>avilacarlosdev.com</span></div>'
        doc = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
               f'<body class="{"oscuro" if oscuro else "claro"}{" centro" if cuerpo.startswith("<!--centro-->") else ""}">{cuerpo}{p}</body></html>')
        h = destino / f"{i + 1:02d}.html"
        h.write_text(doc, encoding="utf-8")
        png = destino / f"{i + 1:02d}.png"
        subprocess.run(["chromium", "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=1", "--window-size=1080,1350",
                        "--allow-file-access-from-files", "--virtual-time-budget=3000",
                        f"--screenshot={png}", h.as_uri()],
                       check=True, capture_output=True)
        print(png)


if __name__ == "__main__":
    for n in (sys.argv[1:] or CARRUSELES):
        generar(n)
