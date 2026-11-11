---
title: "Tablero Comportamientos: documento de campos"
subtitle: "Grupo Pash. Solicitud para desarrollarlo en Onebeat (Jaguar+)"
lang: es
---

# 1. Qué se pide

Un tablero **Comportamientos** dentro de Onebeat, parecido al de Visual Merchandising, pero por atributos: de cápsula y por marca y no solo por tienda. Hoy los compradores arman este análisis a mano, en una ficha por cápsula. Este documento lista los datos que necesita el tablero, de dónde salen hoy y qué hay que confirmar con Onebeat. El archivo `mockup-comportamientos.html` muestra cómo se vería, con datos de ejemplo.

Decisiones de Pash:

- La clasificación del producto es la de Onebeat: **Lanzamiento, Más vendido, Belly, Baja rotación y Sin rotación**. No se usa el semáforo «supera / no supera» del informe actual.
- La **evacuación ideal** la calcula Onebeat: compara la velocidad de ventas del producto-color con la media de su AG (Assortment Group).
- **Ventana de ventas:** el tablero permite elegir 30, 60 o 90 días, como el selector «Ventana de ventas» de Onebeat. Esa ventana alimenta todos los datos de la pantalla. Onebeat ya tiene las tres calculadas.
- Estilo visual de Onebeat. La ficha es una vista dentro del tablero, no un PDF.

# 2. Campos del tablero

**Estado:** *Confirmado* = Pash lo verificó o ya lo vio en Onebeat. *Por confirmar* = pregunta abierta para Onebeat.

## 2.1 Cabecera de la cápsula

| Campo | Cómo se calcula | Origen hoy (informe de compradores) | En Onebeat | Estado |
|---|---|---|---|---|
| Ventas de la ventana (unidades) | Suma de ventas de la cápsula en la ventana elegida: 30, 60 o 90 días | Venta del mes (solo 30 días) | Ventana de ventas 30d / 60d / 90d | Confirmado: Onebeat ya las tiene calculadas |
| Stock en tienda | Unidades en tiendas | Existencia | Stock en tienda | Confirmado |
| Inventario de bodega | Unidades en bodega | Inventario de bodega | Inventario por SKU | Confirmado |
| Sell-through | Ventas de la ventana ÷ (ventas de la ventana + stock) | Evacuación % | Sell-through | Confirmado: es la misma fórmula |
| Cobertura (días) | Stock ÷ (ventas de la ventana ÷ días de la ventana) | Cobertura (en meses) | Cobertura | Confirmado |
| Margen % | (Precio − costo) ÷ precio | Margen | Beneficio bruto y margen | Confirmado |
| Ventas e-commerce | Unidades vendidas por la página | Venta página | Ventas por SKU | Confirmado |
| Peso e-commerce | Ventas e-commerce ÷ ventas totales | No existe hoy | Calculado | Propuesta de Pash |
| Ventas por clima | Participación de cada clima (frío, templado, cálido) | Bloque por clima | Atributo de clima por localización | Confirmado |

## 2.2 Producto-color (tarjeta y detalle)

| Campo | Cómo se calcula | Origen hoy | En Onebeat | Estado |
|---|---|---|---|---|
| Foto, código, color | Del catálogo | Foto y código | Visual Merchandising | Confirmado |
| Clasificación | Lanzamiento, Más vendido, Belly, Baja rotación, Sin rotación | «Supera / no supera» | Desempeño | Confirmado |
| Antigüedad (días) | Días desde la primera entrada | Fecha de entrada | Antigüedad | Confirmado |
| Velocidad vs media del AG | Ventas de la ventana del producto-color ÷ media de su AG en la misma ventana, menos 1 | Evacuación ideal | Desempeño vs media del AG | Por confirmar si la media se calcula por cápsula o solo por tienda |
| Precio de venta | Precio vigente | Precio | Precio | Confirmado |
| Costo | Costo unitario | Margen | Costo por producto-color | Confirmado |
| Margen | (Precio − costo) ÷ precio | Margen | Margen | Confirmado |
| Ventas de la ventana, stock, bodega | Por producto-color; ventas en 30, 60 o 90 días | Venta del mes, existencia, bodega | Ventas 30d, stock | Confirmado |
| Sell-through y cobertura | Mismas fórmulas de la cabecera | Evacuación y cobertura | Sell-through y cobertura | Confirmado |
| Buffer y depleción de stock | Como en Visual Merchandising | No existe hoy | Buffer, depleción | Confirmado |
| Tallas: buffer y stock | Por talla | No existe hoy | Tallas del producto | Confirmado |

## 2.3 Cortes adicionales (en el detalle)

| Campo | Cómo se calcula | Origen hoy | En Onebeat | Estado |
|---|---|---|---|---|
| Ventas por clima | Ventas del producto-color por clima | Bloque frío, templado, cálido | Atributo de clima por localización | Confirmado |
| Ventas de la semana −1 y −2 | Ventas de las dos últimas semanas completas | Venta semana | Ventas 30/60/90 d | Confirmado |
| Ventas e-commerce de la ventana | Unidades por la página en la ventana elegida | Venta página | Ventas por SKU | Confirmado |
| Inventario por ubicación | Tienda y bodega | Existencia e inventario de bodega | Inventario por SKU | Confirmado |

## 2.4 Filtros y vistas

| Elemento | Detalle | Estado |
|---|---|---|
| Ventana de ventas | Selector 30d / 60d / 90d, como en Onebeat. Cambia ventas, sell-through, cobertura y la comparación con la media del AG | Confirmado: Onebeat ya las tiene calculadas |
| Empresa / Tienda | Interruptor como el de Onebeat. Bodega y e-commerce no se abren por tienda | Por confirmar |
| Ventana «Filtros de parámetros» | Marca, Cápsula, Clima, Canal, Desempeño, AG, Producto Color, y señales de grade quebrada y sobrestock. Incluir o «todos excepto» | Por confirmar que cápsula y clima existan como filtro |
| Filtros rápidos | Las 5 clasificaciones, con colores de producto, stock, ventas de la ventana y cobertura | Confirmado |
| Vista Fichas y exportar | Una ficha por producto-color, exportable | Por confirmar el formato |

Hoy el informe de los compradores y el tablero de ejemplo solo registraban 30 días. La ventana de 60 y 90 días es nueva en este documento.

# 3. Preguntas para Onebeat

1. ¿La media del AG se puede calcular por cápsula, o solo por tienda?
2. ¿Cómo se exporta una ficha por cápsula?

# 4. Anexo: estructura del informe actual

El informe actual es un PDF por cápsula, con corte a una fecha. Se arma a mano.

- **Encabezado de cápsula:** días desde la entrada, ventas, compra, evacuación, evacuación ideal, inventario, cobertura y venta del mes, con el desglose por clima.
- **Por producto-color:** entrada, venta total y del mes, % de venta, existencia, cobertura, precio, venta por día, evacuación ideal, venta e inventario de la página, cobertura de página, inventario de bodega, margen y ventas de las semanas −1 y −2, con el desglose por clima.
