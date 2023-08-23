def suma_con_kwargs(**kwargs):
    resultado = 0
    for key, value in kwargs.items():
        resultado += value
    return resultado


'''
NOTA acerca de **kwargs

En **kwargs, se recibe un número indeterminado de argumentos desde cualquier 
variable de dict
'''

valores = {'a': 10, 'b': 20, 'c': 30}
total = suma_con_kwargs(**valores)
print("La suma es:", total)
