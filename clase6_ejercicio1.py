import os
resp = 1
while resp != 0:
    print("paint (1)")
    print("calc (2)")
    print("Apagar PC en 2 hora (3)")
    print("microsoft edge (4)")
    print("Gran Espiritu - Armin (5)")
    print("Salir(0)")
    resp = int(input("seleccione: "))
    if(resp == 1):
        os.system("Mspaint")
    elif(resp == 2):
        os.system("calc")
    elif(resp == 3):
        os.system("shutdown -s -t 7200") 
    elif(resp == 4):
        os.system("start msedge www.facebook.com")
    elif(resp == 5):
        os.system("start msedge www.youtube.com/watch?v=yo4pmauhugo")
    else:
        print("No entiendo esa orden")
