# main.py
# Punto de arranque del programa.
# Se crean los objetos, se agregan al servicio principal
# y se llaman los metodos para mostrar el funcionamiento
# del sistema de gestion del restaurante.

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():

    # crear el servicio principal
    restaurante = Restaurante("Garcia y Punto", "Ambato")
    print(restaurante)

    # crear productos de distintos turnos
    p1 = Producto("D01", "Bolon de verde con cafe",  "Desayuno", 2.50)
    p2 = Producto("D02", "Jugo de naranja",          "Desayuno", 1.25)
    p3 = Producto("A01", "Sopa de lentejas",         "Almuerzo", 2.00)
    p4 = Producto("A02", "Pollo asado con papas",    "Almuerzo", 5.50)
    p5 = Producto("A03", "Limonada natural",         "Almuerzo", 1.50)
    p6 = Producto("C01", "Carne en salsa de tomate", "Cena",     6.00)
    p7 = Producto("C02", "Arroz con menestra",       "Cena",     4.75)

    # agregar productos a la carta
    for producto in [p1, p2, p3, p4, p5, p6, p7]:
        restaurante.agregar_producto(producto)

    # desactivar un producto que se acabo
    p3.desactivar()

    # actualizar precio de uno de los platos
    p4.actualizar_precio(5.00)

    # mostrar la carta completa
    restaurante.mostrar_carta()

    # mostrar solo los productos del almuerzo
    restaurante.carta_por_turno("Almuerzo")

    # crear clientes con reserva
    c1 = Cliente("1804001122", "Cristian Omar Garcia Aguilar", "0987000111", 2)
    c2 = Cliente("1805002233", "Veronica Aguilar",             "0991112233", 4)
    c3 = Cliente("1806003344", "Marco Saltos",                 "0976543210", 3)

    # cancelar la reserva de uno de los clientes
    c3.cancelar_reserva()

    # modificar el numero de personas de otro cliente
    c2.actualizar_personas(6)

    # registrar los clientes en el sistema
    restaurante.agregar_cliente(c1)
    restaurante.agregar_cliente(c2)
    restaurante.agregar_cliente(c3)

    # mostrar todas las reservas
    restaurante.mostrar_reservas()

    # buscar un cliente por cedula
    print("\nBusqueda por cedula 1804001122:")
    encontrado = restaurante.buscar_cliente("1804001122")
    if encontrado:
        print("  " + str(encontrado))
    else:
        print("  No se encontro el cliente.")

    # mostrar resumen del dia
    restaurante.resumen_dia()


if __name__ == "__main__":
    main()
