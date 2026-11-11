# Propuesta: el informe de «comportamientos» de los compradores en Onebeat (Jaguar+)

Pedido de [[Sophie Douer]] a [[Brayan Gallego]], 2026-11-09 9:55 (WhatsApp): «revisate los informes de comportamientos que hacen los compradores a ver cuál sería el paralelo en Onebeat, y cómo lo podríamos hacer con eso. Los nuestros no están tan bien hechos tampoco y son muy manuales.» Brayan respondió a las 10:01 que busca hoy una cita con el equipo para entenderlos, compararlos y diseñar la propuesta.

## Fuentes leídas (solo lectura)

- Correo «RV: Comportamientos Femenino 31.10.2026»: lo envió Magali Garzón (Analista de Negocios, Patprimo) a Sophie y Pepe Douer el 2026-11-03 a las 14:16, con copia a unas 25 personas de Pash; [[Giomar Sarmiento]] se lo reenvió a Brayan el 2026-11-09 a las 12:44. Trae 29 PDF, uno por cápsula, agrupados por módulo M1 a M6. **Leí 2 de los 29:** «3315 – PAT CLUB» (M3) y «3531 – SMART OFFICE» (M6). No sé qué significa el sufijo «TG» de algunos archivos.
- Correo «Informes One Beat Negocios», de María Luisa Ochoa (Directora de Negocios) a Gustavo Ospina y Brayan, 2026-10-05 10:02, con el archivo «ONE BEAT - INFORMES NEGOCIOS.xlsx»: la lista de deseos de Negocios tras reunirse con Sophie y Pepe. Brayan contestó ese día a las 10:11 que convenía «desbloquear esta fase y avanzar en la consolidación de la matriz de indicadores estratégicos, tácticos y operativos».
- Correo de Andrés Alfonso (Onebeat) del 2026-10-09, reenviado a Brayan el 2026-10-13: video del Playground (3 min) y la presentación «KPIs_Onebeat_Grupo_Pash.pdf». Dice que los KPIs recomendados «se pueden construir directamente en el Playground».
- Correo de Andrés Alfonso del 2026-11-04: terminó la configuración en las 4 marcas (reglas de negocio, e-commerce, buffers, reposición y mapeo de atributos).

## Qué es el informe de comportamientos hoy

Una ficha por cápsula, con corte al 2026-10-31.

**Encabezado de cápsula** (ejemplo PAT CLUB): días desde la entrada, ventas, compra, evacuación %, evacuación ideal, inventario, cobertura en meses y venta del mes, con el desglose por clima (cálido, templado, frío).

**Detalle por referencia-color** (ejemplo código 30080603, café): fecha de entrada, entrada, venta total, venta del mes, % de venta, existencia, cobertura en meses, ventas de las semanas −1 y −2, margen, precio, venta por día, evacuación ideal, venta e inventario de la página, cobertura de página, inventario en bodega, y la marca «NO SUPERA».

**Lo que pude verificar con los números de los dos PDF:**

| Campo del informe | Verificación | Lectura |
|---|---|---|
| COMPRA = VTA + INV | PAT CLUB: 11.390 + 10.924 = 22.314. SMART OFFICE: 77 + 363 = 440 | La «compra» del informe es en realidad lo vendido más lo que queda en stock |
| EVAC = VTA ÷ COMPRA | 11.390 ÷ 22.314 = 51 %. 77 ÷ 440 = 17,5 % (el PDF dice 18 %) | **Es la misma fórmula del sell-through de Onebeat:** vendido ÷ (vendido + stock) |
| COBERTURA = INV ÷ VENTA MES | 10.924 ÷ 1.755 = 6,2 meses | Es la cobertura 30d de Onebeat: stock ÷ ventas 30d, en meses |
| DIAS | Entrada 24/12/2025 → corte 31/10/2026 = 311 días. Entrada 23/09/2026 → 38 días | Días desde la primera entrada hasta el corte |
| IDEAL | SMART OFFICE: 42 % ideal a los 38 días contra 18 % real, con la marca «NO SUPERA». PAT CLUB: «#N/D» | Curva objetivo de evacuación según días en tienda. No está definida para todas las cápsulas |

Esto se lee como: «NO SUPERA» = la evacuación real no alcanza la ideal. Es lectura mía, hay que confirmarla.

## Paralelo en Onebeat (Jaguar+)

| Informe de compradores | Equivalente en Jaguar+ | Estado |
|---|---|---|
| Evacuación % | Sell-through (historial), por colección, AG, tienda | **Mismo cálculo.** Cubierto |
| Cobertura (meses) | Cobertura 30d y Cobertura inteligente (solo stock sano), pantalla Coverage | Cubierto. La inteligente aporta más que el informe actual |
| Venta del mes, semana −1 y −2 | Ventas 30/60/90 d en Playground | Venta mensual: cubierto. **Semanal: por confirmar** |
| Inventario, existencia | Unidades y valor del stock; Playground | Cubierto |
| Días desde entrada | Antigüedad (bandas 0–3, 4–6, 7+ meses) y tier Freshness | Parcial: Onebeat da bandas, no días exactos |
| Clima (cálido/templado/frío) | Se puede usar como fila o columna en Playground **si el atributo está cargado** | **Por confirmar** que el clima de la tienda esté en el catálogo |
| Cápsula, UEN, ocasión de uso | Idem: atributos de producto | **Por confirmar** que estén en el mapeo de atributos |
| Margen % | Beneficio bruto y % margen | Depende de que llegue el costo; si no llega, sale en cero sin avisar |
| Top / bottom, cabeza–vientre–cola | Performance (Bestseller deciles 1–3, Belly 4–7, Slowmover/Nomover 8–11) y Pareto 80 % / Bottom 30 % / No Movers | Cubierto (la equivalencia cabeza–vientre–cola es lectura mía) |
| «NO SUPERA» | Semáforo de cada KPI; Heat Map (Winner at Risk, Fast Money, Frozen Cash) | Parcial: falta la curva ideal propia de Pash |
| **Evacuación ideal** | No hay equivalente directo; el semáforo de sell-through se lee «a qué altura de la temporada» | **Brecha principal.** Pash tiene que definir la curva por cápsula |
| Venta, inventario y cobertura de página; inventario en bodega | Tienda Online como ubicación; stock del CD | Por confirmar (Onebeat dice que e-commerce quedó configurado) |
| Compra (OTB, cortes B, presupuesto de compra) | No aparece en los KPIs que mostró Onebeat | **Brecha:** hay que preguntar si hay módulo |

**Lista de deseos de Negocios (5 informes) contra lo que muestra Onebeat:**

1. *Ventas, margen y markdown vs LY:* ventas y margen están; faltan comparativo vs LY y presupuesto, markdown, full/promo y pronóstico de cierre. Brayan anotó por Teams el 2026-11-06 que el campo full/promo está mal en Onebeat (es un porcentaje) y que hay que corregirlo en el catálogo.
2. *Inventario total, cobertura total, on order (importado, nacional, externo):* inventario y cobertura están; la mercancía por llegar (on order) no aparece.
3. *Sell-through y productividad (cabeza–vientre–cola):* es el informe de comportamientos; **el paralelo más directo.**
4. *OTB (compra + cortes B)* y 5. *Presupuesto de compra (estructura, eficiencia):* solo hay cobertura parcial con Pareto y variedad; no vi OTB.

La lista termina con dos preguntas abiertas: «¿Cómo se vería el informe? Formato» (asignada a Brayan) y «¿Dónde vamos a meter la info de telas, patterns y colores para darle la data a Diseño?».

## Cómo hacerlo (fases)

0. **Hoy · entender.** Cita de 45 min con quien arma el informe (Magali Garzón) y Negocios (María Luisa Ochoa, Juanita De la Vega). Pedir ver cómo lo arman, de qué fuentes (la columna «Equivalente Actual» de la lista de deseos nombra «Comparativo / BI Márgenes», «Inventario + Status Producción» y «Gestión Inseason»), cuánto tardan y qué decisiones toman con él.
1. **Esta semana · prototipo de una cápsula.** Reproducir la ficha de PAT CLUB y de SMART OFFICE en el Playground (filas: referencia-color; columnas: clima; métricas: ventas 30d, stock, sell-through, cobertura, margen). **Criterio de éxito: que cuadre con el PDF** (ventas + stock = «compra», evacuación y cobertura iguales).
2. **Siguiente · curva ideal.** Que Negocios defina la evacuación ideal por días desde la entrada y por tipo de cápsula, y pedir a Onebeat dónde cargarla como referencia para marcar «NO SUPERA».
3. **Después · vista guardada.** Vista de Playground por cápsula con exportación a Excel/PDF, y una rutina semanal acordada (la guía de Onebeat sugiere 30 min semanales).
4. **Luego · resto de la lista de deseos** (márgenes, on order, OTB) según lo que Onebeat tenga o desarrolle.

## Preguntas para Onebeat (llevarlas a la reunión de las 13:00 del 2026-11-09)

1. ¿Playground permite ventana semanal (semana −1, −2)? ¿Y días exactos desde la entrada?
2. ¿Están cargados los atributos clima, UEN, ocasión de uso, cápsula y fecha de primera entrada para las 4 marcas?
3. ¿Se puede cargar una curva de «evacuación ideal» como referencia o semáforo propio?
4. ¿Cómo se ve la venta por canal (Tienda Online / página) y el inventario de bodega por referencia?
5. ¿Hay módulo u opción para OTB, cortes B y mercancía por llegar (on order)?
6. ¿Se puede comparar contra el mismo período del año anterior y contra presupuesto?
7. ¿Qué formato de exportación entrega mejor una ficha por cápsula (PDF o Excel)?

## Preguntas para el equipo de compradores

1. ¿Qué fuente y qué corte usan (ventas, inventario, margen)? ¿Quién lo arma y cuánto tarda cada semana?
2. ¿Qué es «IDEAL»? ¿Cómo se calcula y por qué PAT CLUB aparece «#N/D»?
3. ¿Qué significa «NO SUPERA», «TG» y «página»?
4. ¿Qué decisiones se toman con la ficha (recompra, markdown, traslado)?
5. ¿Qué les falta o les sobra del informe actual?

## Riesgos

- Solo leí 2 de 29 fichas: las definiciones salen de ahí y de los encabezados.
- Si costo o fecha de primera entrada no llegan completos a Jaguar+, margen y antigüedad salen mal (lo advierte la propia presentación de Onebeat).
- El informe actual cambió de corte (31.10) y de universo (solo femenino); la comparación debe usar el mismo corte.
- La inversión de tiempo depende de que Onebeat confirme los puntos de la tabla marcados «por confirmar».

## Prototipo «Comportamientos» (2026-11-11)

Prototipo privado con datos de ejemplo, en el estilo de Onebeat y con las fotos de polo del tablero de Visual Merchandising: https://claude.ai/artifact/JQhUdyZCVdQ1F4o2ko7Psq (versión 16). Es para presentarlo a Onebeat en la reunión de las 9:00 del 2026-11-11 (Brayan, mensaje del 2026-11-11).

**Decisiones de Brayan (mensajes del 2026-11-11):**
- SUPERA / NO SUPERA y el % de cumplimiento **no van**. Los reemplaza la clasificación de Onebeat: Lanzamiento, Más vendido, Belly, Baja rotación y Sin rotación.
- La evacuación ideal sale de Onebeat: se compara la velocidad del producto-color con la media del AG (Assortment Group).
- Estilo de Onebeat, no el del PDF de los compradores. La ficha es una vista dentro del tablero.
- Filtros como los de Onebeat: botón «Filtros» con ventana de parámetros (Catálogo y Señales; incluir o «todos excepto») e interruptor Empresa | Tienda.
- Cada tarjeta lleva antigüedad (pie de la foto), precio de venta, costo y margen, y bodega. Sin inventario de página.
- En la cabecera: ventas, stock en tienda, inventario de bodega, sell-through, cobertura, margen, ventas y peso del e-commerce.
- Se quitó: selector de corte, bloque Reposición & Transferencia, ranking y señales del panel derecho, y el menú lateral.

**Datos confirmados por Brayan (2026-11-11):** Onebeat ya tiene por SKU las ventas del e-commerce y los inventarios de bodega y de tienda. Esa brecha de la tabla de arriba queda cerrada en datos.

**Lo que mostré en el prototipo y no está confirmado con Onebeat:**
- vista por cápsula o marca (el tablero actual es por tienda);
- atributo clima;
- costo y margen por producto-color;
- ventas de semana −1 y −2;
- formato ficha y exportación.

**Lo que mostré como si ya existiera y es de ejemplo:** todas las cifras, los códigos, la cápsula M5 · Natural, la marca de cada producto, las tiendas y el inventario de bodega. El peso del e-commerce de la cabecera es una cifra inventada. En el PDF M5 Natural NOD la venta de página es 0 en los 10 productos (revisé solo ese PDF de 29).

**Preguntas para la reunión de las 9:00:**
1. ¿La media del AG se puede calcular por cápsula o solo por tienda?
2. ¿Se pueden sumar por producto-color y por cápsula las ventas, el stock de tienda y la bodega?
3. ¿El clima, el costo y la semana −1/−2 existen por producto-color?
4. ¿Hay forma de exportar una ficha por cápsula?
