# Funcion Diners
def invers2():
    savings = 100 # Diners inicials 100
    increase = 1.1 # Cada any s'incrementa 1.1

    result = savings # Guardar el valor inicial en una variable result
    # Recorrer els 7 anys e ir multiplicant el valor inicial * el increment 7 vegades
    for i in range(7):
        result*= increase
    # Imprimir els diners acumulats (Hacer un str en el numero para combinar un string con un int)
    print("Diners acumulats despres de 7 anys: " + str(result))

invers2() # Llamar a la funcion