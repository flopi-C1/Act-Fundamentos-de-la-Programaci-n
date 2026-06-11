contactos = {
 "Nombre" : input ("Ingrese un nombre: "),
 "Telefono" : input("Ingrese n° de contacto: "),
 "Email" : input ("Ingrese correo / email: "),
 "Edad" : input ("Ingrese la edad: ")
}


while True:
    print ("**** LISTA DE CONTACTOS ***") 

    print ("[1] - Ver ficha")
    print ("[2] - Editar dato")
    print ("[3] - Salir")

    opc = int(input("Ingrese una opción (1 - 2 - 3)"))
    if opc == 1:
        print ("Nombre: ", contactos["Nombre"])
        print ("Telefono: ", contactos["Telefono"])
        print ("Email:", contactos["Email"])
        print ("Edad: ",contactos["Edad"])
    
    elif opc == 2:
        editar = input ("Ingrese el dato que desea editar (Nombre - Telefono - Email - Edad)")
        contacto [editar] = input ("Ingrese nuevo dato para ", editar)     
    
    elif opc == 3:
        ("Saliendo del sistema")
    break    
