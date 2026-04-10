from utils.console import clear
from utils.validator import option_validator

def menu():
    print("=" * 60)
    print(("PERSONAL WALLET").center(60))
    print("=" * 60)
    print("  1. Ver saldo neto")
    print("  2. Ver historial")
    print("  3. Realizar una transacción")
    print("  4. Retirar dinero")
    print("  5. Salir")

def run_menu():
    key = True
    while key:
        menu()
        try:
            option = option_validator(input("Digite una opción: "))
            match option:
                case "1":
                    clear()
                    print("1")
                case "2":
                    clear()
                    print("2")
                case "3":
                    clear()
                    print("3")
                case "4":
                    clear()
                    print("4")
                case "5":
                    key = False
        except KeyboardInterrupt:
            print("\nSaliendo del programa, gracias por usar Personal Wallet.")
            key = False