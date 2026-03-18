# ============================================================
# control_01_tienda_libros.py
# ============================================================
# Control No.1 - Tienda de Libros
#
# Una tienda de libros necesita calcular el precio total de un libro.
# Ingresar: ISBN y título del libro.
#
# Reglas de precio:
# - Portada suave: $10.000
# - Portada dura:  $15.000
# - Cada página:   $10
#
# Descuentos sobre el pago bruto:
# - Menos de 500 páginas:        sin descuento
# - Entre 500 y 1000 páginas:    3% de descuento
# - Entre 1001 y 2000 páginas:   7% de descuento
# - Más de 2000 páginas:         9% de descuento
#
# Mostrar: ISBN, título, tipo de portada, número de páginas,
#          pago bruto, descuento y pago total.