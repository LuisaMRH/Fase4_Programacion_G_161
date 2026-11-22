
"""
Servicios especializados ofrecidos por Software FJ.
"""
#123
# ===========================================================================================
#                       IMPORTACION DE CLASES
# ===========================================================================================

# Se importa la clase abstracta principal.
from .servicio import Servicio

# Se importan los servicios especializados.
from .alquiler_equipos import AlquilerEquipos
from .asesoria import Asesoria
from .reserva_salas import ReservaSalas

# Se importa la interfaz grafica.
from .interfaz import InterfazServicios

# Se importan las excepciones.
from .excepciones import (
    ErrorServicio,
    DatosServicioInvalidos,
    CostoServicioInvalido,
    ServicioIncompleto
)

# ===========================================================================================
#                       ELEMENTOS PUBLICOS DEL PAQUETE
# ===========================================================================================

__all__ = [
    "Servicio",
    "AlquilerEquipos",
    "Asesoria",
    "ReservaSalas",
    "InterfazServicios",
    "ErrorServicio",
    "DatosServicioInvalidos",
    "CostoServicioInvalido",
    "ServicioIncompleto"
]
