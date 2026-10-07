# Reunión con DDTech

Preparación de la reunión de [[Brayan Gallego]] con [[DDTech]] (algo.com), el 2026-10-08 a las 10:00. Coordina [[David Poveda]] ([[Flowing Consultoría]]).

- Presentación (artefacto privado): https://claude.ai/artifact/EpAwgiwMUKtqAAResv5dnu
- Pedido de Brayan, 2026-10-07: explicar brevemente Manufacturas Eliot, la situación con [[Intuiflow]] (sobre todo el módulo de scheduling y sus dificultades) y cómo se implementó la metodología DBR (tambor, buffer y cuerda) en [[EliotFlow]].

## 2026-10-07 · Fuentes y qué quedó en la presentación

Fuente: correos y OneDrive de Brayan, leídos por Claude en solo lectura el 2026-10-07.

- **Objetivo de la reunión** (pautas de David Poveda, adjunto «Pautas para la reunión.docx», correo del 2026-09-27 6:32): confirmar la lectura de los puntos 3 y 4 de Gerencia para que el fabricante cierre su recomendación y se defina el go/no-go de la generación de rutas, pausada al 90 %.
- **Posición del fabricante** (pautas del 2026-09-27; correo de David Poveda del 2026-09-16): puntos 1 y 2 entendidos, el 2 en discusión interna; 5 y 6 disponibles desde la versión 2026.2.2; los nueve pasos manuales tienen un mejor mecanismo en la 2026.1.x.
- **Lectura de los puntos 3 y 4** (por confirmar en la reunión): el 3, reglas locales por área sobre el pool liberado al tambor, dentro de la política global de WIP; el 4, simulación masiva por grupo de máquina con reglas globales y específicas a la vez.
- **Tema nuevo del fabricante:** algo.com explora una integración basada en MCP para pasar a Intuiflow las decisiones de programación tomadas por fuera.
- **Insumos que Eliot debe llevar** (pautas): la versión de Intuiflow que corre hoy y la descripción breve del aplicativo alterno (qué decide y qué devolvería a Intuiflow).
- **Los nueve pasos manuales** de un cambio de secuencia salen del correo de Brayan Gallego a David Poveda, 2026-09-09 «Scheduling Intuiflow - brechas frente al modelo textil».
- OneDrive, carpeta «01. Proyecto DDMRP»: manuales de scheduling (usuario y administrador), «Boceto Scheduling» y la grabación de «Seguimiento DDMRP Consultoria» del 2026-09-25. No leí las grabaciones.

## Pendientes de la presentación

- **No encontré** en el correo ni en OneDrive un documento que describa cómo está implementado DBR en EliotFlow. La lámina «DBR en EliotFlow» es un mapeo propuesto por Claude a partir del Panel de Asignación y de los puntos 1 a 3; Brayan debe validarlo.
- Falta la versión de Intuiflow que corre hoy.
- Falta lo que EliotFlow devuelve a Intuiflow.
- El «15 %» de capacidad de tintorería apagada sale del cálculo del Panel de Asignación (16.970 de 113.245 kg/día), confirmado por Brayan el 2026-09-29.
