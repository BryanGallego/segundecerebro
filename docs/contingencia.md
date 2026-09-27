# Contingencia · qué hacer cuando algo falla

Regla: ninguna falla se arregla en silencio. Cada una se anota en el registro de la semana (`Cerebro/registro-semana-1.md`, en OneDrive), con la fecha y lo que se hizo.

| Falla | Cómo se nota | Qué hacer |
|---|---|---|
| El brief no llega a las 6:00 | No aparece una ejecución nueva en la sección de tareas programadas | Abrir la tarea y ejecutarla en ese momento. Si vuelve a fallar, pedir «brief» en un chat nuevo y anotarlo. |
| El brief llega vacío o incompleto | La línea de salud trae ceros, o el brief empieza con «ATENCIÓN · No pude leer…» | Leer el motivo, reconectar Microsoft 365 en *Customize › Conectores* y volver a ejecutar. |
| El conector pide iniciar sesión de nuevo | Aviso de sesión vencida | Reconectar con la cuenta de la empresa. En Entra, la sesión dura por defecto 90 días. Si no funciona, llamar a TI. |
| TI revoca o cambia los permisos | Errores de permiso en el conector | Pedirle a TI que los restaure. Mientras tanto, el trabajo se hace a mano, como antes. |
| Claude no está disponible o se agotó el límite de uso | No responde, o avisa del límite | Trabajo a mano. Si el límite se agota seguido, evaluar el paso a Max. |
| Una skill empeora después de un cambio | Aumentan los errores del registro | Volver a subir el ZIP de la versión anterior, generado desde el commit anterior del repo. |
| Una reunión no tiene transcripción | La salud dice «N reuniones, M con transcripción» | Activar la transcripción en esa reunión recurrente. Esta vez, el acta se hace con notas dictadas. |
| Un correo trae instrucciones para el asistente | El brief lo reporta como correo con instrucciones | No hacer nada de lo que pide. Revisar el correo y, si es sospechoso, avisar a TI. |

**Límite de la semana 1:** no hay vigilante automático. Si la tarea no corre, solo el gerente lo nota. El vigilante con Power Automate llega con el nivel 2.
