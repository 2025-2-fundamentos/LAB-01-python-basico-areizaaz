"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import glob

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    input_folder = "files/input/"
    file = glob.glob(f"{input_folder}*")
    contador = {}

    with open(file[0], "r", encoding="utf-8") as f:
        for line in f:
            data = line.split("\t")
            diccionario = data[4].split(",")
            for cadena in diccionario:
                key, value = cadena.split(":")
                if key not in contador:
                    contador[key] = [int(value)]
                else:
                    contador[key].append(int(value))

    rta = []
    for key, value in contador.items():
        rta.append((key, min(value), max(value)))
    rta.sort()

    return rta

if __name__ == "__main__":
    print(pregunta_06())
