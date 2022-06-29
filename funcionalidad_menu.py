import pandas as pd
from pandas import ExcelWritere
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





        
        
        