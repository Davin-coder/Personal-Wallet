from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import uuid


class TipoTransaccion(Enum):
    INGRESO = "ingreso"
    GASTO = "gasto"
    RETIRO = "retiro"


@dataclass
class Transaccion:
    monto: float
    descripcion: str
    tipo: TipoTransaccion
    identificador: str = field(default_factory=lambda: str(uuid.uuid4()))
    fecha_creacion: str = field(default_factory=lambda: datetime.now().isoformat())

    def convertir_a_diccionario(self) -> dict:
        return {
            "identificador": self.identificador,
            "monto": self.monto,
            "descripcion": self.descripcion,
            "tipo": self.tipo.value,
            "fecha_creacion": self.fecha_creacion,
        }
    
    @classmethod
    def extraer_desde_diccionario(cls, datos: dict) -> "Transaccion":
        return cls(
            identificador = datos["identificador"],
            monto = datos["monto"],
            descripcion = datos["descripcion"],
            tipo = TipoTransaccion(datos["tipo"]),
            fecha_creacion = datos["fecha_creacion"]
        )
    
    def obtener_texto_para_mostrar(self) -> str:
        simbolo = "+" if self.tipo == TipoTransaccion.INGRESO else "-"
        fecha_corta = self.fecha_creacion[:10]
        
        return f"  {fecha_corta}  {simbolo}${self.monto:,.2f}  —  {self.descripcion}"
