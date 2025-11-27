"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import glob

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    input_folder = "files/input/"
    file = glob.glob(f"{input_folder}*")
    rta = []

    with open(file[0], "r", encoding="utf-8") as f:
        for line in f:
            data = line.split("\t")
            rta.append((data[0], len(data[3].split(",")), len(data[4].split(","))))

    return rta

if __name__ == "__main__":
    print(pregunta_10())
