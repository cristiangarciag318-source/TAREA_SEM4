# modelos/producto.py
# Módulo del modelo Producto.
# Representa un plato o bebida que el restaurante ofrece
# en su carta. Guarda el nombre, el turno en que se sirve,
# el precio y si todavía está disponible ese día.


class Producto:
    """Un plato o bebida que forma parte de la carta del restaurante."""

    def __init__(self, codigo, nombre, turno, precio):
        self.codigo = codigo        # identificador del producto
        self.nombre = nombre        # nombre del plato o bebida
        self.turno = turno          # turno: Desayuno, Almuerzo o Cena
        self.precio = precio        # precio en dólares
        self.activo = True          # True mientras esté disponible

    def desactivar(self):
        """Marca el producto como no disponible para ese día."""
        self.activo = False

    def activar(self):
        """Vuelve a poner el producto como disponible."""
        self.activo = True

    def actualizar_precio(self, nuevo_precio):
        """Cambia el precio del producto."""
        self.precio = nuevo_precio

    def __str__(self):
        estado = "disponible" if self.activo else "no disponible"
        return (f"{self.codigo} | {self.nombre} | {self.turno} "
                f"| ${self.precio:.2f} | {estado}")
