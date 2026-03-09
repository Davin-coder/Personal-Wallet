def number_validator(number, number_type):
    try:
        value = int(number) if number_type == "int" else float(number)
        if converted_value <= 0:
            print("El número debe ser mayor a 0.")
            return validate_number(input("Ingresa el número de nuevo: "), type_number)
        else:
            return converted_value
    except ValueError as Error:
        print ("Ocurrió un error, intenta de nuevo.")
        return validate_number(input("Ingresa el valor de nuevo: "), type_number)
    except KeyboardInterrupt:
        print("\nSaliendo del programa.")