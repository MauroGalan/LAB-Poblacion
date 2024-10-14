from poblacion import lee_poblaciones
from poblacion import calcula_paises, filtra_por_pais, filtra_por_paises_y_anyo,muestra_evolucion_poblacion,muestra_comparativa_paises_anyo

if __name__ == "__main__":
    print(lee_poblaciones("data/population.csv")[:5])

    lista_paises = calcula_paises(lee_poblaciones("data/population.csv"))
    print(lista_paises)

    registros_pais = filtra_por_pais(lee_poblaciones("data/population.csv"), "CSS")
    print(registros_pais)

if __name__ == "__main__":
    registros_paises = filtra_por_paises_y_anyo(lee_poblaciones("data/population.csv"), "1990",("Bangladesh","Barbados","Belarus"))
    print(registros_paises)

if __name__ == "__main__":
    muestra_evolucion_poblacion(lee_poblaciones("data/population.csv"), "ARB")

if __name__ == "__main__":
    muestra_comparativa_paises_anyo(lee_poblaciones("data/population.csv"), 1990, ("Belarus","Bangladesh","Barbados"))