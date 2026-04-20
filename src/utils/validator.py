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

def option_validator(value, valid_options=None):
    if valid_options is None:
        valid_options = ["1", "2", "3", "4", "5"]
    option = value.strip()
    try:
        if option in valid_options:
            return option
        else:
            return option_validator(input(f"Digite una opción válida ({'/'.join(valid_options)}): "), valid_options)
    except ValueError:
        print ("\nOcurrió un error, intenta de nuevo.")
        return option_validator(input("Digite nuevamente la opción: "), valid_options)