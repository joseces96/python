calificaciones = [2,5,5,4.5,1]
nombres = ["moises","camila","fernanda","pablo","tania"]
lista_variada = ["true", 10.5, "abc", [0,1,1]]

print("estudiante: ", nombres[1])
print("calificacion: ", calificaciones[1])
print("lista dentro de otra: ", lista_variada[3][0])
print("imprimir un rango o slices ",nombres[1:2])
print(lista_variada)

#agregar elementos a una lista
nombres.append("jose")
print(nombres)
#remover elementos de una lista
nombres.remove("fernanda")
print(nombres)