def intercalar_mayus_minus(cadena):
    resultado = ""
    mayusculas = True

    for char in cadena:
        if char.isalpha():
            if mayusculas:
                resultado += char.upper()
            else:
                resultado += char.lower()
            mayusculas = not mayusculas
        else:
            resultado += char

    return resultado


cadena_original = input("Ingresa una cadena: ")
cadena_transformada = intercalar_mayus_minus(cadena_original)
print("Cadena transformada:", cadena_transformada)
