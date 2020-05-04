abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("CIFRADOR CÉSAR")

texto=input("Escribe lo que quieras:")
clave=int(input("Clave para cifrar (Número del 1 al 27):"))


resultado=""

for letra in texto:
    nueva_posicion=(abecedario.index(letra)+clave) % 27
    letra_cifrada=abecedario[nueva_posicion]
    resultado+=letra_cifrada

print(resultado)
