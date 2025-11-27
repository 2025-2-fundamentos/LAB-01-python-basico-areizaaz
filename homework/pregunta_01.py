"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import glob

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    input_folder = "files/input/"
    file = glob.glob(f"{input_folder}*")
    suma = 0
    with open(file[0], "r", encoding="utf-8") as f:
        for line in f:
            data = line.split("\t")
            suma += int(data[1])

    return suma

if __name__ == "__main__":
    print(pregunta_01())
