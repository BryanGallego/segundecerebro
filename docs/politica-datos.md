# Política de datos del segundo cerebro · v1 (borrador)

Borrador para revisar con quien maneje la protección de datos en la empresa **antes del día 1**. No es asesoría legal. El marco en Colombia es la Ley 1581 de 2012, de protección de datos personales.

**Aprobado por:** [nombre, cargo] · **Fecha:** [AAAA-MM-DD]

## Para qué

Un asistente de inteligencia artificial le prepara al gerente de manufactura un resumen diario, las actas de reunión y respuestas a sus preguntas sobre la planta. Es un piloto de un solo usuario.

## Qué lee

- El correo recibido y enviado del gerente.
- Su calendario.
- Las transcripciones de Teams de las reuniones que tienen la transcripción activa.
- Archivos de OneDrive y SharePoint a los que el gerente ya tiene acceso, solo cuando responde una consulta.
- La carpeta `Cerebro` del OneDrive del gerente.

Lee con los permisos del gerente: no ve nada que el gerente no pueda ver.

## Qué no lee

Exclusiones que el gerente define antes del día 1:

- **Remitentes:** [por ejemplo, gestión humana, jurídica, servicios médicos]
- **Carpetas de correo:** [ ]
- **Reuniones que nunca se transcriben:** evaluaciones de desempeño, procesos disciplinarios, conversaciones personales, [ ]

Las exclusiones se cumplen por dos vías: la instrucción al asistente y la decisión de no transcribir esas reuniones. Técnicamente, el conector puede leer todo lo que el gerente puede leer. Por eso la regla más fuerte es no transcribir lo que no deba procesarse.

## Qué hace con lo que lee

- Resume, extrae decisiones y compromisos, y responde preguntas citando la fuente.
- No envía correos ni mensajes: el conector está en solo lectura.
- Los temas de personal (salud, disciplina o pago de una persona) aparecen sin detalle.

## Dónde queda y cuánto se conserva

- En el historial de la cuenta de Claude del gerente, en plan Pro y con el uso de los chats para entrenamiento desactivado.
- Desde el nivel 2, en notas de la carpeta `Cerebro` de OneDrive, bajo las reglas de conservación de la empresa.
- Nunca en el repositorio de GitHub: ahí solo hay skills, plantillas y decisiones.
- **Plazo de conservación:** [por definir]. Si el piloto no continúa, se borran sus conversaciones y la carpeta `Cerebro`.

## Quién tiene acceso

Solo el gerente. Cuando envía un acta a los asistentes de una reunión, ellos también la reciben.

## Cómo se revoca

1. Desconectar Microsoft 365 en la cuenta de Claude (*Customize › Conectores*).
2. Pedirle a TI que revoque en Entra la aplicación «M365 MCP Server for Claude».
3. Borrar las skills y la tarea programada.

## Aviso de grabación

El aviso va en la descripción de cada reunión recurrente, antes de activar la transcripción automática. Además, Teams muestra su propio aviso cuando empieza a transcribir.

> Esta reunión se transcribe con Microsoft Teams. La transcripción la procesa un asistente de inteligencia artificial (Claude, de Anthropic) para preparar el acta y los compromisos de la gerencia de manufactura. Solo el gerente tiene acceso a ella. Si alguien no está de acuerdo, o prefiere que un tema no quede registrado, lo dice al inicio y la transcripción se detiene.

**Reuniones con externos (clientes, proveedores):** la transcripción no se activa de forma automática. Si se transcribe una, el aviso va en la invitación y se repite al empezar.
