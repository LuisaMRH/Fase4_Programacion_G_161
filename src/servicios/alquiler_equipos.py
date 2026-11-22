
"""
Servicio especializado para el alquiler de equipos.
"""

# ===========================================================================================
#                       LIBRERIAS
# ===========================================================================================

# Se importa la clase abstracta Servicio.
from .servicio import Servicio

# Se importan las excepciones.
from .excepciones import DatosServicioInvalidos


# ===========================================================================================
#                       CLASE ALQUILER DE EQUIPOS
# ===========================================================================================

class AlquilerEquipos(Servicio):

    # ---------------------------------------------------------------------------------------
    #       METODO CONSTRUCTOR
    # ---------------------------------------------------------------------------------------

    def __init__(self, codigo, nombre, descripcion,
                 tarifa_diaria, cantidad, dias):

        # Se inicializan los atributos generales heredados.
        super().__init__(codigo, nombre, descripcion, tarifa_diaria)

        # Se validan los datos especificos del alquiler.
        if cantidad <= 0 or dias <= 0:
            raise DatosServicioInvalidos(
                "La cantidad de equipos y los dias deben ser mayores que cero."
            )

        self.tarifa_diaria = tarifa_diaria
        self.cantidad = cantidad
        self.dias = dias

    # ---------------------------------------------------------------------------------------
    #       METODO PARA CALCULAR EL COSTO
    # ---------------------------------------------------------------------------------------

    def Calcular_Costo(self):

        costo_total = self.tarifa_diaria * self.cantidad * self.dias

        return costo_total

    # ---------------------------------------------------------------------------------------
    #       METODO PARA MOSTRAR LA INFORMACION
    # ---------------------------------------------------------------------------------------

    def Mostrar_Informacion(self):

        informacion = super().Mostrar_Informacion()

        informacion += (
            f"\nTarifa diaria: ${self.tarifa_diaria:,.2f}"
            f"\nCantidad de equipos: {self.cantidad}"
            f"\nDias de alquiler: {self.dias}"
        )

        return informacion
#holi