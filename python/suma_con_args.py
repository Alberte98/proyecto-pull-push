def suma_con_args(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado


numeros = [1, 2, 3, 4, 5]
total = suma_con_args(*numeros)
print("La suma es:", total)
