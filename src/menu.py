from utils.console import clear, pause
from utils.validator import option_validator, number_validator
from modules.wallet import ServicioBilletera

billetera = ServicioBilletera()

def menu():
    print("=" * 60)
    print(("PERSONAL WALLET").center(60))
    print("=" * 60)
    print("  1. Ver saldo neto")
    print("  2. Ver historial")
    print("  3. Realizar una transacción")
    print("  4. Retirar dinero")
    print("  5. Salir")

def mostrar_saldo():
    saldo = billetera.consultar_saldo()
    print(f"\nSaldo actual: ${saldo:,.2f}\n")
    pause()
    clear()


def mostrar_historial():
    historial = billetera.consultar_historial()

    if not historial:
        print("\nNo hay transacciones registradas.\n")
    else:
        linea_separadora = "─" * 50
        print(f"\n{linea_separadora}")
        print(f"Historial de Movimientos ({len(historial)} registros)")
        print(f"{linea_separadora}")

        for transaccion in historial:
            print(transaccion.obtener_texto_para_mostrar())

        print(f"{linea_separadora}")
        print(f"Saldo actual: ${billetera.consultar_saldo():,.2f}")
        print(f"{linea_separadora}\n")

    pause()
    clear()


def realizar_transaccion():
    print("\nTipo de transacción:")
    print("1. Ingreso")
    print("2. Gasto")
    tipo_seleccionado = option_validator(input("Seleccione (1/2): "), ["1", "2"])

    es_ingreso = tipo_seleccionado == "1"
    monto = number_validator(input("Monto: "), "float")
    descripcion = input("Descripción: ").strip()

    if not descripcion:
        descripcion = "Ingreso" if es_ingreso else "Gasto"

    try:
        nueva_transaccion = billetera.registrar_transaccion(monto, descripcion, es_ingreso)
        icono = "📈" if es_ingreso else "📉"
        print(f"\n{icono} Transacción registrada exitosamente.")
        print(f"{nueva_transaccion.obtener_texto_para_mostrar()}")
    except ValueError as error:
        print(f"\nError: {error}")

    pause()
    clear()


def retirar_dinero():
    print(f"\nSaldo disponible: ${billetera.consultar_saldo():,.2f}")
    monto = number_validator(input("Monto a retirar: "), "float")

    try:
        transaccion_retiro = billetera.retirar_dinero(monto)
        print(f"\nRetiro exitoso.")
        print(f"{transaccion_retiro.obtener_texto_para_mostrar()}")
    except ValueError as error:
        print(f"\nError: {error}")

    pause()
    clear()

def run_menu():
    key = True
    while key:
        menu()
        try:
            option = option_validator(input("Digite una opción: "))
            match option:
                case "1":
                    clear()
                    mostrar_saldo()
                case "2":
                    clear()
                    mostrar_historial()
                case "3":
                    clear()
                    realizar_transaccion()
                case "4":
                    clear()
                    retirar_dinero()
                case "5":
                    key = False
        except KeyboardInterrupt:
            print("\nSaliendo del programa, gracias por usar Personal Wallet.")
            key = False