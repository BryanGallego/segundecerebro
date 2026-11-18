# Segunda propuesta de indicadores para la gerencia (Jaguar+)

Estado: borrador de diseño, 2026-11-18. Responsable: [[Brayan Gallego]]. Contraparte: [[Onebeat]] ([[Hugo Carvalho]], [[Andrés Alfonso]], [[Fabricio García]]).

## Fuentes
- Correo de Brayan Gallego, 2026-11-11 15:36, «RE: Propuesta Indicadores para el Grupo Pash desde Jaguar+», con el Excel «Matriz de Indicadores Grupo Pash.xlsx» (columnas: WorkFlow | Área | Tipo | Tablero | Propósito | Cómo Leerlo | Métricas | Alcance).
- PDF «KPIs_Onebeat_Grupo_Pash.pdf» (Andrés Alfonso, 2026-10-09; reenviado por Hugo Carvalho el 2026-11-13 13:28). **Confirmado por Brayan (2026-11-18, chat):** es el PDF que envió [[Hugo Carvalho]]. En el buzón es el único correo de Hugo con el PDF adjunto (2026-11-13 13:28; el original es del 2026-10-09).
- Casos de trabajo ya hechos con Onebeat: «Comportamientos» (`proyectos/comportamientos-compradores-onebeat.md`). Por confirmar si «los casos» son estos u otros.

## Qué trae el PDF de Onebeat
24 fichas de KPI ordenadas por **nivel × módulo** (estratégico / táctico / operativo): ventas 30/60/90, beneficio y % margen, GMROI, rotación, stock y valor, stock muerto, sell-through, ventas perdidas ($ y u), recuperado por traslados, cobertura (30d vs inteligente), disponibilidad, excedentes, penetración de buffer, curva rota, antigüedad, variedad y cobertura antes/después (allocation), % buffer rojo/amarillo/verde, necesidades-reposición-tránsito, faltas, gestión de traslados. Más cuatro láminas de tableros (Heat Map, Coverage, Pareto, Performance, VM/Playground), una tabla de «KPIs recomendados para Pash» con responsable «[Nombre]» y tres rutinas (diaria, semanal, mensual).

## Brechas frente a la matriz de Brayan
1. **Otra lógica de organización.** Brayan pidió *workflows* (procesos) con propósito, alcance, cómo leerlo y métricas. Onebeat entregó un catálogo por nivel y módulo; el lector de la gerencia tiene que reconstruir el proceso.
2. **Workflows de la matriz sin cubrir.** *Estacionalidad y Campañas* no tiene ningún KPI (factor y matriz de estacionalidad). *Reposición Inteligente* solo aparece como necesidad/reposición/tránsito, sin la «Escala de prioridad». *Visual Merchandising*, *Performance* y *Playground* aparecen como láminas descriptivas, no como indicadores. *Heat Map* trae los 6 problemas pero sin una cifra de gerencia (costo total por problema, tendencia).
3. **Semáforos genéricos.** Las bandas son «referencia fashion retail», no calibradas con la historia de Pash; los ejemplos son «ilustrativos» (cifras inventadas). La gerencia no puede decidir con ellos.
4. **Sin dueño ni decisión.** La columna «Responsable» quedó en «[Nombre]» y no hay qué decisión se toma ni quién la firma.
5. **Sin lo que ya definimos nosotros.** No incluye «Comportamientos» por producto-color y cápsula (30/60/90 d, margen, precio, costo, antigüedad, bodega, peso del e-commerce), ni el canal e-commerce vs. tiendas como corte de gerencia.
6. **Sin calidad de datos.** Los mismos tips del PDF avisan que sin costo, precio o fecha de entrada los KPIs salen en cero o «viejos» sin avisar; no hay un KPI que lo vigile.
7. **Sin vínculo con la cadena de abastecimiento.** Nada conecta la señal de venta/cobertura con compras, tela y producción (plazo de reposición, órdenes, buffer crudo), que es lo que la gerencia de manufactura necesita.
8. **Sin medición de adopción.** Hay % de traslados aprobados, pero no cuánto de lo que recomienda Jaguar+ se ejecuta realmente ni su efecto.

## Propuesta: estructura de la segunda versión
Conservar las columnas de Brayan y añadir: **Pregunta de gerencia** | **Fórmula** | **Fuente / campo** | **Estado** (existe en Jaguar+ · por construir · requiere dato de Pash) | **Dueño** | **Frecuencia** | **Semáforo Pash** (se calibra con 8–12 semanas de historia) | **Decisión que habilita**.

### Workflows (13)
| # | Workflow | Nivel | Qué agrega frente a Onebeat |
|---|---|---|---|
| 1 | Reposición Inteligente | Táctico/Operativo | Escala de prioridad; % necesidad cubierta; días de respuesta CD→tienda |
| 2 | Estacionalidad y Campañas | Táctico | Factor de estacionalidad; error de pronóstico por campaña; venta de campaña vs. plan (**vacío en el PDF**) |
| 3 | Análisis de Pareto | Estratégico | Pareto 80%, Bottom 30%, sin movimiento, venta e inventario por edad (existe) + % de capital en cola |
| 4 | Heat Map | Estratégico | Costo total en $ por problema y su tendencia semanal; qué parte se recuperó |
| 5 | Visual Merchandising | Táctico | % de producto con foto/estado local; grilla rota con solución vs. sin solución |
| 6 | Performance (tiers) | Estratégico/Táctico | Distribución HEAD/BELLY/TAIL por colección; rotación entre tiers |
| 7 | Cobertura | Táctico | Cobertura vs. inteligente por AG; bandas relativas y absolutas |
| 8 | Playground | Táctico | Vistas guardadas fijas para gerencia (no KPI nuevo) |
| 9 | **Comportamientos** (nuevo) | Estratégico/Táctico | Producto-color y cápsula: ventas 30/60/90, margen, precio, costo, antigüedad, bodega, peso e-commerce |
| 10 | **Lanzamientos y Allocation** (nuevo) | Táctico | Sell-through temprano de lanzamiento; variedad cumplida; cobertura antes→después |
| 11 | **Traslados entre tiendas** (nuevo) | Operativo/Estratégico | % gestionado, venta recuperada realizada vs. proyectada |
| 12 | **Canal: tienda vs. e-commerce** (nuevo) | Estratégico | Peso del e-commerce por cápsula; disponibilidad y venta perdida por canal |
| 13 | **Calidad de datos y adopción** (nuevo) | Operativo | % SKU con costo, precio y fecha de entrada; % de recomendaciones ejecutadas |

### Reglas de diseño
- Máximo 5–7 indicadores por workflow; el resto queda como apoyo.
- Cada indicador: fórmula escrita como suma÷suma (no promedio de razones), como dice el propio PDF.
- Cada semáforo se marca «referencia Onebeat» hasta calibrarlo con datos de Pash.
- Cada workflow con un dueño nombrado y una frecuencia.

## Pendiente por decidir con Brayan
1. Confirmar cuáles son «los casos» (el PDF ya está confirmado).
2. ¿Los 5 nuevos workflows (9–13) van en esta versión o en una tercera?
3. ¿La gerencia ve solo estratégicos, o también tácticos?
4. Dueños por workflow (¿quién de Pash?).
5. Si se incluye el vínculo con compras/tela/producción (brecha 7), qué datos de Pash se pueden compartir con Onebeat (el repositorio y los datos de Pash no se copian fuera).
