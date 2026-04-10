def number_validator(number, number_type):
    try:
        value = int(number) if number_type == "int" else float(number)
        if value <= 0:
            print("El número debe ser mayor a 0.")
            return number_validator(input("Ingresa el número de nuevo: "), number_type)
        else:
            return value
    except ValueError:
        print ("El valor no puede estar vacío y debe ser un numero válido.")
        return number_validator(input("\nIngresa el valor de nuevo: "), number_type)

def option_validator(value):
    option = value.strip()
    try:
        if option in ["1", "2", "3", "4", "5"]:
            return option
        else:
            return option_validator(input("Digite una opción válida (1-5): "))
    except ValueError:
        print ("\nOcurrió un error, intenta de nuevo.")
        return option_validator(input("Digite nuevamente la opción: "))