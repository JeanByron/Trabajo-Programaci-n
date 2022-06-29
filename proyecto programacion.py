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

def grafica(materias,notas):    
    #Se define el largo utilizando numpy y la funcion (arange) con la longitud del numero de materias
    largo=np.arange(len(materias))
    
    ancho=0.30

    #Definicion del lugar donde se dibujara la grafica y un objeto desde el que se llamaran las funciones
    #(subplots) se utiliza para abrir la posibilidad de usar barras sobre otras barras
    fig, ax=plt.subplots()

    ax.bar(largo,notas,ancho)
    ax.set_title("Grafica de materias")
    ax.set_ylabel("Notas")
    ax.set_xticks(largo)
    ax.set_xticklabels(materias)
    

lista, lista_materias, lista_notas_estudiantes = registro_estudiantes()
lista, lista_materias, lista_notas_estudiantes = mas_asignaturas(lista, lista_materias, lista_notas_estudiantes)

for i in lista_notas_estudiantes:
    lista_notas = i.get("notas")
    print(lista_notas)
    
print(lista_materias,"\n")

def menu_ensenar_reporte(nombre_estudiante, lista_notas_estudiantes, lista_materias):
    pregunta=int(input("Desea ver el reporte general? (1) o un reporte en específico? (2), ó la gráfica? (3): "))
    if pregunta==1:
        leer_reporte=pd.read_excel(f"{nombre_estudiante}.xlsx", index_col=False)
        return leer_reporte
    elif pregunta==2:
        pregunta_materia=input("Ingrese el nombre de la materia que desea consultar: ")
        leer_reporte = pd.read_excel(f"{nombre_estudiante}.xlsx")
        leer_materia = leer_reporte.loc[:,f"{pregunta_materia}"]
        return leer_materia
    elif pregunta == 3:
        for notas in lista_notas_estudiantes:
            if notas.get("Nombre") == nombre_estudiante:
                notas_estudiante = notas.get("notas")
                grafica(lista_materias, notas_estudiante)

nombre_estudiante = input("Ingrese el nombre: ")
(menu_ensenar_reporte(nombre_estudiante, lista_notas_estudiantes, lista_materias))
plt.show()


