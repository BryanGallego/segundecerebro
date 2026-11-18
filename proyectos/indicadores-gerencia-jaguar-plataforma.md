# Exploración de la plataforma Jaguar+ (Onebeat) para la matriz de indicadores

Fecha: 2026-11-18. Proyecto relacionado: `proyectos/indicadores-gerencia-jaguar.md`. Contraparte: [[Onebeat]].
Fuente: acceso de solo lectura con Chromium (Playwright) a la URL de tablero de Jaguar+ que dio el gerente en la tarea, 2026-11-18 ~16:00 UTC. No se cambió, guardó, aprobó ni envió nada, y no se usaron credenciales.

## Resultado corto
**La exploración quedó bloqueada en la entrada.** La plataforma no abre sin inicio de sesión y no se pudo recorrer ninguna pantalla. Por eso este archivo **no** contiene un inventario de pantallas, métricas o filtros de la plataforma: no está en lo que se pudo ver y no se rellena (regla 2).

## 1. Qué pantallas y métricas existen (nombre exacto)
**No verificado en la plataforma.** Lo único observado:

- La dirección carga una aplicación web titulada «Onebeat Jaguar Plus» (logo de Onebeat, fondo azul oscuro).
- La única pantalla visible fue un aviso de error de inicio de sesión: texto «We could not reach the sign-in service.» y un botón «Try again». No hubo formulario de usuario y contraseña, ni botón de SSO, ni menús, ni tableros detrás.
- La causa no se pudo establecer: el servicio de autenticación no respondió desde el entorno de la sesión (puede ser el bloqueo de red del entorno o que el servicio exige otro acceso). No se probó nada más para saltarlo.

Los nombres de pantallas que sí constan por escrito vienen del PDF y la matriz (no de la plataforma), y están en `proyectos/indicadores-gerencia-jaguar.md`: Heat Map, Coverage, Pareto, Performance, Visual Merchandising / Playground, Reposición Inteligente, Estacionalidad y Campañas. «CEO», «CFO», «CCO», «Asignación» e «IST» no aparecen en ese documento; su existencia y sus nombres exactos quedan sin confirmar.

## 2. Indicadores de la matriz soportados por la plataforma
**No se puede decidir con esta exploración.** Lo que hay es la lectura del PDF de Onebeat (ver «Brechas» en el archivo de la matriz), que es lo que Onebeat dice que ofrece, no lo que se comprobó en pantalla:

| Workflow de la matriz | Estado según el PDF (sin verificar en plataforma) |
|---|---|
| Cobertura, Pareto, Performance, Reposición Inteligente (parcial), Heat Map (parcial) | El PDF trae fichas o láminas; falta confirmar el nombre de la métrica y el filtro en la plataforma |
| Estacionalidad y Campañas | El PDF no trae ningún KPI; falta ver si la plataforma lo ofrece |
| Visual Merchandising, Playground | Solo láminas descriptivas en el PDF; falta ver las vistas y la lista de métricas, filas y columnas |
| Workflows 9–13 (Comportamientos, Lanzamientos y Allocation, Traslados, Canal, Calidad de datos y adopción) | Sin evidencia ni a favor ni en contra |

## 3. Lo que no se pudo ver
- Todo lo que está detrás del inicio de sesión: menús, paneles CEO / CFO / CCO, Coverage, Pareto, Heat Map, Performance, Visual Merchandising, Playground (métricas, filas y columnas), Reposición, Asignación, IST, Estacionalidad y Campañas.
- Nombres exactos de métricas y filtros, y si hay corte por canal (tienda vs. e-commerce), por cápsula o por producto-color.
- Si la plataforma muestra calidad de datos o adopción de recomendaciones.

## Cómo desbloquearlo
1. Reintentar desde una red con acceso al servicio de inicio de sesión, o pedir a [[Hugo Carvalho]] / [[Andrés Alfonso]] cómo se accede a un usuario de solo lectura.
2. Alternativa que no requiere acceso: que Onebeat envíe la lista de pantallas y métricas (capturas o PDF) y el gerente la mande por el celular para guardar sus nombres exactos.
3. Para entrar, la persona con acceso debe iniciar sesión ella misma; yo no pido ni uso credenciales por mi cuenta.
