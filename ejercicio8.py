#resolver la ecuacion cuadratica: 2x**2-7x+3=0
a = 2
b = -7
c = 3

x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
print(x1)
print(x2)

#operaciones con cadenas de texto
print("SNPP" + "CTFPJ" + "PROGRAMACION PYTHON")
print("AULA" +str (2102)) 

#operaciones mixtas
print("tun chi " * 5)
print("Ja" * (2 ** 3))

#operadores de comparacion 
print(3 >4)
print(3 <4)
print(3 >=4)
print(4 <=4)
print(3 ==4)
print(3 !=4)

# operaciones con cadenas de texto
print("python" > "PYTHON")
print("aaaa" >= "abaa")
print(len("aaaa")>= len("abaa"))

print("python" != "PYTHON")

### operadores logicos

print(10 >4 and "Z" > "A")
print(10 >4 or "Z" > "A")
print(not(10 >4) and "Z" > "A")

### strings o de cadenas de texto

nombre = "tu nombre"
apellido = "apellido"

print(nombre + " " + apellido)
texto = "Este texto \n tiene salto de linea y \t tabulacion"
print(texto) 

#formateo
user, password, email= "moios",12345, "admin@admin.com"
print("su usuario y contraseña son {}{} y su email {}".format(user, password, email))
print("su usuario y contraseña son %s %d y su email %s" % (user, password, email))
print("su usuario y contraseña son " + user + " " + str(password) + "y su email " + email)
print(f"su usuario y contraseña son {user} {password} y email {email}")