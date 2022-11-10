def names():
    #Array
    areas = ['cuina', 7.88, 'menjador', 13.0, 'terrassa', 20.34, 'lavabo', 6.55, 'habitació1', 7.98, 'habitació2', 12, 'rebedor', 4.23]

    cocina = areas[0]
    suma = areas[9] + areas[11]
    #Creando la Funcion para cambiar el Nombre
    def canvinom():
        canviarea = areas
        canviarea[6] = 'area'
        print(canviarea)
    #Creando y usando append, para agregar un nuevo valor
    def añadirName():
        variable = areas
        variable.append('pati interior')
        variable.append(6.78)
        print(variable)

    #Prints
    print(areas[2])
    print(areas[13])
    print(areas[5])
    print(areas[0:3])
    print(areas[3:])
    print(suma)
    canvinom()
    añadirName()
    #Afegir l’area de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
#Llamos al objeto
names()