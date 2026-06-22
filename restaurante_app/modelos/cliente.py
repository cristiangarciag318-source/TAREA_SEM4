# modelos/cliente.py
# Módulo del modelo Cliente.
# Representa a una persona que hace una reserva o llega
# directamente al restaurante. Almacena sus datos y
# la información de su reserva.


class Cliente:
    """Persona que realiza una reserva en el restaurante."""

    def __init__(self, cedula, nombre, telefono, num_personas):
        self.cedula = cedula                # número de cédula
        self.nombre = nombre                # nombre completo
        self.telefono = telefono            # contacto telefónico
        self.num_personas = num_personas    # personas que vienen con él
        self.con_reserva = True             # indica si tiene reserva activa

    def cancelar_reserva(self):
        """Cancela la reserva del cliente."""
        self.con_reserva = False

    def actualizar_personas(self, cantidad):
        """Modifica el número de personas de la reserva."""
        self.num_personas = cantidad

    def __str__(self):
        reserva = "con reserva" if self.con_reserva else "sin reserva"
        return (f"{self.cedula} | {self.nombre} | Tel: {self.telefono} "
                f"| Personas: {self.num_personas} | {reserva}")
