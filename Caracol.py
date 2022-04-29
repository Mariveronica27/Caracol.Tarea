Bandera=True

while(Bandera):

    Hdepozo = input("Ingrese Hdepozo: ")
    Hdepozo = float(Hdepozo)
    
    Ld = input("Ingrese Ld: ")
    Ld = float(Ld)
    
    Ln = input("Ingrese Ln: ")
    Ln = float(Ln)

    operacion = float((Hdepozo) / (Ld - Ln))
    

    while Ld > Ln:
         print("El caracol tardo en salir del pozo(dias): " + str (round(operacion, 4)))
         Bandera=False
         break


    if Ld < Ln:
        print("El caracol se murio. Porfavor ingrese valores donde el caracol sobreviva")
        Bandera=True



