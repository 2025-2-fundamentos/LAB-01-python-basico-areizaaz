"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import glob

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    input_folder = "files/input/"
    file = glob.glob(f"{input_folder}*")
    contador = {}

    with open(file[0], "r", encoding="utf-8") as f:
        for line in f:
            data = line.split("\t")
            diccionario = data[4].split(",")
            for cadena in diccionario:
                key, _ = cadena.split(":")
                if key not in contador:
                    contador[key] = 1
                else:
                    contador[key] += 1

    return contador

if __name__ == "__main__":
    print(pregunta_09())
