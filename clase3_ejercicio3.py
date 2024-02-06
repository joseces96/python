#mayor/menor
valor1= int(input("ingrese un entero"))
valor2= int(input("ingrese otro entero"))

if(valor1 > valor2)
    print("El mayor es: ",valor1)
    
    if(valor1 % 2 == 0)
        print("El numero es PAR")
    else:
        print("El numero es IMPAR")
elif(valor1 < valor2)
    print("El mayor es: ",valor1)
    
    if(valor2 % 2 == 0)
        print("El numero es PAR")
    else:
        print("El numero es IMPAR")   
else:
    print("los numeros son iguales")