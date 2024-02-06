def cargar_lista():
    valor = input("ingrese un valor")
    lista.append(valor)

def imprimir_lista():
    for x in range(len(lista)):
        print(f"{lista[x]}", end=" | ")

lista = []
cargar_lista()
cargar_lista()
cargar_lista()
imprimir_lista()


