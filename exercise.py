lista_personas = [
    ('11111111', 'Pedro', 'Paez', 24),
    ('22222222', 'Fito', 'Garcia', 23),
    ('33333333', 'Leo', 'Peralta', 26),
    ('44444444', 'Bruno', 'Mac', 25),
    ('55555555', 'Nico', 'Zaoral', 27),
    ('44444444', 'Bruno', 'Mac', 25),
]


def ordenar(lista_personas):
    """ El metodo debe devolver una lista con las edades ordenadas de menor a mayor"""
    
    # Completar
    edades = [] # Lista vacía que contendra las edades a retornar 
    for i in lista_personas:
        edades.append(i[3])
    edades.sort() # El metodo sort ordena la lista de menor a mayor
    return edades
# tambien se podria haber usado el metodo sorted() que devuelve una lista ordenada sin modificar la original y con lambdas se puede hacer de manera mas eficiente
# lista_ordenada = sorted(lista_personas, key=lambda x: x[3])

def convertir_a_diccionario(lista_personas):
    """ Hacer un diccionario que tenga como claves los “dni” y como valores tuplas con nombre, apellido y edad """
    # Completar
    dic = {}
    for i in lista_personas:
        dic[i[0]] = (i[1], i[2], i[3])
    return dic
    


def devolver_edad(lista_personas, dni):
    """ Para la 'lista_personas' devuelve la edad de la persona que tenga el dni definido.
    Tip: intentar usar el método convertir_a_diccionario"""
    # Completar
    dic = convertir_a_diccionario(lista_personas)
    return dic[dni][2] # Se accede a la edad de la persona con el dni pasado por parametro en el diccionario creado en el metodo anterior
    


def eliminar_repetidos(lista_personas):
    """ El metodo debe devolver los elementos unicos """
    # Completar
    return list(set(lista_personas)) # Se convierte la lista en un set para eliminar los elementos repetidos y luego se vuelve a convertir en lista

    


def separar_por_edad(lista_personas):
    """ Devolver dos listas
    * lista 1: mayores de 25 (incluido)
    * lista 2: menores de 25
    """
    # Completar
    mayores = []
    menores = []
    for i in lista_personas:
        if i[3] >= 25:
            mayores.append(i)
        else:
            menores.append(i)

    return mayores, menores
# tambien se podria haber usado list comprehension para hacerlo de manera mas eficiente
#   mayores = [persona for persona in lista_personas if persona[3] >= 25]
    # menores = [persona for persona in lista_personas if persona[3] < 25]
    # return mayores, menores

def obtener_promedio(lista):
    """ Implementar obtener el promedio de la lista de números que se recibe.
    Capturar con un try/except la excepción de dividir por cero"""
    # Completar
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        return 0
    
    


def main():
    """ Este metodo no debe modificarse y es solo a fines de probar el codigo """
    print('Resultados:\n')
    print(' * Edades ordenadas: %s\n' % ordenar(lista_personas))
    print(' * Elementos como diccionario: %s\n' % convertir_a_diccionario(lista_personas))
    print(' * La edad para dni 55555555 es: %s\n' % devolver_edad(lista_personas, '55555555'))
    print(' * Elementos únicos: %s\n' % eliminar_repetidos(lista_personas))
    print(' * Los mayores de 25 son: %s\n' % separar_por_edad(lista_personas)[0])
    print(' * Los menores de 25 son: %s\n' % separar_por_edad(lista_personas)[1])
    print(' * El promedio de las edades es: %s\n' % obtener_promedio(ordenar(lista_personas)))
    print(' * El promedio de una lista vacía es: %s\n' % obtener_promedio([]))


if __name__ == '__main__':
    main()