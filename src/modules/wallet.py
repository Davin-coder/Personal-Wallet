from models.transaction import Transaccion, TipoTransaccion
from repositories.wallet_repository import BilleteraRepositorio


class ServicioBilletera:
    def __init__(self, repositorio: BilleteraRepositorio = None):
        if repositorio is not None:
            self._repositorio = repositorio
        else:
            self._repositorio = BilleteraRepositorio()

    def consultar_saldo(self) -> float:
        return self._repositorio.calcular_saldo()

    def consultar_historial(self) -> list:
        transacciones = self._repositorio.obtener_todas_las_transacciones()
        transacciones_ordenadas = sorted(
            transacciones,
            key=lambda transaccion: transaccion.fecha_creacion,
            reverse=True
        )
        return transacciones_ordenadas

    def registrar_transaccion(self, monto: float, descripcion: str, es_ingreso: bool) -> Transaccion:
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a 0.")

        if es_ingreso:
            tipo_transaccion = TipoTransaccion.INGRESO
        else:
            tipo_transaccion = TipoTransaccion.GASTO

        if not es_ingreso:
            saldo_actual = self.consultar_saldo()
            if monto > saldo_actual:
                raise ValueError(
                    f"Saldo insuficiente. Saldo actual: ${saldo_actual:,.2f}"
                )
        nueva_transaccion = Transaccion(
            monto=monto,
            descripcion=descripcion,
            tipo=tipo_transaccion
        )
        self._repositorio.guardar_transaccion(nueva_transaccion)
        return nueva_transaccion

    def retirar_dinero(self, monto: float) -> Transaccion:
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0.")

        saldo_actual = self.consultar_saldo()
        if monto > saldo_actual:
            raise ValueError(
                f"Saldo insuficiente para retirar. Saldo actual: ${saldo_actual:,.2f}"
            )
        transaccion_retiro = Transaccion(
            monto=monto,
            descripcion="Retiro de fondos",
            tipo=TipoTransaccion.RETIRO
        )
        self._repositorio.guardar_transaccion(transaccion_retiro)
        return transaccion_retiro