---
title: "Tablero Comportamientos: documento de campos"
subtitle: "Grupo Pash. Solicitud para desarrollarlo en Onebeat (Jaguar+)"
lang: es
---

# 1. Qué se pide

Un tablero **Comportamientos** dentro de Onebeat, parecido al de Visual Merchandising, pero **por cápsula y por marca** y no solo por tienda. Hoy los compradores arman este análisis a mano, en una ficha por cápsula. Este documento lista los datos que necesita el tablero, de dónde salen hoy y qué hay que confirmar con Onebeat. El archivo `mockup-comportamientos.html` muestra cómo se vería, con datos de ejemplo.

Decisiones de Pash:

- La clasificación del producto es la de Onebeat: **Lanzamiento, Más vendido, Belly, Baja rotación y Sin rotación**. No se usa el semáforo «supera / no supera» del informe actual.
- La **evacuación ideal** la calcula Onebeat: compara la velocidad de ventas del producto-color con la media de su AG (Assortment Group).
- Estilo visual de Onebeat. La ficha es una vista dentro del tablero, no un PDF.

# 2. Campos del tablero

**Estado:** *Confirmado* = Pash lo verificó o ya lo vio en Onebeat. *Por confirmar* = pregunta abierta para Onebeat.

## 2.1 Cabecera de la cápsula

| Campo | Cómo se calcula | Origen hoy (informe de compradores) | En Onebeat | Estado |
|---|---|---|---|---|
| Ventas 30 días (unidades) | Suma de ventas de la cápsula en 30 días | Venta del mes | Ventas 30d | Confirmado |
| Stock en tienda | Unidades en tiendas | Existencia | Stock en tienda | Confirmado |
| Inventario de bodega | Unidades en bodega | Inventario de bodega | Inventario por SKU | Confirmado por Pash. Por confirmar que se pueda sumar por cápsula |
| Sell-through | Ventas ÷ (ventas + stock) | Evacuación % | Sell-through | Confirmado: es la misma fórmula |
| Cobertura (días) | Stock ÷ (ventas 30d ÷ 30) | Cobertura (en meses) | Cobertura | Confirmado |
| Margen % | (Precio − costo) ÷ precio | Margen | Beneficio bruto y margen | Por confirmar que llegue el costo por producto-color |
| Ventas e-commerce | Unidades vendidas por la página | Venta página | Ventas por SKU | Confirmado por Pash. Por confirmar que se pueda sumar por cápsula |
| Peso e-commerce | Ventas e-commerce ÷ ventas totales | No existe hoy | Calculado | Propuesta de Pash |
| Ventas por clima | Participación de cada clima (frío, templado, cálido) | Bloque por clima | Atributo de clima | Por confirmar |

## 2.2 Producto-color (tarjeta y detalle)

| Campo | Cómo se calcula | Origen hoy | En Onebeat | Estado |
|---|---|---|---|---|
| Foto, código, color | Del catálogo | Foto y código | Visual Merchandising | Confirmado |
| Clasificación | Lanzamiento, Más vendido, Belly, Baja rotación, Sin rotación | «Supera / no supera» | Desempeño | Confirmado |
| Antigüedad (días) | Días desde la primera entrada | Fecha de entrada | Antigüedad | Confirmado |
| Velocidad vs media del AG | Ventas 30d del producto-color ÷ media de su AG, menos 1 | Evacuación ideal | Desempeño vs media del AG | Por confirmar si la media se calcula por cápsula o solo por tienda |
| Precio de venta | Precio vigente | Precio | Precio | Confirmado |
| Costo | Costo unitario | Margen | No visto | Por confirmar |
| Margen | (Precio − costo) ÷ precio | Margen | Margen | Por confirmar |
| Ventas 30d, stock, bodega | Por producto-color | Venta del mes, existencia, bodega | Ventas 30d, stock | Confirmado |
| Sell-through y cobertura | Mismas fórmulas de la cabecera | Evacuación y cobertura | Sell-through y cobertura | Confirmado |
| Buffer y depleción de stock | Como en Visual Merchandising | No existe hoy | Buffer, depleción | Confirmado |
| Tallas: buffer y stock | Por talla | No existe hoy | Tallas del producto | Confirmado |

## 2.3 Cortes adicionales (en el detalle)

| Campo | Cómo se calcula | Origen hoy | En Onebeat | Estado |
|---|---|---|---|---|
| Ventas por clima | Ventas del producto-color por clima | Bloque frío, templado, cálido | Atributo de clima | Por confirmar |
| Ventas de la semana −1 y −2 | Ventas de las dos últimas semanas completas | Venta semana | Ventas 30/60/90 d | Por confirmar la ventana semanal |
| Ventas e-commerce 30d | Unidades por la página | Venta página | Ventas por SKU | Confirmado por Pash |
| Inventario por ubicación | Tienda y bodega | Existencia e inventario de bodega | Inventario por SKU | Confirmado por Pash |

## 2.4 Filtros y vistas

| Elemento | Detalle | Estado |
|---|---|---|
| Empresa / Tienda | Interruptor como el de Onebeat. Bodega y e-commerce no se abren por tienda | Por confirmar |
| Ventana «Filtros de parámetros» | Marca, Cápsula, Clima, Canal, Desempeño, AG, Producto Color, y señales de grade quebrada y sobrestock. Incluir o «todos excepto» | Por confirmar que cápsula y clima existan como filtro |
| Filtros rápidos | Las 5 clasificaciones, con colores de producto, stock, ventas 30d y cobertura | Confirmado |
| Vista Fichas y exportar | Una ficha por producto-color, exportable | Por confirmar el formato |

# 3. Preguntas para Onebeat

1. ¿La media del AG se puede calcular por cápsula, o solo por tienda?
2. ¿Se pueden sumar por producto-color y por cápsula las ventas, el stock de tienda, la bodega y el e-commerce?
3. ¿El clima, el costo y la venta de las semanas −1 y −2 existen por producto-color?
4. ¿Cómo se exporta una ficha por cápsula?

# 4. Anexo: estructura del informe actual

El informe actual es un PDF por cápsula, con corte a una fecha. Se arma a mano.

- **Encabezado de cápsula:** días desde la entrada, ventas, compra, evacuación, evacuación ideal, inventario, cobertura y venta del mes, con el desglose por clima.
- **Por producto-color:** entrada, venta total y del mes, % de venta, existencia, cobertura, precio, venta por día, evacuación ideal, venta e inventario de la página, cobertura de página, inventario de bodega, margen y ventas de las semanas −1 y −2, con el desglose por clima.

Aquí solo va la estructura. El informe real trae precios, costos y márgenes de Pash y no se comparte.
