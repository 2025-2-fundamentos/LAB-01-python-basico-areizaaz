"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import glob

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    input_folder = "files/input/"
    file = glob.glob(f"{input_folder}*")
    contador = {}

    with open(file[0], "r", encoding="utf-8") as f:
        for line in f:
            data = line.split("\t")
            _, mes, _ = data[2].split("-")
            if mes not in contador:
                contador[mes] = 1
            else:
                contador[mes] += 1

    rta = []
    for key, value in contador.items():
        rta.append((key, value))
    rta.sort()

    return rta

if __name__ == "__main__":
    print(pregunta_04())
