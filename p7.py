
abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cifracesar(texto,key):
    
    resultado=""

    for letra in texto:
        
        nueva_posicion=(abecedario.index(letra)+key)
        if (nueva_posicion>26):
            nueva_posicion=nueva_posicion-26    
            nueva_posicion=nueva_posicion-1

        letra_cifrada=abecedario[nueva_posicion]
        resultado+=letra_cifrada

    return resultado

print("CIFRADOR CÉSAR")

texto=input("Escribe lo que quieras")
clave=int(input("Clave para cifrar (Número del 1 al 27):"))


cifrado=cifracesar(texto,clave)
print ("El texto cifrado es:",cifrado)