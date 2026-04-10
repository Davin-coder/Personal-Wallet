def number_validator(number, number_type):
    try:
        value = int(number) if number_type == "int" else float(number)
        if converted_value <= 0:
            print("El número debe ser mayor a 0.")
            return validate_number(input("Ingresa el número de nuevo: "), type_number)
        else:
            return converted_value
    except ValueError as Error:
        print ("\nOcurrió un error, intenta de nuevo.")
        return validate_number(input("Ingresa el valor de nuevo: "), type_number)

def option_validator(value):
    option = value.strip()
    try:
        if option in ["1", "2", "3", "4", "5"]:
            return option
        else:
            return option_validator(input("Digite una opción válida (1-5): "))
    except ValueError as error:
        print ("\nOcurrió un error, intenta de nuevo.")
        return option_validator(input("Digite nuevamente la opción: "))