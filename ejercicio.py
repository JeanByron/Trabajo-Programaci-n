def registro ():
    nombre=input("ingrese su nombre: ")
    usuario=input("ingrese el nombre de usuario que desea: ")
    ciudad=input("ingrese su ciudad: ")
    doc_identidad=input("ingrese su documento de identidad: ")
    genero=input("ingrese el genero con el que se identifica: ")
    clave=input("ingrese la clave que desea: ")
    print("\n")
    listado_usuarios = {'nombre':nombre ,'usuario':usuario ,'ciudad':ciudad ,'doc_identidad':doc_identidad ,'genero':genero ,'clave':clave}





def login ():
    while True:
        nombre_usuario=input("ingrese su nombre de usuario: ")
        contrasenia=input("ingrese su clave: ")
        if (nombre_usuario in usuario):
            if (contrasenia in clave):
                print("bienvendio señor/señora" ,listado_usuarios['nombre'], "al sistema de calificacion")
                break
            else:
                print("usuario o clave incorrectos")
        else:
            print("usuario o clave incorrectos")

def menu():
    while True:
            opcionMenu = input("bienvenido a la plataforma de calificaion e informes creada por el grupo de fundamentos de programacio. \n ingrese una de las opciones, donde: \n 1. es para ingresar como docente. \n 2.para ingresar como estudiante. \n 3. para crear un usuario de docente. \n 0. para salir por completo del sistema.")
            if opcionMenu=="1":  
                    print ("")
                    input("usted esta solicitando el ingreso al modulo de docentes...\npulsa una tecla para continuar \n")
                    
            elif opcionMenu=="2":
                    print ("")
                    input("ingreso al modulo de estudiantes...\npulsa una tecla para continuar \n")
            elif opcionMenu=="3":
                    print ("")
                    input("ingreso a la opcion de registro...\npulsa una tecla para continuar \n")
            elif opcionMenu=="0":
                    break
            else:
                    print ("")
                    input("No se ha pulsado ninguna opción correcta...\npulsa una tecla para volver a intentar. \n")


