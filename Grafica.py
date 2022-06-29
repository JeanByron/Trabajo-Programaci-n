import numpy as np
import matplotlib.pyplot as plt

materias=["Calculo","Programacion","Ingles"]
calificaciones=[3,4,4]

largo=np.arange(len(materias))
ancho=0.30

fig, ax=plt.subplots()
ax.bar(largo,calificaciones,ancho)
ax.set_title("Grafica de materias")
ax.set_ylabel("Notas")
ax.set_xticks(largo)
ax.set_xticklabels(materias)
