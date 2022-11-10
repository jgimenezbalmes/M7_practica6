#Funcio que agafa dues variables...
def sumainputs(x,y):
    #Passem les variables a str per a sumar-les a la resta de la frase.
    #Per a la suma, passem cada valor a int per a poder fer una suma bé, i després passem el resultat a str
    print("La suma del valor "+str(x)+" més el valor "+str(y)+" serà: "+str(x)+"+"+str(y)+"="+str(int(x)+int(y))+".")