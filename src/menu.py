from utils.console import clear

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
            option = input("Seleccione una opción: ")
            if option == "1":
                pass
            elif option == "2":
                pass
            elif option == "3":
                pass
            elif option == "4":
                pass
            elif option == "5":
                key = False
            else:
                clear()
                print("¡Opción inválida!")
        except KeyboardInterrupt:
            print("\nSaliendo del programa.")
            key = False