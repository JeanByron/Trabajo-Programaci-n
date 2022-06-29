import pandas as pd
def menu_enseñar_reporte(nombre_estudiante):
    pregunta=int(input("Desea ver el reporte general? (1) o un reporte en específico? (2): "))
    if pregunta==1:
        leer_reporte=pd.read_excel(f"{nombre_estudiante}")
        print(leer_reporte)
    elif pregunta==2:
        pregunta_materia=str(input("Ingrese el nombre de la materia que desea consultar: "))
        leer_reporte=pd.read_excel(f"{nombre_estudiante}")
        leer_materia=leer_reporte.loc[:,f"{pregunta_materia}"]
        print(leer_materia)