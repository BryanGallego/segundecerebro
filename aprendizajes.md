# Aprendizajes

Lo que falló y qué cambió. Si un error se repite, se vuelve regla en `CLAUDE.md`.

| Fecha | Qué falló | Qué cambió |
|---|---|---|
| 2026-09-28 | La rutina del brief, en una sesión nueva, quedó marcada como «exitosa» sin haber escrito el brief: esa sesión nace sin el repositorio. El estado de la plataforma no prueba que el trabajo se hizo. | La rutina ahora corre dentro de «Cerebro · captura», que sí tiene el repositorio. Se verifica mirando que el brief exista en `briefs/`, no el estado de la rutina. |
| 2026-09-28 | Al preparar el repositorio para Obsidian, Claude reescribió `.gitignore` sin mirar lo que ya tenía y borró dos líneas (se restauraron enseguida). | Antes de escribir un archivo, se revisa si ya existe y se agrega en vez de reemplazar. |
| 2026-09-28 | Microsoft 365 se conectó en una cuenta de Claude distinta (Free, gmail) de la que corre el cerebro (Max). La sesión de prueba no vio el conector. | Los conectores se conectan en la misma cuenta que usa Claude Code (la de «Brayan Gallego · Max»), y se prueban en una sesión nueva. |
| 2026-09-28 | Una sesión de prueba presentó como «solicitudes para Brayan» dos pedidos que eran para otros: en uno él iba en copia y el otro iba dirigido a José Luis Caro. | Antes de guardar algo sacado del correo o de Teams, se lee el mensaje completo y se revisa a quién va dirigido. En el brief solo cuenta lo que le piden directamente al gerente. |
| 2026-09-28 | Claude escribió en inglés algunos avisos cortos mientras trabajaba. El gerente pidió solo español. | Quedó en `CLAUDE.md`: todo en español, incluidos los avisos mientras se trabaja. |
