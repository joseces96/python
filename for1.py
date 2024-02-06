promedio_general = 0
total = 0
cantidad = 0
calificacion = 1
while(calificacion !=0):
    #se permite solamente del 1 al 5
    #while...if
    calificacion = int(input("Ing calif: "))
    total += calificacion
    cantidad+=1

#restamos 1a cantidad por el exceso de calif = 0
cantidad-=1

promedio_general = total / cantidad
print(f"el promedio general es{promedio_general}")

