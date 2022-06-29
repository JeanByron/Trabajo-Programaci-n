import pandas as pd
from pandas import ExcelWriter
import numpy as np
import matplotlib.pyplot as plt


def registro_estudiantes():
    lista_materias = []
    nombre_asignatura = input("Ingrese el nombre de la asignatura:")
    lista_materias.append(nombre_asignatura)
    ingresar_estudiante = int(input("Digite 1 para agregar estudiantes:"))
    lista = []
    lista_notas_estudiantes = []
    while ingresar_estudiante == 1:
        estudiante = input("Ingrese el nombre del estudiante: ")
        cedula = input("Ingrese la cédula del estudiante: ")
        nota = float(input("Ingrese la nota: "))
        datos = {"Nombre" : [estudiante],
                 "cédula" : [cedula],
                nombre_asignatura : [nota]}
        
        notas = { "Nombre" : [estudiante],
                 "notas": [nota] }
        
        lista.append(datos)
        lista_notas_estudiantes.append(notas)
        data_null = {}
        df_null = pd.DataFrame(data_null)
        df_null.to_excel(f"{estudiante}.xlsx", index=False)
        writer = pd.ExcelWriter(f"{estudiante}.xlsx")
        df1 = pd.DataFrame(datos)
        df1.to_excel(writer, "Estudiante", index=False)
        writer.save()
        writer.close()
        ingresar_estudiante = int(input("Digite 1 si quiere agregar más estudiantes u otro número si quiere salir: "))
    print("Se salió de la sección REGISTRO DE NOTAS")
    return lista, lista_materias, lista_notas_estudiantes



def mas_asignaturas(lista, lista_materias, lista_notas_estudiantes):
    nombre_asignatura = input("Ingrese el nombre de la asignatura:")
    lista_materias.append(nombre_asignatura)
    ingresar_estudiante = int(input("Digite 1 para agregar estudiantes:"))
    i = 1
    while ingresar_estudiante == 1:
        estudiante = input("Ingrese el nombre del estudiante: ")
        cedula = input("Ingrese la cédula del estudiante: ")
        nota = float(input("Ingrese la nota: "))
        writer = pd.ExcelWriter(f"{estudiante}.xlsx")
        for datos in lista:
            if datos.get("Nombre") == [estudiante]:
                datos[nombre_asignatura] = [nota]
                df1 = pd.DataFrame(datos)
                df1.to_excel(writer, "Estudiante1", index=False)
                writer.save()
                writer.close()
        for notas in lista_notas_estudiantes:
            if notas.get("Nombre") == [estudiante]:
                total_notas = notas.get("notas")
                total_notas.append(nota)            
        ingresar_estudiante = int(input("Digite 1 para agregar estudiantes o 2 para salir:"))
        i += 1
    return lista, lista_materias, lista_notas_estudiantes



def grafica(num_materias,calificaciones,materias):
    for i in range(num_materias):
        def_materias=str(input(f"Ingresa la materia numero {i+1}: "))
        materias.append(def_materias)
        def_calificaciones=int(input(f"Ingrese la calificacion de la materia numero {i+1}: "))
        calificaciones.append(def_calificaciones)
        
    largo=np.arange(len(materias))
    ancho=0.30
    fig, ax=plt.subplots()
    ax.bar(largo,calificaciones,ancho)
    ax.set_title("Grafica de materias")
    ax.set_ylabel("Notas")
    ax.set_xticks(largo)
    ax.set_xticklabels(materias)

def menu_ensenar_reporte(nombre_estudiante, lista_notas_estudiantes, lista_materias):
    pregunta=int(input("Desea ver el reporte general? (1) o un reporte en específico? (2), ó quiere generar una gráfica? (3): "))
    if pregunta==1:
        leer_reporte=pd.read_excel(f"{nombre_estudiante}.xlsx", index_col=False)
        return leer_reporte
    elif pregunta==2:
        pregunta_materia=input("Ingrese el nombre de la materia que desea consultar: ")
        leer_reporte = pd.read_excel(f"{nombre_estudiante}.xlsx")
        leer_materia = leer_reporte.loc[:,f"{pregunta_materia}"]
        return leer_materia
    elif pregunta == 3:
        num_materias=int(input("Ingrese el numero de materias que desea registrar: "))
        calificaciones = []
        materias = []
        grafica(num_materias,calificaciones,materias)
        plt.show()
        
        

def registro ():
    nombre=input("ingrese su nombre: ")
    usuario=input("ingrese el nombre de usuario que desea: ")
    ciudad=input("ingrese su ciudad: ")
    doc_identidad=input("ingrese su documento de identidad: ")
    genero=input("ingrese el genero con el que se identifica: ")
    clave=input("ingrese la clave que desea: ")
    print("\n")
    listado_usuarios = {'nombre':nombre ,'usuario':usuario ,'ciudad':ciudad ,'doc_identidad':doc_identidad ,'genero':genero ,'clave':clave}
    return listado_usuarios

def login (listado_usuarios):
    while True:
        nombre_usuario=input("ingrese su nombre de usuario: ")
        contrasenia=input("ingrese su clave: ")
        if (listado_usuarios.get("usuario")== nombre_usuario):
            if (listado_usuarios.get("clave") == contrasenia):
                print("bienvendio señor/señora" ,listado_usuarios['nombre'], "al sistema de calificacion")
                break
            else:
                print("usuario o clave incorrectos")
        else:
            print("usuario o clave incorrectos")
            
def menu():
    while True:
        opcionMenu = input("Bienvenido a la plataforma de calificacion e informes creada por el grupo de fundamentos de programación. \n Nota: Si no está registrado, primero hágalo o de lo contrario lanzará un error. \n Ingrese una de las opciones, donde: \n 1. es para ingresar como docente. \n 2.para ingresar como estudiante. \n 3. para crear un usuario de docente. \n 0. para salir por completo del sistema.\n Ingrese una opción: ")
        if opcionMenu=="1":
            print ("usted esta solicitando el ingreso al modulo de docentes")
            login(listado_usuarios)
            mas_asignaturas(lista, lista_materias, lista_notas_estudiantes)
            input("\npulsa una tecla para continuar")
            
        elif opcionMenu=="2":
            print ("ingresó al módulo de estudiantes")
            nombre_estudiante = input("Ingrese su nombre: ")
            print(menu_ensenar_reporte(nombre_estudiante, lista_notas_estudiantes, lista_materias))
            input("\n pulse espacio para continuar: ")
            
        elif opcionMenu=="3":
            print ("Ingresó a la opción de registro")
            listado_usuarios = registro()
            input("\npulsa una tecla para continuar")
            
        elif opcionMenu=="0":
            break
        else:
            print ("")
            input("No se ha pulsado ninguna opción correcta...\npulsa una tecla para volver a intentar.")


for i in range(2):
    opcionMenu = input("Bienvenido a la plataforma de calificacion e informes creada por el grupo de fundamentos de programación. \n Nota: Si no está registrado, primero hágalo o de lo contrario lanzará un error. \n Ingrese una de las opciones, donde: \n 1. es para ingresar como docente. \n 2.para ingresar como estudiante. \n 3. para crear un usuario de docente. \n 0. para salir por completo del sistema.\n Ingrese una opción: ")
    if opcionMenu=="3":
        print ("")
        print("Usted está solicitando registrarse")
        listado_usuarios = registro()
    
    elif opcionMenu=="1":
        print ("Usted esta solicitando el ingreso al modulo de docentes")
        login(listado_usuarios)
        lista, lista_materias, lista_notas_estudiantes = registro_estudiantes()

menu()
    
