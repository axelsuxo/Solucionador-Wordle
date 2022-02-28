from gettext import find
from operator import truediv
import string
#Nota 1: Todo se debe escribir con mayúsculas
lista=[]
lista2=[]
intentos=0
repborrar="si"
print("Bienvenido a wordle")
print("**Consejo: prueba primero con la palabra \"aireo\"")
palabra_secreta="aireo"
#archivo=open("palabras.txt","r")
archivo=open("diccionario.txt","r")
biblioteca=archivo.readlines()
for j in biblioteca:
    lista.append(j)
while(intentos<6):
    intentos=intentos+1
    palabra=input("Ingresa la palabra de 5 letras: ")
    contador=0
    if palabra not in lista:
        f = open ('diccionario.txt','a')
        #f = open ('palabras.txt','a')
        f.write("\n"+palabra)
        f.close()
    contador=contador+1
    #Borra las palabras que no contienen esas letras
    while True:
        borrar=input("Encontraste letras que no van en la palabra? ")
        if borrar=="SI":
            letraborrar=input("Escribe la letra: ")
            contador=0
            while contador<len(lista):
                if letraborrar in lista[contador]:
                    lista.pop(contador)
                    contador=contador-1
                contador=contador+1
        else:
            print(lista)
            break
    #Realiza un filtrado con palabras que contienen esas letras y la posición
    while True:
        movida=input("¿Hay alguna letra que exista y que este en una posición incorrecta? ")
        if movida=="SI":
            letra=str(input("Escribe la letra: "))
            posicion=int(input("Escribe la posición de la "+letra+" de la palabra "+palabra+": "))
            posicion=(posicion-1)
            contador=0
            while contador<len(lista):
                if letra not in lista[contador]:
                    lista.pop(contador)
                    contador=contador-1
                contador=contador+1
            contador=0
            while contador<len(lista):
                l=lista[contador]
                if letra in l[posicion]:
                    lista.pop(contador)
                    if contador>0:
                        contador=contador-1
                else:
                    contador=contador+1
        else:
            print(lista)
            break
    #Realiza un filtrado con la posicion de las letras correctas
    while True:
        print("¿Encontraste una letra en la pasición correcta? ")
        qposicion=input()
        if qposicion=="SI":
            aposicion=int(input("Ingresa la posición de la letra correcta de la palabra "+palabra +": "))
            aposicion=(aposicion-1)
            print(palabra[aposicion])
            letracorrecta=str(palabra[aposicion])
            print(aposicion)
            print(palabra)
            contador=0
            while contador<len(lista):
                l=lista[contador]
                if letracorrecta not in l[aposicion]:
                    lista.pop(contador)
                    if contador>0:
                        contador=contador-1
                else:
                    contador=contador+1
        else:
            print(lista)
            break