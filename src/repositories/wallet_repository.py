import json
import os
from models.transaction import Transaccion


class BilleteraRepositorio:
    def __init__(self, ruta_archivo: str = None):
        if ruta_archivo is None:
            directorio_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self._ruta_archivo = os.path.join(directorio_base, "data", "wallet.json")
        else:
            self._ruta_archivo = ruta_archivo
        self._asegurar_que_archivo_existe()
    
    def obtener_todas_las_transacciones(self) -> list:
        datos = self._leer_archivo()
        lista_de_transacciones = []
        
        for datos_transaccion in datos["transacciones"]:
            transaccion = Transaccion.extraer_desde_diccionario(datos_transaccion)
            lista_de_transacciones.append(transaccion)
        return lista_de_transacciones
    
    def guardar_transaccion(self, transaccion: Transaccion) -> None:
        datos = self._leer_archivo()
        datos["transacciones"].append(transaccion.convertir_a_diccionario())
        self._escribir_archivo(datos)
    
    def calcular_saldo(self) -> float:
        transacciones = self.obtener_todas_las_transacciones()
        saldo = 0.0
        
        for transaccion in transacciones:
            if transaccion.tipo.value == "ingreso":
                saldo += transaccion.monto
            else:
                saldo -= transaccion.monto
        return saldo
    
    def eliminar_todas_las_transacciones(self) -> None:
        self._escribir_archivo(self._estructura_inicial())
    
    def _asegurar_que_archivo_existe(self) -> None:
        directorio = os.path.dirname(self._ruta_archivo)
        
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        
        if not os.path.exists(self._ruta_archivo):
            self._escribir_archivo(self._estructura_inicial())
    
    def _leer_archivo(self) -> dict:
        try:
            with open(self._ruta_archivo, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (json.JSONDecodeError, FileNotFoundError):
            datos_por_defecto = self._estructura_inicial()
            self._escribir_archivo(datos_por_defecto)
            return datos_por_defecto
    
    def _escribir_archivo(self, datos: dict) -> None:
        with open(self._ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=2, ensure_ascii=False)
    
    @staticmethod
    def _estructura_inicial() -> dict:
        return {
            "transacciones": []
        }