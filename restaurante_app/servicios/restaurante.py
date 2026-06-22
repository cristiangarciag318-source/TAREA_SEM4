# servicios/restaurante.py
# Módulo del servicio Restaurante.
# Es la clase principal del sistema. Se encarga de administrar
# la carta de productos y la lista de clientes con reserva.
# Tambien permite filtrar por turno y ver un resumen del dia.

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Administra los productos de la carta y los clientes con reserva."""

    def __init__(self, nombre, ciudad):
        self.nombre = nombre        # nombre del restaurante
        self.ciudad = ciudad        # ciudad donde se encuentra
        self.carta = []             # lista de objetos Producto
        self.reservas = []          # lista de objetos Cliente

    # gestion de la carta

    def agregar_producto(self, producto):
        """Agrega un producto a la carta del restaurante."""
        self.carta.append(producto)

    def mostrar_carta(self):
        """Imprime todos los productos de la carta."""
        print("\nCarta de " + self.nombre)
        print("-" * 50)
        if not self.carta:
            print("La carta esta vacia.")
        for p in self.carta:
            print("  " + str(p))
        print("-" * 50)

    def carta_por_turno(self, turno):
        """Muestra solo los productos del turno indicado."""
        print("\nProductos del turno " + turno + ":")
        encontrados = [p for p in self.carta if p.turno == turno and p.activo]
        if not encontrados:
            print("  No hay productos disponibles para ese turno.")
        for p in encontrados:
            print("  " + str(p))

    # gestion de reservas

    def agregar_cliente(self, cliente):
        """Registra un cliente con reserva en el sistema."""
        self.reservas.append(cliente)

    def mostrar_reservas(self):
        """Imprime la lista de clientes con reserva."""
        print("\nReservas en " + self.nombre)
        print("-" * 50)
        if not self.reservas:
            print("No hay reservas registradas.")
        for c in self.reservas:
            print("  " + str(c))
        print("-" * 50)

    def buscar_cliente(self, cedula):
        """Devuelve el cliente que tenga esa cedula, o None si no existe."""
        for c in self.reservas:
            if c.cedula == cedula:
                return c
        return None

    def total_comensales(self):
        """Suma el total de personas que vienen con reserva activa."""
        return sum(c.num_personas for c in self.reservas if c.con_reserva)

    def resumen_dia(self):
        """Imprime un resumen general del dia en el restaurante."""
        activos = sum(1 for p in self.carta if p.activo)
        con_reserva = sum(1 for c in self.reservas if c.con_reserva)
        print("\nResumen del dia - " + self.nombre + " (" + self.ciudad + ")")
        print("  Productos en carta    : " + str(len(self.carta)) +
              " (" + str(activos) + " disponibles)")
        print("  Reservas activas      : " + str(con_reserva))
        print("  Total de comensales   : " + str(self.total_comensales()) +
              " personas")

    def __str__(self):
        return "Restaurante " + self.nombre + " - " + self.ciudad
