"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import glob

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    input_folder = "files/input/"
    file = glob.glob(f"{input_folder}*")
    contador = {}

    with open(file[0], "r", encoding="utf-8") as f:
        for line in f:
            data = line.split("\t")
            if data[0] not in contador:
                contador[data[0]] = [int(data[1])]
            else:
                contador[data[0]].append(int(data[1]))

    rta = []
    for key, value in contador.items():
        rta.append((key, max(value), min(value)))
    rta.sort()

    return rta

if __name__ == "__main__":
    print(pregunta_05())
