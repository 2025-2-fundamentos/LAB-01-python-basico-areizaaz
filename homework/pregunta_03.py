"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import glob

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    input_folder = "files/input/"
    file = glob.glob(f"{input_folder}*")
    contador = {}

    with open(file[0], "r", encoding="utf-8") as f:
        for line in f:
            data = line.split("\t")
            if data[0] not in contador:
                contador[data[0]] = int(data[1])
            else:
                contador[data[0]] += int(data[1])

    rta = []
    for key, value in contador.items():
        rta.append((key, value))
    rta.sort()

    return rta

if __name__ == "__main__":
    print(pregunta_03())
