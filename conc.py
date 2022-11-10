#Variables globals integer
a = 2
b = 4

#Imprimir el resultat de la suma de les dues variables (int)
def sumanumero():
    print(a+b)

#Imprimir el resultat de la suma de les dues variables (int) dintre d'un text (string)
def sumanumstring():
    #Fiquem str a la suma per a que la passi a string i la pugui juntar a l'altre string
    print("El Roger m'ha dit que sumi "+str(a+b))

#Invoquem les dues funcions
sumanumero()
sumanumstring()