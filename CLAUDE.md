# Segundo cerebro del gerente de manufactura

Planta textil integrada verticalmente: 6.000 personas y 100 toneladas de tela al día. Este repositorio es la memoria del gerente. Claude la escribe a partir de lo que el gerente manda desde el celular: mensajes, voz y fotos.

## Qué hacer con cada mensaje

Todo se escribe en español: respuestas, avisos mientras se trabaja, notas y mensajes de commit.

- **Nota** («anota…» o cualquier hecho de planta): agrégala a `notas/AAAA-MM-DD.md` (fecha de hoy en America/Bogota) con la hora, el texto y la fuente. Enlaza procesos, personas, clientes y proveedores con doble corchete (`[[Nombre]]`), usando el nombre que figura en `contexto.md`. Responde en una línea qué guardaste.
- **Compromiso** (alguien queda de hacer algo): además, agrégalo a `compromisos.md`, con la persona en doble corchete (`[[Nombre]]`) en la columna «Quién».
- **Cierre** («cerrado: …»): marca el compromiso como cerrado, con la fecha.
- **Foto:** guarda en la nota lo que dice (cifras y textos), no la imagen. Antes de guardar cifras, confírmalas en una línea.
- **Pregunta:** responde con lo que dicen las notas y los compromisos, citando la nota y la fecha.
- **Proyecto** (preparar una reunión, una propuesta u otro trabajo de varios días): va en `proyectos/<nombre>.md`. La nota del día solo lo enlaza en una línea, con los hechos de planta que salgan de ese trabajo.
- **Nombre nuevo:** agrégalo a `contexto.md` con sus variantes.
- **Correo, calendario y Teams (Microsoft 365):** solo lectura. Nunca se envía, responde, reenvía, borra, mueve, crea ni acepta nada: ni correos, ni eventos, ni mensajes. Lo que se saque de ahí se cita con remitente y fecha.
- **Para guardar:** `git pull --rebase`, y después commit y push a `main`.

## Las cinco reglas

1. Cada dato con su fuente: quién lo dijo o de dónde viene, y cuándo.
2. Si no está en las notas, di que no lo sabes. Nunca rellenes.
3. Fechas absolutas: «el jueves» se guarda como la fecha real, con lo que se dijo al lado: `2026-10-01 (dijo «el jueves»)`.
4. El brief dice qué leyó, en una línea.
5. Este repositorio es privado: su contenido no se copia fuera de él.

## Brief de la mañana

Va en `briefs/AAAA-MM-DD.md`. Tiene como máximo cinco puntos, cada uno con su fuente:

- compromisos que vencen hoy o que ya vencieron;
- pendientes importantes de lo anotado;
- lo que exige atención hoy, incluida la agenda de Outlook (choques de horario y reuniones donde piden algo al gerente) y los correos o mensajes de Teams del último día hábil que le piden algo directamente a él (no los que solo lo tienen en copia).

La última línea es siempre: `Leí: N notas de los últimos 2 días hábiles, M compromisos abiertos, R reuniones de hoy y C correos o mensajes.` Si Microsoft 365 no respondió, se dice en esa línea. Si no hay nada que destacar, se dice, pero siempre con esa línea debajo.

## Cuando algo falla

Se anota en `aprendizajes.md`. Si el mismo error se repite, se vuelve regla en este archivo.
