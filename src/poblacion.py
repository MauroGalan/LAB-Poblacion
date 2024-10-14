from collections import namedtuple
import csv
from matplotlib import pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')
Tuplapais = namedtuple("Tuplapaís", "pais, censo")
Tuplaaño = namedtuple("Tuplaaño", "pais, año, censo")

def lee_poblaciones(ruta_fichero):
    """
    lee el fichero de entrada y devuelve una lista de tuplas de tipo RegistroPoblacion.
    """
    res = []
    with open(ruta_fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        for pais,acronimo,año,poblacion in lector:
            año = int(año)
            poblacion = int(poblacion)
            dato_año_pais = RegistroPoblacion(pais,acronimo,año,poblacion)
            res.append(dato_año_pais)
    return(res)

def calcula_paises(poblaciones): 
    """
    toma una lista de tuplas de tipo RegistroPoblacion y devuelve una lista ordenada alfabéticamente 
    con los nombres de los países para los que hay datos.
    """
    paises = set()
    for registro in poblaciones:
        paises.add(registro.pais)
    return sorted(paises)

def filtra_por_pais(poblaciones, nombre_o_codigo): 
    """
    toma una lista de tuplas de tipo RegistroPoblacion, y el nombre o código de un país, 
    y devuelve una lista de tuplas con los datos del país que se pasa como parámetro (año y censo) 
    (NOTA: He añadido país para poder ponerle nombre a la gráfica). 
    ¡Importante!: el país puede venir expresado en el parámetro nombre_o_codigo 
    con su nombre completo o con su código.
    """
    res = []
    for registro in poblaciones:
        if (registro.pais == nombre_o_codigo or registro.codigo == nombre_o_codigo):
            tupla = Tuplaaño(registro.pais, registro.año, registro.censo)
            res.append(tupla)
    return(res)

def filtra_por_paises_y_anyo(poblaciones, anyo, paises): 
    """
    toma una lista de tuplas de tipo RegistroPoblacion, un año y un conjunto de nombres de países, 
    y devuelve una lista de tuplas (nombre_pais, num_habitantes) con los datos del año pasado 
    como parámetro para los países incluidos en el parámetro paises.
    """
    res = []
    for registro in poblaciones:
        if registro.año == int(anyo):
            if registro.pais in paises:
                tupla = Tuplapais(registro.pais, registro.censo)
                res.append(tupla)
    return(res)

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo): 
    """
    toma una lista de tuplas de tipo RegistroPoblacion y el nombre o código de un país,
    y genera una gráfica con la curva de evolución de la población del país dado como parámetro. 
    ¡Importante!: el país puede venir expresado en el parámetro nombre_o_codigo 
    con su nombre completo o con su código.
    """
    lista_años = []
    lista_habitantes = []
    lista_filtrada = filtra_por_pais(poblaciones, nombre_o_codigo)
    for registro in lista_filtrada:
        lista_años.append(registro.año)
        lista_habitantes.append(registro.censo)

    plt.title(f"Evolucion poblacional de {registro.pais}")
    plt.plot(lista_años, lista_habitantes)
    plt.show()

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises): 
    """
    toma una lista de tuplas de tipo RegistroPoblacion, un año y un conjunto de nombres de países 
    y genera una gráfica de barras con la población de esos países en el año dado como parámetro. 
    Los países se mostrarán en el eje X en orden alfabético.
    """
    lista_paises = []
    lista_habitantes = []
    lista_filtrada = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    lista_filtrada.sort()
    for registro in lista_filtrada:
        lista_paises.append(registro.pais)
        lista_habitantes.append(registro.censo)
    plt.title(f"Comparación de {paises}")
    plt.bar(lista_paises, lista_habitantes)
    plt.show()